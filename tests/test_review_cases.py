import copy
import sqlite3
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import Mock,patch
import test_brackets
from stockbot import review_cases as review
from stockbot.cli import cycle
from stockbot.gui import Dashboard

class ReviewTests(unittest.TestCase):
    setUp=test_brackets.BracketTests.setUp
    check=test_brackets.BracketTests.check

    def test_replacement_stays_blocked_after_normal_read(self):
        self.check();original=copy.deepcopy(self.root)
        self.root.update(status='pending_replace',replaced_by='replacement-id')
        data=self.check();case=next(c for c in data['review']['cases'] if c['code']=='order_replaced')
        self.assertTrue(case['manual_review_required']);self.assertFalse(data['inventory']['ready'])
        self.root.clear();self.root.update(original)
        data=self.check();self.assertEqual(data['reconciliation']['unresolved'],0)
        self.assertFalse(data['inventory']['ready']);self.assertGreater(data['review']['blocking'],0)
        self.c['symbols']=['MSFT']
        with self.assertRaises(RuntimeError):cycle(self.c,True,self.b)
        self.assertEqual(len(self.b.sent),1)

    def test_changed_price_evidence(self):
        self.root['limit_price']='999'
        data=self.check();case=next(c for c in data['review']['cases'] if c['code']=='price_changed')
        self.assertEqual(case['observed'],'999');self.assertNotEqual(case['expected'],'999')
        self.assertFalse(data['review']['override_available'])

    def test_quantity_does_not_infer_split(self):
        self.root['qty']=str(self.qty+1)
        data=self.check();case=next(c for c in data['review']['cases'] if c['code']=='quantity_changed')
        self.assertIn('미확정',case['next_action']);self.assertTrue(case['active'])

    def test_transient_failure_recovers_read_only(self):
        original=self.b.find_order
        def fail(cid):raise TimeoutError('SECRET_DO_NOT_SHOW')
        self.b.find_order=fail;data=self.check()
        self.assertNotIn('SECRET_DO_NOT_SHOW',str(data));self.assertGreater(data['review']['blocking'],0)
        self.b.find_order=original;data=self.check()
        self.assertTrue(data['inventory']['ready']);self.assertEqual(data['review']['blocking'],0)
        self.assertTrue(any(c['code']=='lookup_failed' and not c['active'] for c in data['review']['cases']))
        self.assertEqual(len(self.b.sent),1)

    def test_sticky_persists_without_repeat_spam(self):
        self.root['replaced_by']='replacement-id';self.check();self.check()
        with closing(sqlite3.connect(Path(self.temp.name)/'orders.sqlite')) as db:
            snap=review.snapshot(db);case=next(c for c in snap['cases'] if c['code']=='order_replaced')
            self.assertEqual(case['occurrences'],1);self.assertTrue(case['active'])
            review.resolve_transient(db,self.cid);db.commit()
        with closing(sqlite3.connect(Path(self.temp.name)/'orders.sqlite')) as db:self.assertGreater(review.blocking(db),0)

    def test_detail_dialog_does_not_acknowledge_or_trade(self):
        self.root['replaced_by']='replacement-id';data=self.check()
        case=next(c for c in data['review']['cases'] if c['code']=='order_replaced')
        app=Dashboard.__new__(Dashboard);table=Mock();table.selection.return_value=['row']
        app.tables={'review':table};app.review_items={'row':case};app.root=Mock()
        with patch('stockbot.gui.messagebox.showinfo') as info:
            self.assertEqual(app.show_review_detail(),'break');self.assertIn('차단은 해제되지 않습니다',info.call_args.args[1])
        self.assertFalse(self.check()['inventory']['ready']);self.assertEqual(len(self.b.sent),1)
