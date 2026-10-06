"""Official Toss Open API read-only adapter. No live order submission."""
import json
import os
import time
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError

class TossReadOnly:
    base = 'https://openapi.tossinvest.com'
    def __init__(self):
        self.client_id=os.environ.get('TOSS_CLIENT_ID')
        self.secret=os.environ.get('TOSS_CLIENT_SECRET')
        self.account=os.environ.get('TOSS_ACCOUNT_SEQ')
        if not self.client_id or not self.secret:
            raise ValueError('Set TOSS_CLIENT_ID and TOSS_CLIENT_SECRET')
        self.token=None;self.expires=0
    def _send(self,path,params=None,body=None,headers=None):
        url=self.base+path
        if params: url+='?'+urlencode(params)
        req=Request(url,data=body,headers=headers or {})
        try:
            with urlopen(req,timeout=20) as r: return json.load(r)
        except HTTPError as e:
            raise RuntimeError(f'Toss HTTP {e.code}; check credentials, allowed IP and permissions') from None
    def get(self,path,params=None):
        if not self.token or time.monotonic() >= self.expires:
            data=urlencode({'grant_type':'client_credentials','client_id':self.client_id,'client_secret':self.secret}).encode()
            r=self._send('/oauth2/token',body=data,headers={'Content-Type':'application/x-www-form-urlencoded'})
            self.token=r['access_token'];self.expires=time.monotonic()+max(0,int(r['expires_in'])-60)
        headers={'Authorization':'Bearer '+self.token}
        if self.account: headers['X-Tossinvest-Account']=str(self.account)
        r=self._send(path,params,headers=headers)
        if 'error' in r or 'result' not in r: raise RuntimeError('Invalid Toss response')
        return r['result']
    def account_snapshot(self):
        accounts=self.get('/api/v1/accounts')
        if not self.account:
            if len(accounts)!=1: raise ValueError('Select TOSS_ACCOUNT_SEQ explicitly; account selection ambiguous')
            self.account=str(accounts[0]['accountSeq'])
        if str(self.account) not in {str(a['accountSeq']) for a in accounts}:
            raise ValueError('Selected account not found')
        holdings=self.get('/api/v1/holdings')
        orders=self.get('/api/v1/orders',{'status':'OPEN'})
        if orders['hasNext'] or orders['nextCursor'] is not None: raise ValueError('Incomplete open-order snapshot')
        return {'complete':True,'account_id':str(self.account),'as_of':datetime.now(timezone.utc).isoformat(),
                'positions':holdings['items'],'open_orders':orders['orders'],
                'coverage':'API-supported equity orders only; conditional orders and unsupported order types excluded'}
    def submit(self,*args,**kwargs):
        raise RuntimeError('Toss live orders disabled in this release')
    def cancel(self,*args,**kwargs):
        raise RuntimeError('Toss live cancellation disabled in this release')

if __name__=='__main__':
    try:
        r=TossReadOnly().account_snapshot()
        # Print counts only, no credentials, account IDs or full portfolio.
        print(json.dumps({'status':'read_only_connected','positions':len(r['positions']),
                          'open_orders':len(r['open_orders']),'as_of':r['as_of']},indent=2))
    except Exception as e:
        print(str(e));raise SystemExit(1) from None
