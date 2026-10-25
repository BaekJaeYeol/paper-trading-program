import json
import os
import time
from urllib.request import Request, urlopen
from urllib.parse import urlencode,quote
from urllib.error import HTTPError

class AlpacaHTTPError(RuntimeError):
    def __init__(self,status):
        self.status=status
        super().__init__(f'Alpaca HTTP {status}')

class AlpacaPaper:
    # No configurable live URL: this release can only submit paper orders.
    trading = "https://paper-api.alpaca.markets"
    data = "https://data.alpaca.markets"

    def __init__(self):
        self.key = os.environ.get("APCA_API_KEY_ID")
        self.secret = os.environ.get("APCA_API_SECRET_KEY")
        if not self.key or not self.secret:
            raise ValueError("Set APCA_API_KEY_ID and APCA_API_SECRET_KEY (paper keys)")

    def request(self, path, params=None, body=None, data=False):
        url = (self.data if data else self.trading)+path
        if params:
            url += "?"+urlencode(params)
        headers = {"APCA-API-KEY-ID":self.key,"APCA-API-SECRET-KEY":self.secret}
        payload = None
        if body is not None:
            headers["Content-Type"] = "application/json"
            payload = json.dumps(body).encode()
        req = Request(url, data=payload, headers=headers)
        try:
            with urlopen(req, timeout=20) as response:
                return json.load(response)
        except HTTPError as exc:
            # Do not print response bodies, headers, or credentials.
            raise AlpacaHTTPError(exc.code) from None

    def bars(self, symbol, start, end, feed):
        rows, token, seen = [], None, set()
        started=time.monotonic()
        for _ in range(10):
            if time.monotonic()-started>=60:raise RuntimeError('Daily bar lookup exceeded time budget')
            params = {"timeframe":"1Day","start":start,"end":end,"feed":feed,"adjustment":"split","limit":1000,"sort":"asc"}
            if token:
                params["page_token"] = token
            response = self.request(f"/v2/stocks/{symbol}/bars", params, data=True)
            if time.monotonic()-started>=60:raise RuntimeError('Daily bar lookup exceeded time budget')
            if not isinstance(response,dict) or not isinstance(response.get('bars'),(list,type(None))):raise ValueError('Invalid daily bar page')
            rows.extend(response.get("bars") or [])
            if len(rows)>5000:raise RuntimeError('Daily bar count limit exceeded')
            token = response.get("next_page_token")
            if not token:
                return rows
            if not isinstance(token,str) or len(token)>2048 or token in seen:raise RuntimeError('Invalid or repeated daily bar token')
            seen.add(token)
        raise RuntimeError('Daily bar page limit exceeded')

    def quote(self, symbol, feed):
        return self.request(f"/v2/stocks/{symbol}/quotes/latest", {"feed":feed}, data=True)["quote"]

    def find_order(self,client_id):
        try:return self.request('/v2/orders:by_client_order_id',{'client_order_id':client_id})
        except AlpacaHTTPError as exc:
            if exc.status==404:return None
            raise

    def bracket_order(self,order_id):
        return self.request('/v2/orders/'+quote(order_id,safe=''),{'nested':'true'})
