"""Read-only, self-contained HTML report from persisted paper accounts."""
import html
import json
from pathlib import Path


def render_dashboard(state, status, next_run):
    state = Path(state)
    esc = lambda value: html.escape(str(value))
    def table(headers, rows):
        if not rows:
            return '<div class="empty">아직 기록이 없습니다. 다음 새 완료 봉을 기다립니다.</div>'
        return '<div class="scroll"><table><thead><tr>' + ''.join('<th>'+esc(h)+'</th>' for h in headers) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td>'+esc(v)+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'
    accounts, orders, comparisons, health = [], [], [], []
    details = []
    count = 0
    for symbol, info in status.get('symbols', {}).items():
        health.append([symbol, info.get('health', {}).get('market', '확인 필요'), info.get('health', {}).get('data', info.get('status', '-')), info.get('last_success_utc') or '없음', info.get('last_completed_bar_start_utc', '-'), info.get('message', info.get('detail', '-'))])
        path = state / symbol / 'accounts-v2.json'
        if path.exists():
            for strategy, account in json.loads(path.read_text(encoding='utf-8')).items():
                count += 1
                events = account.get('events', [])
                risk = account.get('risk', {})
                points = [{'time': e['bar'], 'equity': e['equity']} for e in events if 'equity' in e]
                details.append(dict(symbol=symbol, strategy=strategy, equity=account['equity'], cash=account['cash'], qty=account['qty'], initial=account.get('initial',10000), points=points, events=events[-200:], halted=risk.get('halted',False), reason=risk.get('reason','')))

                reason = ('중단: '+risk.get('reason', '')) if risk.get('halted') else events[-1].get('reason', '새 완료 봉·매매 신호 대기') if events else '계좌 준비 완료 · 다음 새 완료 봉 대기'
                accounts.append([symbol, strategy, f"${account['equity']:,.2f}", f"${account['equity']-account.get('initial',10000):+,.2f}", f"${account['cash']:,.2f}", f"{account['qty']:.4f}", reason])
                for event in events:
                    if event.get('side') == 'hold':
                        continue
                    orders.append([event.get('bar','-'), symbol, strategy, {'buy':'매수','sell':'매도'}.get(event.get('side'),event.get('side')), event.get('status','-'), f"{event.get('quantity',0):.4f}", f"{event.get('remaining',0):.4f}", f"${event.get('price',0):.2f}", f"${event.get('fee',0):.2f}", event.get('reason','-')])
        path = state / symbol / 'comparison.json'
        if path.exists():
            for strategy, folds in json.loads(path.read_text(encoding='utf-8')).get('results', {}).items():
                row = folds['holdout']
                comparisons.append([symbol, strategy, row['start'][:10]+' ~ '+row['end'][:10], *[f"{row[key]['return_']:.2%}" for key in ('strategy_gross','strategy_net','buy_hold_net','matched_buy_hold_net')], f"{row['strategy_net']['average_exposure']:.1%}", f"{row['strategy_net']['max_drawdown']:.2%}"])
    orders.sort(key=lambda row: row[0], reverse=True)
    stopped = status.get('emergency_stop', False)
    failures = sum(info.get('status') == 'error' for info in status.get('symbols', {}).values())
    title = '비상 중단 활성' if stopped else '데이터 확인 필요' if failures else '모의 운영 기록'
    data_json = json.dumps(details, ensure_ascii=False).replace('<', '\\u003c')
    body = f'''<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>투자랩 · 운영 대시보드</title>
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#f4f7fb;color:#18243b;font:15px system-ui,'Malgun Gothic',sans-serif}}header{{background:#13223c;color:white;padding:26px 5vw}}header span{{color:#96abc9}}main{{max-width:1440px;margin:auto;padding:28px 4vw}}h1{{font-size:28px;margin:0 0 8px}}h2{{font-size:20px}}.tag{{display:inline-block;background:#e1edf9;color:#285c90;padding:6px 12px;border-radius:20px}}.cards{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:22px 0}}.card,section{{background:white;border:1px solid #e2e8f1;border-radius:14px;padding:22px}}.card strong{{display:block;font-size:24px;margin-top:12px}}.muted{{color:#64748b;font-size:13px;line-height:1.7}}nav{{display:flex;gap:8px;margin:22px 0;flex-wrap:wrap}}button,input{{font:inherit;border:1px solid #d7dfeb;border-radius:8px;background:white;padding:11px 16px}}button{{cursor:pointer}}button[aria-selected=true]{{background:#2862dd;color:white;border-color:#2862dd}}input{{width:100%;margin:0 0 18px}}section[hidden]{{display:none}}.scroll{{overflow:auto}}table{{border-collapse:collapse;width:100%;font-size:13px}}th{{text-align:left;background:#f4f7fb;color:#596a82;white-space:nowrap}}td,th{{padding:13px 12px;border-bottom:1px solid #edf1f6}}td{{max-width:330px;min-width:90px}}.empty{{padding:45px;text-align:center;color:#718096}}.notice{{border-left:3px solid #2862dd;padding:12px 16px;background:#edf4ff;line-height:1.7}}@media(max-width:800px){{.cards{{grid-template-columns:repeat(2,1fr)}}main{{padding:20px}}header{{padding:24px}}}}
svg{{width:100%;height:auto;background:#f7faff;border-radius:12px}}select{{padding:10px;border:1px solid #d7dfeb;border-radius:8px;font:inherit}}#overview tbody tr{{cursor:pointer}}#overview tbody tr:hover{{background:#edf4ff}}
</style><header><h1>투자랩 <span> / Paper Research</span></h1><div>미국 ETF · 15분봉 · 실제 계좌 주문 없음</div></header><main>
<div class="tag">{esc(title)}</div><div class="cards"><div class="card">v2 가상 계좌<strong>{count}개</strong></div><div class="card">누적 매매 판단 기록<strong>{len(orders)}건</strong></div><div class="card">수집 오류 종목<strong>{failures}개</strong></div><div class="card">보호 기준<strong>3% / 10%</strong><span class="muted">일중 손실 / 최고 평가액 낙폭</span></div></div>
<p class="muted">최근 확인 {esc(status.get('checked_utc','없음'))} UTC<br>다음 예약 요청 {esc(next_run)} UTC · 실행 지연 가능 · 이 파일은 생성 시점의 기록입니다.</p>
<nav role="tablist"><button role="tab" aria-selected="true" data-tab="overview">운영 요약</button><button role="tab" aria-selected="false" data-tab="comparison">전략 비교</button><button role="tab" aria-selected="false" data-tab="orders">주문 기록</button><button role="tab" aria-selected="false" data-tab="health">운영 관리</button></nav>
<section id="overview"><h2>계좌별 자산과 매매 이유</h2><p class="notice">각 계좌는 별도 전략 실험입니다. 평가액을 합쳐 하나의 포트폴리오로 해석하지 마세요. 새 봉이나 신호가 없으면 대기합니다.</p>{table(['종목','전략','평가액','손익','현금','보유 수량','최근 판단·대기 이유'],accounts)}</section>
<section id="detail" hidden><h2 id="detail-title">계좌 상세</h2><div id="detail-metrics" class="cards"></div><label>차트 기간 <select id="range"><option value="all">전체 기록</option><option value="30">최근 30일</option><option value="7">최근 7일</option></select></label><h2>자산 곡선 · USD</h2><div id="equity-chart"></div><h2>최고 평가액 대비 낙폭 · %</h2><div id="drawdown-chart"></div><p class="muted">저장된 평가액 기록만 표시합니다. 낙폭은 전체 저장 기록의 최고 평가액을 기준으로 계산합니다. 이전 버전에서 저장되지 않은 평가액은 복원하지 않습니다.</p><h2>최근 판단·체결 기록 (최대 200건)</h2><div id="detail-events" class="scroll"></div></section>
<section id="comparison" hidden><h2>같은 기간의 공정 비교</h2><p class="muted">보류 구간의 사후 연구 결과입니다. 평균 노출 맞춤은 설명용이며 v2 계좌 수익률과 다릅니다. 서로 다른 종목·평가 기간의 순위를 자동 선정하지 않습니다.</p>{table(['종목','전략','평가 기간','비용 전','비용 후','100% 보유','같은 노출 보유','평균 노출','전략 낙폭'],comparisons)}</section>
<section id="orders" hidden><h2>가상 체결 기록</h2><input id="filter" aria-label="주문 기록 검색" placeholder="종목, 전략, 상태 또는 매매 이유 검색"><p class="muted">다음 봉 시가에 비용·스프레드·거래량 제한을 적용한 가상 체결. 잔량은 만료됩니다. 체결 시각과 기록 시각은 다를 수 있습니다.</p>{table(['봉 시각 UTC','종목','전략','매매','체결 상태','체결 수량','만료 잔량','가격','비용','판단 이유'],orders)}</section>
<section id="health" hidden><h2>수집과 운영 상태</h2>{table(['종목','시장','데이터','최근 성공 UTC','마지막 완료 봉 UTC','상세'],health)}<p class="notice">비상 중단: {'활성 · 신규 매매 차단' if stopped else '비활성'}<br>중단 시 보유분을 자동 매도하지 않습니다. 서버 중단은 GitHub Actions의 emergency_stop으로 실행하세요. 이 보고서는 읽기 전용입니다.</p><a href="https://github.com/BaekJaeYeol/paper-trading-program/actions/workflows/investment-intraday.yml">서버 실행·중단 관리 열기</a></section>
</main><script>
document.querySelectorAll('[data-tab]').forEach(button=>button.addEventListener('click',()=>{{document.querySelectorAll('section').forEach(section=>section.hidden=section.id!==button.dataset.tab);document.querySelectorAll('[data-tab]').forEach(tab=>tab.setAttribute('aria-selected',String(tab===button)));}}));
document.querySelector('#filter').addEventListener('input',event=>{{const query=event.target.value.toLowerCase();document.querySelectorAll('#orders tbody tr').forEach(row=>row.hidden=!row.textContent.toLowerCase().includes(query));}});

const accountDetails={data_json};
let selectedAccount=null;
const safeText=value=>String(value??'—');
function chart(target,points,values,color){{
 const host=document.getElementById(target);host.replaceChildren();
 if(points.length<2){{host.textContent='평가액 기록이 2개 이상 쌓이면 차트가 표시됩니다.';return;}}
 const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox','0 0 900 240');svg.setAttribute('role','img');svg.setAttribute('aria-label',target==='equity-chart'?'계좌 자산 곡선':'계좌 낙폭');
 const min=Math.min(...values),max=Math.max(...values),span=max-min||1;
 const start=Date.parse(points[0].time),end=Date.parse(points.at(-1).time);
 const line=document.createElementNS(ns,'polyline');line.setAttribute('points',values.map((v,i)=>`${{55+(Date.parse(points[i].time)-start)/(end-start||1)*800}},${{190-(v-min)/span*150}}`).join(' '));line.setAttribute('fill','none');line.setAttribute('stroke',color);line.setAttribute('stroke-width','3');svg.append(line);
 [[55,25,max.toFixed(2)],[55,215,min.toFixed(2)],[150,235,points[0].time.slice(0,10)],[700,235,points.at(-1).time.slice(0,10)]].forEach(([x,y,label])=>{{const text=document.createElementNS(ns,'text');text.setAttribute('x',x);text.setAttribute('y',y);text.setAttribute('font-size','12');text.textContent=label;svg.append(text);}});host.append(svg);
}}
function showAccount(index){{
 selectedAccount=index;const a=accountDetails[index];document.querySelectorAll('section').forEach(s=>s.hidden=s.id!=='detail');document.querySelectorAll('[data-tab]').forEach(t=>t.setAttribute('aria-selected','false'));
 document.getElementById('detail-title').textContent=a.symbol+' · '+a.strategy;
 const metrics=document.getElementById('detail-metrics');metrics.replaceChildren();[['평가액','$'+a.equity.toFixed(2)],['손익','$'+(a.equity-a.initial).toFixed(2)],['현금','$'+a.cash.toFixed(2)],['보유 수량',a.qty.toFixed(4)]].forEach(([label,value])=>{{const card=document.createElement('div');card.className='card';card.textContent=label;const strong=document.createElement('strong');strong.textContent=value;card.append(strong);metrics.append(card);}});
 let peak=a.initial;const all=a.points.map(p=>{{peak=Math.max(peak,p.equity);return {{...p,drawdown:(p.equity/peak-1)*100}};}});const days=document.getElementById('range').value;const cutoff=all.length&&days!=='all'?Date.parse(all.at(-1).time)-Number(days)*86400000:-Infinity;const points=all.filter(p=>Date.parse(p.time)>=cutoff);
 chart('equity-chart',points,points.map(p=>p.equity),'#2862dd');chart('drawdown-chart',points,points.map(p=>p.drawdown),'#e16b60');
 const host=document.getElementById('detail-events');host.replaceChildren();const table=document.createElement('table');const head=document.createElement('tr');['봉 UTC','判断','상태','수량','판단 이유'].forEach(label=>{{const th=document.createElement('th');th.textContent=label==='判断'?'매매':label;head.append(th);}});table.append(head);a.events.slice().reverse().forEach(e=>{{const row=document.createElement('tr');[e.bar,e.side,e.status,e.quantity,e.reason].forEach(v=>{{const cell=document.createElement('td');cell.textContent=safeText(v);row.append(cell);}});table.append(row);}});host.append(table);if(!a.events.length){{const p=document.createElement('p');p.textContent='다음 새 완료 봉·신호 대기';host.append(p);}}
}}
document.querySelectorAll('#overview tbody tr').forEach((row,index)=>{{row.tabIndex=0;row.setAttribute('aria-label',accountDetails[index].symbol+' '+accountDetails[index].strategy+' 상세 보기');row.addEventListener('click',()=>showAccount(index));row.addEventListener('keydown',e=>{{if(e.key==='Enter'||e.key===' '){{e.preventDefault();showAccount(index);}}}});}});
document.getElementById('range').addEventListener('change',()=>{{if(selectedAccount!==null)showAccount(selectedAccount);}});

</script></html>'''
    (state / 'dashboard.html').write_text(body, encoding='utf-8')
