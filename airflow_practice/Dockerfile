FROM apache/airflow:2.10.0

USER root

# 필요한 패키지 설치
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 파일을 복사
COPY requirements.txt /

# USER airflow로 전환
USER airflow

# Python 패키지 설치
RUN pip install --no-cache-dir -r /requirements.txt