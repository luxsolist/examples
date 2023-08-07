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
* https://github.com/luxsolist/examples/blob/main/database/mysql/README.md 참조

## 테이블 생성
* mysql에 접속하여 schema.sql 파일의 내용(DDL 구문) 실행

# 실행

## 로컬에서 실행

```bash
$ uvicorn main:app --host=0.0.0.0 --port=8080 --reload
```

## Docker로 실행
* 단, 이 경우 mysql이 local PC에 docker로 함께 떠있는 경우 api_server docker에서 mysql docker로 네트워크 연결이 안될 수 있다. docker compose 등에서 별도 네트워크 설정을 하거나 mysql을 외부의 다른 서버에서 띄우거나 해야한다.
```bash
$ docker build -t api_server ./
$ docker run -d -p 8080:8080 api_server
```
