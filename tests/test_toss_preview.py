import copy
import os
import sys
import time
import unittest
from datetime import datetime, timezone
from stockbot.toss_preview import preview, inputs, PreviewBlocked, describe

NOW = datetime(2026, 10, 26, 14, 0, tzinfo=timezone.utc)


class PreviewBroker:
    def __init__(self):
        self.calls = []
        self.snapshots = 0
        self.snapshot = {'complete': True, 'account_id': 'fixture', 'positions': [], 'open_orders': []}
        self.data = {
            '/api/v1/conditional-orders': {'hasNext': False, 'nextCursor': None, 'conditionalOrders': []},
            '/api/v1/stocks': [{'symbol': 'TEST', 'currency': 'USD', 'market': 'NASDAQ', 'status': 'ACTIVE',
                               'securityType': 'STOCK', 'isCommonShare': True}],
            '/api/v1/prices': [{'symbol': 'TEST', 'currency': 'USD', 'lastPrice': '5', 'timestamp': NOW.isoformat()}],
            '/api/v1/exchange-rate': {'baseCurrency': 'USD', 'quoteCurrency': 'KRW', 'rate': '1400',
                                    'validFrom': '2026-10-26T13:59:30+00:00', 'validUntil': '2026-10-26T14:00:30+00:00'},
            '/api/v1/commissions': [{'marketCountry': 'US', 'commissionRate': '0.001', 'startDate': None, 'endDate': None}],
            '/api/v1/buying-power': {'currency': 'USD', 'cashBuyingPower': '100'},
        }

    def get(self, path, params=None):
        self.calls.append((path, params))
        return copy.deepcopy(self.data[path])

    def account_snapshot(self):
        self.snapshots += 1
        return copy.deepcopy(self.snapshot)

    def submit(self, *args):
        raise AssertionError('Order prohibited')

    cancel = submit


