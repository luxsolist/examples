# 환경 설정
## 파이썬 가상환경 설정 및 모듈 설치
* anaconda or pyenv로 python 3.11.x 버전의 가상환경 설정(이하 가상환경 이름은 example로 간주한다)하고 활성화

### Anaconda로 설치

```bash
$ conda create -n example python=3.11.2
$ conda activate example
$ pip install -r requirements.txt
```

### pyenv로 설치

```bash
$ pyenv install 3.11.2
$ pyenv virtualenv 3.11.2 example
$ pyenv activate example

# mysql client 설치 필요
(example) $ pip install -r requirements.txt
```

# Database 준비

## Database 설치
* database/mysql/README.md 설치 가이드 참조

## 테이블 생성
* mysql에 접속하여 schema.sql 파일의 내용(DDL 구문) 실행

# 실행

## 로컬에서 실행

```bash
$ uvicorn main:app --host=0.0.0.0 --port=8080 --reload
```

## Docker로 실행

```bash
$ docker build -t api_server ./
$ docker run -d -p 8080:8080 api_server
```
