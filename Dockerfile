# 베이스 이미지 설정
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . .

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 애플리케이션 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]

