import unittest
from unittest.mock import patch
from stockbot.toss import TossReadOnly
from stockbot.toss_gui import holding_rows


class TossViewTests(unittest.TestCase):
    def test_decimal_and_unmanaged(self):
        item = dict(symbol='AAPL', name='Apple', marketCountry='US', quantity='0.123456789',
                    currency='USD', averagePurchasePrice='203.0001', lastPrice='204.002')
        row = holding_rows({'complete': True, 'positions': [item]})[0]
        self.assertEqual(row[3], '0.123456789')
        self.assertEqual(row[-1], '관리 대상 아님')
        self.assertNotIn('account_id', row)

    def test_incomplete_or_changed_schema_rejected(self):
        with self.assertRaises(ValueError):
            holding_rows({'complete': False, 'positions': []})
        with self.assertRaises(KeyError):
            holding_rows({'complete': True, 'positions': [{}]})

    def test_no_orders_or_cancellations(self):
        with patch.dict('os.environ', {'TOSS_CLIENT_ID': 'fixture', 'TOSS_CLIENT_SECRET': 'fixture'}):
            broker = TossReadOnly()
        with patch.object(broker, '_send') as send:
            with self.assertRaises(RuntimeError):
                broker.submit({})
            with self.assertRaises(RuntimeError):
                broker.cancel('test')
            send.assert_not_called()