class PreviewTests(unittest.TestCase):
    def run_preview(self, broker=None, price='5', qty='1'):
        return preview(broker or PreviewBroker(), 'TEST', price, qty, now=lambda: NOW)

    def test_budget_and_read_only(self):
        broker = PreviewBroker()
        result = self.run_preview(broker)
        self.assertTrue(result['within_budget'])
        self.assertFalse(result['orders_enabled'])
        self.assertEqual(result['fee_usd'], '0.01')
        self.assertEqual(result['buffered_krw'], '7085')
        self.assertEqual(broker.snapshots, 2)
        self.assertEqual(len(broker.calls), 7)
        self.assertIn('주문 전송 불가', describe(result))

    def test_oversized_or_no_cash(self):
        result = self.run_preview(price='10')
        self.assertFalse(result['within_budget'])
        broker = PreviewBroker()
        broker.data['/api/v1/buying-power']['cashBuyingPower'] = '0'
        self.assertIn('달러 현금', self.run_preview(broker)['reasons'][0])

    def test_invalid_inputs_no_network(self):
        for symbol, price, qty in [('A,B','5','1'),('TEST','NaN','1'),('TEST','Infinity','1'),
                                   ('TEST','1e100','1'),('TEST','0','1'),('TEST','0.9','1'),
                                   ('TEST','1.001','1'),('TEST','5','0.1'),('TEST','5','-1'),('TEST','5','0')]:
            with self.subTest((symbol, price, qty)), self.assertRaises(PreviewBlocked):
                inputs(symbol, price, qty)

    def test_existing_holdings_excluded(self):
        broker = PreviewBroker()
        broker.snapshot['positions'] = [{'symbol': 'TEST', 'quantity': '0.0001'}]
        with self.assertRaisesRegex(PreviewBlocked, '기존 보유'):
            self.run_preview(broker)
        self.assertEqual(broker.calls, [])

    def test_unrelated_holdings_untouched(self):
        broker = PreviewBroker()
        broker.snapshot['positions'] = [{'symbol': 'OTHER', 'quantity': '3'}]
        self.assertTrue(self.run_preview(broker)['within_budget'])

    def test_any_general_order_blocks(self):
        broker = PreviewBroker()
        broker.snapshot['open_orders'] = [{'symbol': 'OTHER', 'side': 'BUY', 'price': None}]
        with self.assertRaisesRegex(PreviewBlocked, '일반 미체결'):
            self.run_preview(broker)

    def test_conditions_and_pagination(self):
        for field, value in [('conditionalOrders', [{}]), ('hasNext', True), ('nextCursor', 'next')]:
            broker = PreviewBroker()
            broker.data['/api/v1/conditional-orders'][field] = value
            with self.subTest(field), self.assertRaises(PreviewBlocked):
                self.run_preview(broker)

    def test_data_validation(self):
        cases = [('/api/v1/prices', 'currency', 'KRW'), ('/api/v1/prices', 'symbol', 'WRONG'),
                 ('/api/v1/prices', 'timestamp', '2026-10-26T13:58:00+00:00'),
                 ('/api/v1/prices', 'timestamp', '2026-10-26T14:01:00+00:00'),
                 ('/api/v1/prices', 'timestamp', '2026-10-26T14:00:00'),
                 ('/api/v1/stocks', 'status', 'DELISTED'), ('/api/v1/stocks', 'securityType', 'ETF'),
                 ('/api/v1/stocks', 'currency', 'KRW'), ('/api/v1/stocks', 'isCommonShare', False)]
        for path, field, value in cases:
            broker = PreviewBroker()
            broker.data[path][0][field] = value
            with self.subTest((field, value)), self.assertRaises(PreviewBlocked):
                self.run_preview(broker)

    def test_fx_expiry_and_currency(self):
        for field, value in [('validUntil', NOW.isoformat()), ('baseCurrency', 'KRW'), ('rate', '0')]:
            broker = PreviewBroker()
            broker.data['/api/v1/exchange-rate'][field] = value
            with self.subTest(field), self.assertRaises(PreviewBlocked):
                self.run_preview(broker)

    def test_expired_or_ambiguous_fee(self):
        for fees in [[], [{'marketCountry': 'US', 'commissionRate': '0.001', 'endDate': '2026-10-25'}],
                     [{'marketCountry': 'US', 'commissionRate': '0.001'}] * 2]:
            broker = PreviewBroker()
            broker.data['/api/v1/commissions'] = fees
            with self.subTest(fees), self.assertRaises(PreviewBlocked):
                self.run_preview(broker)

    def test_changed_account_or_new_order(self):
        for change in [{'account_id': 'other'}, {'open_orders': [{}]}, {'positions': [{'symbol': 'TEST'}]}]:
            broker = PreviewBroker()
            original = broker.account_snapshot
            def changed():
                snapshot = original()
                if broker.snapshots == 2:
                    snapshot.update(change)
                return snapshot
            broker.account_snapshot = changed
            with self.subTest(change), self.assertRaises(PreviewBlocked):
                self.run_preview(broker)

    def test_time_budget(self):
        ticks = iter([0, 0, 31])
        with self.assertRaisesRegex(PreviewBlocked, '30초'):
            preview(PreviewBroker(), 'TEST', '5', '1', now=lambda: NOW, monotonic=lambda: next(ticks))


@unittest.skipUnless(sys.platform == 'win32' or os.environ.get('DISPLAY'), 'Native display required')
class PreviewGuiTests(unittest.TestCase):
    def test_open_calculate_close(self):
        import tkinter as tk
        from tkinter import ttk
        from unittest.mock import patch
        from stockbot.toss_gui import TossDashboard
        root = tk.Tk()
        try:
            app = TossDashboard(root, PreviewBroker)
            app.open_preview()
            root.update()
            dialog = next(w for w in root.winfo_children() if isinstance(w, tk.Toplevel))
            def descendants(widget):
                return [child for w in widget.winfo_children() for child in [w, *descendants(w)]]
            widgets = descendants(dialog)
            entries = [w for w in widgets if isinstance(w, ttk.Entry)]
            for entry, value in zip(entries, ['TEST', '5', '1']):
                entry.delete(0, 'end')
                entry.insert(0, value)
            calculate = next(w for w in widgets if isinstance(w, ttk.Button) and '예산 계산' in w.cget('text'))
            with patch('stockbot.toss_gui.preview', side_effect=lambda b,s,p,q: preview(b,s,p,q,now=lambda: NOW)):
                calculate.invoke()
                deadline = time.monotonic() + 5
                while app.busy and time.monotonic() < deadline:
                    root.update()
                    time.sleep(.01)
            output = next(w for w in widgets if isinstance(w, tk.Text))
            self.assertIn('예산 검사 통과', output.get('1.0', 'end'))
            self.assertFalse(app.busy)
            self.assertEqual(str(output.cget('state')), 'disabled')
            next(w for w in widgets if isinstance(w, ttk.Button) and w.cget('text') == '닫기').invoke()
            root.update()
            self.assertFalse(dialog.winfo_exists())
        finally:
            root.destroy()
