"""KIS domestic paper account connection. No order endpoints are implemented."""
import json
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPRedirectHandler

PAPER_URL = 'https://openapivts.koreainvestment.com:29443'
BALANCE_PATH = '/uapi/domestic-stock/v1/trading/inquire-balance'

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

class KISPaper:
    def __init__(self, key, secret, account, product):
        if not key.strip() or not secret.strip():
            raise ValueError('모의투자 App Key와 App Secret을 입력하세요.')
        if not re.fullmatch(r'[0-9]{8}', account) or not re.fullmatch(r'[0-9]{2}', product):
            raise ValueError('모의계좌 앞 8자리와 뒤 2자리를 확인하세요.')
        self.key, self.secret = key.strip(), secret.strip()
        self.account, self.product = account, product
        self.token, self.expires = None, 0
        self.opener = build_opener(NoRedirect())

    def _send(self, path, params=None, body=None, headers=None):
        if path not in ('/oauth2/tokenP', BALANCE_PATH):
            raise ValueError('조회 전용 연결입니다.')
        url = PAPER_URL + path
        if params:
            url += '?' + urlencode(params)
        payload = json.dumps(body).encode() if body is not None else None
        request = Request(url, data=payload, headers={'Content-Type': 'application/json', **(headers or {})})
        try:
            with self.opener.open(request, timeout=20) as response:
                data = json.load(response)
                continuation = response.headers.get('tr_cont', '')
        except (HTTPError, URLError, ValueError):
            raise RuntimeError('KIS 연결 실패: 모의투자 키·계좌·네트워크를 확인하세요.') from None
        if not isinstance(data, dict) or (path == BALANCE_PATH and data.get('rt_cd') != '0'):
            raise RuntimeError('KIS 조회 실패: 모의투자 신청 상태와 계좌 정보를 확인하세요.')
        return data, continuation

    def authenticate(self):
        if self.token and time.monotonic() < self.expires:
            return
        data, _ = self._send('/oauth2/tokenP', body={'grant_type':'client_credentials',
                                                   'appkey':self.key, 'appsecret':self.secret})
        if not data.get('access_token'):
            raise RuntimeError('KIS 모의투자 인증 실패')
        self.token = data['access_token']
        self.expires = time.monotonic() + max(0, int(data.get('expires_in', 86400)) - 60)

    def snapshot(self):
        self.authenticate()
        params = {'CANO':self.account, 'ACNT_PRDT_CD':self.product, 'AFHR_FLPR_YN':'N',
                  'OFL_YN':'', 'INQR_DVSN':'02', 'UNPR_DVSN':'01', 'FUND_STTL_ICLD_YN':'N',
                  'FNCG_AMT_AUTO_RDPT_YN':'N', 'PRCS_DVSN':'00',
                  'CTX_AREA_FK100':'', 'CTX_AREA_NK100':''}
        headers = {'authorization':'Bearer ' + self.token, 'appkey':self.key,
                   'appsecret':self.secret, 'tr_id':'VTTC8434R', 'custtype':'P'}
        positions, seen = [], set()
        summary = None
        for page in range(100):
            if page:
                time.sleep(0.6)
            data, continuation = self._send(BALANCE_PATH, params=params, headers=headers)
            if summary is None:
                summary = data['output2'][0]
            for p in data['output1']:
                if float(p['hldg_qty']) <= 0:
                    continue
                positions.append({'symbol':p['pdno'], 'qty':p['hldg_qty'],
                                  'avg_entry_price':p['pchs_avg_pric'], 'current_price':p['prpr'],
                                  'unrealized_pl':p['evlu_pfls_amt']})
            if continuation not in ('M','F'):
                return {'equity':float(summary['tot_evlu_amt']), 'cash':float(summary['dnca_tot_amt']),
                        'buying_power':None, 'daily_pnl':None, 'positions':positions, 'orders':[]}
            cursor = (data.get('ctx_area_fk100',''), data.get('ctx_area_nk100',''))
            if cursor == ('','') or cursor in seen:
                raise RuntimeError('잔고 연속조회 실패: 전체 잔고를 확인하지 못했습니다.')
            seen.add(cursor)
            params['CTX_AREA_FK100'], params['CTX_AREA_NK100'] = cursor
            headers['tr_cont'] = 'N'
        raise RuntimeError('잔고 조회 한도 초과')
