# Python 이미지 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 정적 파일 모으기
RUN python manage.py collectstatic --noinput

# Gunicorn 실행
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
