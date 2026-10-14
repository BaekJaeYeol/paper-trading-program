import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from bar_reconciliation import reconcile_bars
class RevisionTests(unittest.TestCase):
 def test_small_revision_preserves_accepted_bar(self):
  old=[('a',760.,762.,759.,760.859985,100)]
  new=[('a',760.,762.,759.,760.945007,101),('b',761.,763.,760.,762.,200)]
  rows,events=reconcile_bars(old,new)
  self.assertEqual(rows[0],old[0]);self.assertEqual(rows[1],new[1]);self.assertEqual(len(events),1)
  again,_=reconcile_bars(rows,new);self.assertEqual(again,rows)
 def test_split_and_large_change_stop(self):
  with self.assertRaises(ValueError):reconcile_bars([('a',100,100,100,100,100)],[('a',50,50,50,50,200)])
 def test_missing_anchor_is_not_fabricated(self):
  rows,events=reconcile_bars([('a',100,100,100,100,100)],[('b',100,100,100,100,100)])
  self.assertEqual([r[0] for r in rows],['b'])
