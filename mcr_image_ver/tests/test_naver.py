from playwright.sync_api import sync_playwright

def test_naver_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # UI 없이 실행
        page = browser.new_page()
        
        page.goto("https://www.naver.com")
        page.fill("#query", "카리나")
        page.keyboard.press("Enter")

        page.click('a[role="tab"]:has-text("이미지")')

        # 페이지 요청 대기
        page.wait_for_load_state("networkidle")

        page.screenshot(path="./tests/scre/pytest_naver1.png")

        browser.close()