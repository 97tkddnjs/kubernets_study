FROM python:3.11-slim

WORKDIR /app

# 애플리케이션 코드 복사
COPY app/ .

# 의존성 설치
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 포트 노출
EXPOSE 8000

# 헬스체크
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]