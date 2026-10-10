"""Chronological multi-asset experiments and isolated forward accounts."""
import hashlib
import json
from pathlib import Path
from engine import load, evaluate
from research import candidates
from paper import Paper


def walk_forward(rows, cost=.002, train=252, test=63):
    if train < 126 or test < 21 or len(rows) < 61 + train + test:
        raise ValueError('반복 검증에는 최소 376일 데이터가 필요합니다')
    if not 0 <= cost < .1:
        raise ValueError('거래 비용 범위를 확인하세요')
    ss = candidates(rows)
    results = []
    for lo in range(61 + train, len(rows) - test + 1, test):
        # Selection sees only the preceding window; test windows never overlap.
        scores = {name: evaluate(rows, sig, lo-train, lo, cost)
                  for name, sig in ss.items()}
        eligible = [name for name, m in scores.items()
                    if name not in ('cash', 'buy_hold') and m['turnover'] >= 4]
        selected = max(eligible, key=lambda name: scores[name]['sharpe_rf0']) if eligible else 'cash'
        prior_return = rows[lo-1][4]/rows[lo-61][4]-1
        regime = '상승' if prior_return > .05 else '하락' if prior_return < -.05 else '횡보'
        baseline = evaluate(rows, ss['buy_hold'], lo, lo+test, cost)['return']
        for name, sig in ss.items():
            metrics = evaluate(rows, sig, lo, lo+test, cost)
            results.append(dict(strategy=name, selected=name == selected,
                                regime_at_start=regime, train_start=rows[lo-train][0], train_end=rows[lo-1][0],
                                test_start=rows[lo][0], test_end=rows[lo+test-1][0],
                                excess_return=metrics['return']-baseline, **metrics))
    return results


def batch_validate(inputs, outdir, source):
    records = []
    errors = {}
    for symbol, path in inputs.items():
        try:
            rows = load(path)
            digest = hashlib.sha256(Path(path).read_bytes()).hexdigest()
            for result in walk_forward(rows):
                records.append(dict(symbol=symbol, data_sha256=digest, **result))
        except (ValueError, OSError) as exc:
            errors[symbol] = str(exc)
    report = dict(source=source, results=records, errors=errors, live_ready=False,
                  selection='preceding 252 days only; nonoverlapping 63-day tests; fixed candidates',
                  limitations=['Separate flat-start experiments, not a combined portfolio',
                               'Correlated symbols and windows are not independent samples',
                               'Repeated inspection is exploratory, not a fresh final holdout'])
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir/'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    return report


class Fleet:
    """One database per fixed strategy. No shared capital or initial quote fills."""
    def __init__(self, directory):
        self.directory = Path(directory)

    def update(self, symbol, rows):
        result = {}
        for name in candidates(rows):
            key = hashlib.sha256(name.encode()).hexdigest()[:16]
            account = Paper(self.directory/symbol/(key+'.sqlite'))
            snapshot = account.snapshot()
            if not snapshot['active']:
                snapshot = account.start(rows, name, 'real_download')
            else:
                snapshot = account.advance(rows)
            result[name] = snapshot
        return result
