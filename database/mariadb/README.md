# Docker를 이용한 MariaDB 설치 및 실행 방법
## Docker 설치


## MariaDB docker 실행

```bash
$ docker pull mariadb:latest
$ docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD={루트유저패스워드} -v /{로컬파일저장경로}:/var/lib/mysql --name {도커컨테이너이름} mariadb
```

## Database 초기 설정
```bash
# 실행중인 mariadb docker container에 접속
$ docker exec -it {도커컨테이너이름} /bin/bash 

# mariadb 접속
(도커) $ mariadb -u root -p --port 3306 --host 127.0.0.1
Enter password: {루트유저패스워드}

# 데이터베이스 생성
MariaDB [(none)]> create database {데이터베이스이름};

# 데이터베이스 사용자 생성
MariaDB [(none)]> create user '{유저이름}'@'%' identified by '{패스워드}';

# 생성한 유저에 생성한 데이터베이스에 대한 권한 추가
MariaDB [(none)]> grant all privileges on {데이터베이스이름}.* to '{유저이름}'@'%';

# 변경사항 적용
MariaDB [(none)]> flush privileges;

#종료
MariaDB [(none)]> exit
Bye

# docker container 접속 종료
(도커) $ exit
exit

$

```
