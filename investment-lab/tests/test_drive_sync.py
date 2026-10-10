import json, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from drive_sync import DriveSync, payload

class SyncTests(unittest.TestCase):
    def test_queue_disconnect_retry_and_deduplicate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);folder=root/'drive';folder.mkdir();sync=DriveSync(root/'work')
            sync.configure(str(folder),True);folder.rmdir()
            value=payload({'source':'synthetic','selected':'cash','api_key':'secret'})
            self.assertIn('대기',sync.export(value));self.assertFalse(folder.exists())
            self.assertEqual(len(list((root/'work'/'drive_outbox').glob('*.json'))),1)
            folder.mkdir();self.assertIn('미확인',sync.export())
            sync.export(value);self.assertEqual(len(list(folder.glob('*.json'))),1)
            saved=json.loads(next(folder.glob('*.json')).read_text(encoding='utf-8'))
            self.assertNotIn('api_key',saved['research']);self.assertFalse(saved['cloud_upload_verified'])
            self.assertEqual(list((root/'work'/'drive_outbox').glob('*.json')),[])
            self.assertTrue(DriveSync(root/'work').settings['enabled'])
    def test_disabled_and_local_workspace_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            sync=DriveSync(Path(tmp)/'work');self.assertIn('꺼짐',sync.export({'x':1}))
            sync.work.mkdir()
            with self.assertRaises(ValueError):sync.configure(str(sync.work),True)
    def test_full_paper_export(self):
        from paper import Paper
        with tempfile.TemporaryDirectory() as tmp:
            paper=Paper(Path(tmp)/'paper.sqlite')
            with paper.connect() as db:
                for i in range(120):db.execute('INSERT INTO ledger VALUES(?,?,?,?,?,?,?)',(str(i),0,'hold',0,1,0,100))
            self.assertEqual(len(paper.snapshot()['ledger']),0)  # inactive account
            with paper.connect() as db:db.execute('INSERT INTO account VALUES(1,?,?,?,?,?)',(json.dumps({'strategy':'cash'}),100,0,'119',1))
            self.assertEqual(len(paper.snapshot()['ledger']),100)
            self.assertEqual(len(paper.snapshot(full=True)['ledger']),120)
