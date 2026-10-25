from dataclasses import dataclass
from datetime import date
import math

@dataclass(frozen=True)
class Bar:
    day: date
    open: float
    high: float
    low: float
    close: float
    volume: float

    def __post_init__(self):
        values = (self.open, self.high, self.low, self.close, self.volume)
        if not all(math.isfinite(x) for x in values):
            raise ValueError("Non-finite bar")
        if min(values[:4]) <= 0 or self.volume < 0:
            raise ValueError("Invalid price/volume")
        if self.low > min(self.open, self.close) or self.high < max(self.open, self.close) or self.low > self.high:
            raise ValueError("Invalid OHLC")

def signal(bars, ratio=3.0, max_return=0.03):
    if len(bars) < 31:
        return None
    if any(a.day >= b.day for a, b in zip(bars, bars[1:])):
        raise ValueError("Dates must be unique and ascending")
    avg = sum(b.volume for b in bars[-31:-1]) / 30
    if avg <= 0:
        return None
    vr = bars[-1].volume / avg
    ret = bars[-1].close / bars[-22].close - 1
    if vr >= ratio and ret <= max_return:
        return {"date": bars[-1].day.isoformat(), "close": bars[-1].close,
                "volume_ratio": vr, "return_21d": ret}
    return None

def size(equity, buying_power, price, fraction):
    if not all(math.isfinite(x) and x > 0 for x in (equity, buying_power, price, fraction)):
        return 0
    return max(0, math.floor(min(equity * fraction, buying_power) / price))

def backtest(bars, config, cash=10000.0, fee=0.001, slippage=0.001, *, sell_tax=0.0, entry_filter=None, start_index=0, liquidate_end=False):
    """Single asset daily approximation. Past-only, next-open, stop first on ambiguity."""
    if not math.isfinite(cash) or cash<=0:raise ValueError('Invalid research capital')
    if any(not math.isfinite(v) or not 0<=v<1 for v in (fee,slippage,sell_tax)) or fee+sell_tax>=1:raise ValueError('Invalid research costs')
    if type(start_index) is not int or not 0<=start_index<=len(bars):raise ValueError('Invalid evaluation start')
    if any(a.day>=b.day for a,b in zip(bars,bars[1:])):raise ValueError('Dates must be unique and ascending')
    for key in ('max_position_fraction','stop_loss','take_profit','max_gap'):
        if not math.isfinite(config[key]) or not 0<config[key]<1:raise ValueError('Invalid strategy risk setting')
    if not math.isfinite(config['volume_ratio']) or config['volume_ratio']<=0 or not math.isfinite(config['max_return']) or not -1<config['max_return']<1:raise ValueError('Invalid signal setting')
    if entry_filter is None:
        from .strategies import configured_filter
        entry_filter=configured_filter(config)
    initial=cash;qty=0;stop=target=position_cost=0.0
    trades=[];curve=[];profits=[];costs=0.0;held_days=0
    def exit_position(raw,bar,reason):
        nonlocal cash,qty,costs
        price=raw*(1-slippage);proceeds=qty*price*(1-fee-sell_tax)
        costs+=qty*(raw-price)+qty*price*(fee+sell_tax)
        profits.append(proceeds-position_cost);cash+=proceeds
        trades.append({'date':str(bar.day),'side':'sell','qty':qty,'price':price,'reason':reason})
        qty=0
    for i in range(start_index,len(bars)):
        bar=bars[i];entered=False;was_held=bool(qty)
        if not qty and i>=31 and signal(bars[:i],config['volume_ratio'],config['max_return']):
            if entry_filter is None or entry_filter(bars[:i]):
                previous=bars[i-1].close;entry=bar.open*(1+slippage)
                proposed_stop=previous*(1-config['stop_loss']);proposed_target=previous*(1+config['take_profit'])
                if abs(bar.open/previous-1)<=config['max_gap'] and 0<proposed_stop<entry<proposed_target:
                    qty=size(cash,cash,entry*(1+fee),config['max_position_fraction'])
                    if qty:
                        position_cost=qty*entry*(1+fee);cash-=position_cost
                        costs+=qty*(entry-bar.open)+qty*entry*fee
                        stop,target=proposed_stop,proposed_target
                        trades.append({'date':str(bar.day),'side':'buy','qty':qty,'price':entry})
                        entered=True
        if qty:
            if bar.low<=stop:exit_position(min(bar.open,stop),bar,'stop')
            elif bar.high>=target:exit_position(target if entered else max(bar.open,target),bar,'target')
        held_days+=int(was_held or entered)
        if qty and liquidate_end and i==len(bars)-1:exit_position(bar.close,bar,'research_end')
        value=cash+qty*bar.close
        if not all(math.isfinite(v) for v in (cash,value,costs)):raise ValueError('Non-finite simulation result')
        curve.append(value)
    peak=initial;dd=0.0
    for value in curve:
        peak=max(peak,value);dd=max(dd,1-value/peak)
    gains=sum(p for p in profits if p>0);losses=-sum(p for p in profits if p<0)
    ending=curve[-1] if curve else cash
    return {'ending_equity':ending,'max_drawdown':dd,'open_qty':qty,'trades':trades,
            'total_return':ending/initial-1,'closed_trades':len(profits),
            'win_rate':sum(p>0 for p in profits)/len(profits) if profits else None,
            'profit_factor':gains/losses if losses else None,'estimated_costs':costs,
            'exposure_days':held_days,'evaluation_days':len(curve),'ending_cash':cash}
