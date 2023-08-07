# 1. 소스 구조
```treebash
api_server/ : 패키지/모듈 root. 실행도 이위치에서 해야함
│
├── model/ : API로 주고받을 데이터 model 정의. 원래는 router/xxx.py에 함께 넣으려 했으나 repository/yyy.py를 서로 호출하는 구조라서(썩 좋은 구조는 아님. 예제용..) 상호참조 문제로 외부로 빼냄.
│   ├── user_model.py : user 등록/조회 관련 API 입력 param 및 응답 데이터에 대한 model.
│   └── ...
│
├── repository/ : 데이터소스(여기서는 mysql db) CRUD 관련 로직 및 데이터 model 정의.
│   ├── user_repo.py : users 테이블에 대한 CRUD 처리 코드.
│   └── ...
│
├── resource/ : API server 동작에 필요한 각종 시스템 리소스(database 접속 등).
│   ├── database.py : DB 접속 및 session 연결 관련 코드.
│   └── ...
│
├── router/ : API endpoint별 처리 로직.
│   ├── user.py : user 등록, 조회 관련 API 경로 및 대응되는 endpoint 로직 구현.
│   └── ...
│
├── Dockerfile : API server를 docker로 만들때 정의 파일.
├── main.py : API server를 실행할 main 파일.
├── requirements.txt : 필요한 파이썬 패키지 정의 파일.
└── schema.sql : mysql database table 정의 파일.
```

# 2. 실행
## 2.1. 환경 설정
### 파이썬 가상환경 설정 및 모듈 설치
* anaconda or pyenv로 python 3.11.x 버전의 가상환경 설정(이하 가상환경 이름은 example로 간주한다)하고 활성화

#### Anaconda로 설치
* 아래 내용은 대충 적은거라 정확히 해보고 수정 필요
```bash
$ conda create -n example python=3.11.2
$ conda activate example

# mysql client 설치 필요
$ pip install -r requirements.txt
```

#### pyenv로 설치

```bash
$ pyenv install 3.11.2
$ pyenv virtualenv 3.11.2 example
$ pyenv activate example

# mysql client 설치 필요
(example) $ pip install -r requirements.txt
```

## 2.2. Database 준비

### Database 설치
* https://github.com/luxsolist/examples/blob/main/database/mysql/README.md 참조

### 테이블 생성
* mysql에 접속하여 schema.sql 파일의 내용(DDL 구문) 실행

## 2.3. API server 구동

### 로컬에서 실행

```bash
$ uvicorn main:app --host=0.0.0.0 --port=8080 --reload
```

### Docker로 실행
* 단, 이 경우 mysql이 local PC에 docker로 함께 떠있는 경우 api_server docker에서 mysql docker로 네트워크 연결이 안될 수 있다. docker compose 등에서 별도 네트워크 설정을 하거나 mysql을 외부의 다른 서버에서 띄우고 resource/database.py 파일에 있는 DATABASE_URL의 db 접속 주소를 그에 맞게 변경해줘야한다.
```bash
$ docker build -t api_server ./
$ docker run -d -p 8080:8080 api_server
```
