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

def backtest(bars, config, cash=10000.0, fee=0.001, slippage=0.001):
    """Single asset, next-open entries. Stop first if both exits touched."""
    qty = 0
    stop = target = 0.0
    trades = []
    curve = []
    for i, bar in enumerate(bars):
        entered = False
        if not qty and i >= 31 and signal(bars[:i], config["volume_ratio"], config["max_return"]):
            previous = bars[i-1].close
            if abs(bar.open / previous - 1) <= config["max_gap"]:
                entry = bar.open * (1 + slippage)
                qty = size(cash, cash, entry * (1+fee), config["max_position_fraction"])
                if qty:
                    cash -= qty * entry * (1+fee)
                    stop, target = previous*(1-config["stop_loss"]), previous*(1+config["take_profit"])
                    trades.append({"date":str(bar.day),"side":"buy","qty":qty,"price":entry})
                    entered = True
        if qty:
            exit_price = None
            if bar.low <= stop:
                exit_price = min(bar.open, stop)
            elif bar.high >= target:
                # On entry day, don't infer a better fill from opening gap.
                exit_price = target if entered else max(bar.open, target)
            if exit_price is not None:
                exit_price *= 1-slippage
                cash += qty*exit_price*(1-fee)
                trades.append({"date":str(bar.day),"side":"sell","qty":qty,"price":exit_price})
                qty = 0
        curve.append(cash+qty*bar.close)
    peak = curve[0] if curve else cash
    dd = 0.0
    for value in curve:
        peak = max(peak,value)
        dd = max(dd,1-value/peak)
    return {"ending_equity":curve[-1] if curve else cash,"max_drawdown":dd,"open_qty":qty,"trades":trades}
