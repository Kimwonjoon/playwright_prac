from playwright.sync_api import sync_playwright

def test_velog_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # UI 없이 실행
        page = browser.new_page()
        
        page.goto("https://velog.io/@kimpass189/Playwright-%EA%B8%B0%EC%88%A0%EC%A1%B0%EC%82%AC2-python")

        print(page.title())

        page.screenshot(path="./tests/scre/pytest_velog1.png")

        browser.close()