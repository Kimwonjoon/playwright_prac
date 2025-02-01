# playwright test
from playwright.sync_api import sync_playwright

# Playwright 시작
with sync_playwright() as p:
    # 브라우저(Chromium) 열기
    browser = p.chromium.launch(headless=False)  # headless=False는 브라우저가 눈에 보이도록 설정
    page = browser.new_page()
    
    # 웹 페이지 열기
    page.goto('https://velog.io/@kimpass189/posts')

    # 로컬 html 파일 테스트 하고 싶을때
    # file_path = os.path.abspath('/home/kimpass189/myfile.html')  # 로컬 파일의 절대 경로
    # page.goto(f'file://{file_path}')  # 로컬 HTML 파일 열기
    
    # 페이지 제목 출력
    print(page.title())
    
    # 검색창에 입력 locator("#<id값>")
    # search_box = page.locator("#APjFqb")
    # search_box.fill("카리나")

    # Enter 키 입력하여 검색 실행
    # search_box.press("Enter")

    # 결과 페이지가 로드될 때까지 대기
    # page.wait_for_load_state("networkidle")

    print("검색 완료!")

    page.screenshot(path="./screenshot/testing1.png")

    # 브라우저 닫기
    # browser.close()
