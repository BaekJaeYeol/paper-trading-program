"""Durable broker-independent order controller. Only MockBroker is implemented."""
import datetime as dt
import hashlib
import json
import math
import sqlite3

TERMINAL={'filled','canceled','rejected'}
class MockBroker:
    def __init__(self,path,cash=10000.):
        self.db=sqlite3.connect(path)
        self.db.execute('CREATE TABLE IF NOT EXISTS balance (id INTEGER PRIMARY KEY,cash REAL,qty REAL)')
        self.db.execute('INSERT OR IGNORE INTO balance VALUES (1,?,0)',(cash,))
        self.db.execute('CREATE TABLE IF NOT EXISTS orders (id TEXT PRIMARY KEY, payload TEXT)');self.db.commit()
        self.lose_reply=False;self.fail_cancel=False
    def lookup(self,key):
        row=self.db.execute('SELECT payload FROM orders WHERE id=?',(key,)).fetchone()
        return json.loads(row[0]) if row else None
    def submit(self,key,side,quantity,price):
        old=self.lookup(key)
        if old:return old
        order=dict(id=key,side=side,quantity=quantity,price=price,filled=0.,fee=0.,status='accepted')
        self.db.execute('INSERT INTO orders VALUES (?,?)',(key,json.dumps(order)));self.db.commit()
        if self.lose_reply:raise TimeoutError('accepted but response lost')
        return order
    def fill(self,key,quantity):
        order=self.lookup(key)
        if order['status'] in TERMINAL:return order
        cash,qty=self.balance();price=order['price']
        q=min(quantity,order['quantity']-order['filled'],cash/price if order['side']=='buy' else qty)
        if not math.isfinite(q) or q<0:raise ValueError('Invalid fill')
        sign=1 if order['side']=='buy' else -1
        self.db.execute('UPDATE balance SET cash=?,qty=? WHERE id=1',(cash-sign*q*price,qty+sign*q))
        order['filled']+=q;order['status']='filled' if order['quantity']-order['filled']<1e-8 else 'partial'
        self.db.execute('UPDATE orders SET payload=? WHERE id=?',(json.dumps(order),key));self.db.commit();return order
    def cancel(self,key):
        if self.fail_cancel:raise TimeoutError('cancel response unavailable')
        order=self.lookup(key)
        if order and order['status'] not in TERMINAL:
            order['status']='canceled';self.db.execute('UPDATE orders SET payload=? WHERE id=?',(json.dumps(order),key));self.db.commit()
        return order
    def balance(self):return self.db.execute('SELECT cash,qty FROM balance WHERE id=1').fetchone()

class Controller:
    def __init__(self,path,broker,initial_cash=10000.,daily_limit=.03,drawdown_limit=.10):
        if not 0<daily_limit<1 or not 0<drawdown_limit<1:raise ValueError('Invalid limits')
        self.db=sqlite3.connect(path);self.broker=broker
        self.db.execute('CREATE TABLE IF NOT EXISTS intents (id TEXT PRIMARY KEY,payload TEXT)')
        self.db.execute('CREATE TABLE IF NOT EXISTS control (id INTEGER PRIMARY KEY,payload TEXT)')
        self.db.execute('INSERT OR IGNORE INTO control VALUES (1,?)',(json.dumps(dict(initial_cash=initial_cash,halted=False,
            reason='',peak=initial_cash,day=None,day_equity=initial_cash,daily_limit=daily_limit,drawdown_limit=drawdown_limit)),));self.db.commit()
    def control(self):return json.loads(self.db.execute('SELECT payload FROM control WHERE id=1').fetchone()[0])
    def save_control(self,c):self.db.execute('UPDATE control SET payload=? WHERE id=1',(json.dumps(c),));self.db.commit()
    def intents(self):return [json.loads(r[0]) for r in self.db.execute('SELECT payload FROM intents')]
    def save_order(self,o):
        self.db.execute('INSERT OR REPLACE INTO intents VALUES (?,?)',(o['id'],json.dumps(o)));self.db.commit()
    def stop(self,reason):
        c=self.control();c.update(halted=True,reason=reason);self.save_control(c)
    def reconcile(self):
        cash=self.control()['initial_cash'];qty=0.
        try:
            for o in self.intents():
                current=self.broker.lookup(o['id'])
                if current is None:
                    if o['status']!='created':raise ValueError('주문 접수 여부 불명')
                    current=o
                if any(current[k]!=o[k] for k in ('id','side','quantity','price')):raise ValueError('주문 내용 불일치')
                self.save_order(current)
                sign=1 if current['side']=='buy' else -1
                cash-=sign*current['filled']*current['price']+current.get('fee',0);qty+=sign*current['filled']
            actual=self.broker.balance()
            if abs(cash-actual[0])>1e-6 or abs(qty-actual[1])>1e-6:raise ValueError('잔고 불일치')
            return True
        except Exception as exc:self.stop('복구 중단: '+str(exc));return False
    def gate(self,price,day):
        if not math.isfinite(price) or price<=0:raise ValueError('Invalid mark')
        if not self.reconcile():return False
        c=self.control();cash,qty=self.broker.balance();equity=cash+qty*price
        if c['day']!=day:c.update(day=day,day_equity=equity)
        c['peak']=max(c['peak'],equity)
        if equity<=c['day_equity']*(1-c['daily_limit']) or equity<=c['peak']*(1-c['drawdown_limit']):c.update(halted=True,reason='손실 한도')
        self.save_control(c);return not c['halted']
    def submit(self,signal_id,side,quantity,price,day):
        if side not in ('buy','sell') or not math.isfinite(quantity) or quantity<=0:raise ValueError('Invalid order')
        key=hashlib.sha256(signal_id.encode()).hexdigest()
        existing=next((o for o in self.intents() if o['id']==key),None)
        if existing:
            if (side,quantity,price)!=(existing['side'],existing['quantity'],existing['price']):raise ValueError('주문 식별자 재사용 충돌')
            self.reconcile();return self.broker.lookup(key) or existing
        if not self.gate(price,day):raise ValueError('신규 주문 중단')
        if any(o['status'] not in TERMINAL for o in self.intents()):raise ValueError('미해결 주문 확인 필요')
        cash,qty=self.broker.balance()
        if side=='buy' and quantity*price>cash+1e-8 or side=='sell' and quantity>qty+1e-8:raise ValueError('잔고 부족')
        o=dict(id=key,side=side,quantity=quantity,price=price,status='created',filled=0.,fee=0.)
        self.save_order(o) # durable intent before any external call
        try:
            self.save_order({**o,'status':'submitting'})
            result=self.broker.submit(key,side,quantity,price);self.save_order(result);return result
        except Exception:
            self.save_order({**o,'status':'unknown'});self.stop('통신 장애: 기존 주문 조회 필요');return {**o,'status':'unknown'}
    def emergency_stop(self):
        self.stop('사용자 비상 중단');confirmed=True
        for o in self.intents():
            if o['status'] in TERMINAL:continue
            try:
                result=self.broker.cancel(o['id'])
                if result:self.save_order(result)
                if not result or result['status'] not in TERMINAL:confirmed=False
            except Exception:confirmed=False
        self.reconcile()
        return dict(halted=True,cancellation_confirmed=confirmed,liquidated=False)
