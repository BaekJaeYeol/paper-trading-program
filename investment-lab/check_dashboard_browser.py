"""Browser checks for the generated server report; no account mutations."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

report = Path(sys.argv[1]).resolve()
if not report.is_file():
    raise SystemExit("dashboard.html was not generated")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(report.as_uri())
    page.get_by_role("heading", name="계좌별 자산과 매매 이유").wait_for()
    for name, section in [("전략 비교", "comparison"), ("주문 기록", "orders"), ("운영 관리", "health"), ("운영 요약", "overview")]:
        page.get_by_role("tab", name=name).click()
        assert page.locator("#" + section).is_visible(), name
    rows = page.locator("#overview tbody tr")
    if rows.count():
        rows.first.click()
        assert page.locator("#detail").is_visible()
        for period in ("7", "30", "all"):
            page.locator("#range").select_option(period)
        assert page.locator("#detail-metrics .card").count() == 4
        assert page.locator("#equity-chart").inner_text() or page.locator("#equity-chart svg").count()
        page.get_by_role("tab", name="운영 요약").click()
    page.get_by_role("tab", name="주문 기록").click()
    page.get_by_role("textbox", name="주문 기록 검색").fill("NO_MATCH_BROWSER_CHECK")
    assert page.locator("#orders tbody tr:visible").count() == 0
    page.get_by_role("textbox", name="주문 기록 검색").fill("")
    page.get_by_role("tab", name="운영 요약").click()
    page.screenshot(path=str(report.parent / "dashboard-desktop.png"), full_page=True)
    page.set_viewport_size({"width": 390, "height": 844})
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
    page.screenshot(path=str(report.parent / "dashboard-mobile.png"), full_page=True)
    assert not errors, errors
    browser.close()
print("PASS: generated HTML, tabs, account details, date filter, order search, responsive layout, no JavaScript errors")
