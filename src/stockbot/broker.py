import json
import os
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError

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
            raise RuntimeError(f"Alpaca HTTP {exc.code}") from None

    def bars(self, symbol, start, end, feed):
        rows, token = [], None
        while True:
            params = {"timeframe":"1Day","start":start,"end":end,"feed":feed,"adjustment":"split","limit":1000,"sort":"asc"}
            if token:
                params["page_token"] = token
            response = self.request(f"/v2/stocks/{symbol}/bars", params, data=True)
            rows.extend(response.get("bars") or [])
            token = response.get("next_page_token")
            if not token:
                return rows

    def quote(self, symbol, feed):
        return self.request(f"/v2/stocks/{symbol}/quotes/latest", {"feed":feed}, data=True)["quote"]
