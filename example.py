from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

# Mock
def route_ex(route, request):
    if "api.example.com/data" in request.url:
        # 요청에 대한 임의의 응답
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"data": "mocked response"}',
        )
    else:
        route.continue_()

with sync_playwright() as p:
    # 브라우저 GUI 모드로 실행
    browser = p.chromium.launch(headless=False)

    # 새 페이지 생성
    page = browser.new_page()

    # 요청 가로채기 설정
    page.route("**/api.example.com/data", route_ex)

    # URL로 이동
    page.goto("https://example.com")

    # JS 코드 사용 시 evaluate 사용
    page.evaluate("fetch('https://api.example.com/data').then(res => res.json()).then(console.log)")

    # 페이지 title 값 출력
    print(page.title())

    # 현 페이지 스크린샷 저장
    page.screenshot(path="<파일저장경로>")

    # 클릭, 채우기
    page.click("input[name="username"]") # CSS 선택자
    page.fill("#id", "test_user") # ID 기반 선택자
    page.click("text="Submit"") # 텍스트 기반 선택자

    # 테스트 기대값 검증 expect
    # 반환값 : AssertionError
    expect(page).to_have_url('https://example.com/dashboard')
    expect(page.locator('h1')).to_have_text('대시보드')

    browser.close()