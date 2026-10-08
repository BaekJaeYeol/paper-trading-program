import datetime, hashlib, json, os, sys, tempfile, unittest, zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from drive_sync import compact, payload

class ArchiveTests(unittest.TestCase):
    def put(self,folder,value,month):
        data=json.dumps(value).encode();p=folder/('investment-lab-'+hashlib.sha256(data).hexdigest()+'.json');p.write_bytes(data)
        stamp=datetime.datetime(2026,month,5,tzinfo=datetime.timezone.utc).timestamp();os.utime(p,(stamp,stamp));return p,data
    def test_months_latest_and_preserve_unrelated(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);a,old=self.put(folder,payload({'source':'synthetic','selected':'cash'},symbol='SPY'),8)
            b,new=self.put(folder,payload({'source':'synthetic','selected':'trend'},symbol='SPY'),9)
            untouched=folder/'notes.json';untouched.write_text('mine')
            compact(folder)
            self.assertFalse(a.exists());self.assertFalse(b.exists());self.assertEqual(untouched.read_text(),'mine')
            self.assertEqual(next(folder.glob('*latest*.json')).read_bytes(),new)
            for month,data in [('08',old),('09',new)]:
                with zipfile.ZipFile(folder/f'investment-lab-history-2026-{month}.zip') as z:self.assertEqual(z.read(z.namelist()[0]),data)
            # Late arrival of an old result must not replace the latest result.
            self.put(folder,payload({'source':'synthetic','selected':'cash'},symbol='SPY'),8);compact(folder)
            self.assertEqual(next(folder.glob('*latest*.json')).read_bytes(),new)
    def test_corrupt_archive_keeps_original(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);p,data=self.put(folder,payload({'source':'synthetic'}),8)
            (folder/'investment-lab-history-2026-08.zip').write_bytes(b'broken')
            with self.assertRaises(zipfile.BadZipFile):compact(folder)
            self.assertEqual(p.read_bytes(),data)
    def test_same_month_append_and_no_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp)
            for strategy in ['cash','trend','cash']:
                self.put(folder,payload({'source':'synthetic','selected':strategy}),8);compact(folder)
            with zipfile.ZipFile(folder/'investment-lab-history-2026-08.zip') as z:self.assertEqual(len(z.namelist()),2)
