# Practice Playwright with python
![image](https://github.com/user-attachments/assets/42876d37-8ea2-46e3-823c-ed61a7ed7a97)

E2E 테스트 툴 Playwright 연습 레포입니다.

mcr_image_ver : ms 기존 playwright 이미지
py_image_ver : python 이미지로 pip install playwright

### pytest
pytest를 하고 싶은 폴더엔 __init__.py가 필요하다.
테스트 파일형식은 test_*.py or *_test.py
클래스 명칭 : class Test*
함수 명칭 : def test_*
병렬 실행 하면 __init__.py와 같이 있는 test 파일들 한번에 실행됨
안하면 한 파일씩 순차적 실행됩니다.

## usage
### build
```bash
# container 빌드
$ docker build --no-cache -t <container name>:<version> .
```

### run
```bash
# docker 실행
$ docker run --rm -v $(pwd):/app playtest:0.1.0
```

### Pytest
```bash
# 그냥 실행
$ pytest
# 자세한 테스트 로그, print 결과 확인
$ pytest -v -s
# 병렬 실행
$ pytest -n <worker 개수>
$ pytest -n auto
```