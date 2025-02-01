FROM mcr.microsoft.com/playwright/python:v1.49.1-jammy

# 작업 디렉토리 설정
WORKDIR /app

# 로컬 파일 전부 복사
COPY . .

# 필요한 Python 패키지 설치
RUN pip install -r requirements.txt

# playwright에 브라우저는 포함되어있기 때문에 install 필요없음
# RUN python -m playwright install

# 필요한 의존성 설치 (X 서버 관련)
# headless mode 관련 xvfb 사용하지 않으면 headless 사용 불가능능
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libasound2 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    x11-utils \
    dbus-x11 \
    xvfb

# 기본 명령어(스크립트 실행 등)
# CMD ["python", "test1.py"]
# headless 사용을 위한 실행 방법
# CMD xvfb-run -a python test1.py
CMD ["pytest", "-v", "-n", "4"]