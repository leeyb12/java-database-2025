# java-database-2025
Java 개발자 과정 Database 리포지토리 

## 1일차 
- Github Desktop 설치
    - https://desktop.github.com/download/ 다운로드 
    - 기존 Github계정으로 SigIn with Browser
    - Git명령어 없이 사용가능
- Database(DB) 개요
    - 데이터를 저장하는 장소, 서비스를 하는 서버
    - 데이터베이스를 관리하는 프로그램 DBMS(DataBase Management Software)
    - 가장 유명한 것이 Oracle
    - 사용자는 SQL로 요청, DB서버는 처리결과를 테이블로 리턴
    - SQL을 배우는 것이 목적
- Oracle 설치(Docker)
    1. Powershell 오픈
    2. docker search로 내려받고 있는 확인하기기
    3. docker pull 내려받기
        ```shell 
        docker pull oracleinanutshell/oracle-xe-11g
        ```
    4. 다운로드 이미지 확인
        ```shell
        PS C:\User\Admin> docker image ls
        REPOSITORY              TAG       IMAGE ID       CREATED        SIZE
        
        ```
    5. 도커 컨테이버 실행
        ```shell
        > docker run --name oracle11g -d -p 1521:1521 --restart=always oracleinanutshell/oracle-xe-11g
        ```
        - 1521 - 오라클 기본포트
        - 아이디 system / oracle
    6. 도커 실행확인
        - Docker Desktop > Containers 확인
    7. Powershell 오픈
        ```shall
        > docker exec -it oracle19c bash
        [oracle@... ~]$ sqlplus / as sysdba
        SQL > 
        ```
    8. DBeaver 접속
        - Connection > Select your DB > Oracle 선택

        <img src="./image/db001.png" width="650">

- DBeaver 툴 설치
    - https://dbeaver.io/download/
- DML, DDL, DCL
    - 언어의 특징을 가지고 있음
        - 프로그래밍언어와 차이 - 어떻게(How) 
        - SQL - 무엇(What)
    - SQL의 구성요소 3가지
        - DDL(Data Definition Lang) - 데이터베이스 생성, 테이블 생성, 객체 생성, 수정, 삭제
            - CREATE, ALTER, DROP ...
        - DCL(Data Control Lang) - 사용자 권한 부여, 해제, 트랜잭션 시작, 종료
            - GRANT, REVOKE, BEGIN TRANS, COMMIT, ROLLBACK
        - **DML**(Data Manupulation Lang) - 데이터 조작언어(핵심!), 데이터 삽입, 조회, 수정, 삭제
            - 'INSERT', 'SELECT', 'UPDATE', 'DELETE'
- SELECT 기본
    - 데이터 조회 시 사용하는 기본명령어
        ```sql
        -- 기본 주석(한줄)
        /* 여러줄 주석
           여러줄로 주석 작성가능 */
        SELECT [ALL|DISTINCT] [*|컬럼명(들)]
          FROM 테이블명(들)
         [WHERE 검색조건(들)]  
         [GROUP BY 속성명(들)]
        [HAVING 집계함수조건(들)]
         [ORDER BY 정렬속성(들) ASC|DESC]
          [WITH ROLLUP]
        ```
    - 기본 쿼리 학습 : [SQL](./Day01/sql01_select기본.sql)
        1. 기본 SELECT
        2. WHERE 조건절
        3. NULL(!)
        4. ORDER BY 정렬
        5. 집합 

    - 함수(내장함수)
        - 문자함수 : [SQL](./Day01/sql02_함수.sql)
        - 숫자함수

## 2일차
- 함수(계속)
    - 문자함수 부터: [SQL](./Day02/sql01_함수계속.sql)
    - 숫자함수
    - 날짜함수
    - 형변환함수
- 복수행함수: [SQL](./Day02/sql02_복수행함수.sql)
    - 집계함수
    - GROUP BY
    - HAVING
    - ROLLUP
    - RANK, DENSE_RANK, ROW_NUMBER 

- 데이터베이스 타입형
    - **CHAR(n)** - 고정형 문자열, 최대 2000바이트
        - CHAR(20)으로 'Hello World'를 입력하면, 'Hello World        '로 저장!(공백포함됨)
        - 기준코드나 반드시 자리수를 지켜야하는 데이터 필요
    - **VARCHAR2(n)** - 가변형 문자열, 최대 4000바이트
        - VARCHAR2(20)로 'Hello World'를 저장하면, 'Hello World'로 저장!
    - INTEGER - 모든 데이터의 기준. 4byte, 정수를 담는 데이터형 
    - FLOAT(p) - 실수형 타입, 최대 22byte
    - NUMBER(p, s) - 숫자값, p 전체자리수, s 소수점길이. 최대 22byte
    - **DATE** - 날짜타입
    - **LONG(n)** - 가변길이문자열, 최대 2G바이트
    - LONG RAW(n) - 원시이진 데이터, 최대 2G바이트
    - CLOB - 대용량 텍스트 데이터타입, 최대 4G
    - BLOB - 대용량 바이너리 데이터타입, 최대 4G
    - BFILE - 외부파일에 저장된 데이터, 4G

## 3일차
- JOIN: [SQL](./Day03/sql03_조인기본.sql)
    - ERD(Entity Relationship Diagram) - 개체 관계 다이어그램
        - PK(Primary Key) - 기본키. 중복이안되고 빠진데이터가 하나도 없다. UNIQUE, NOT NULL 
        - FK(Foreign Key) - 외래키. 다른엔티티(테이블)의 PK. 두 엔티티의 관계를 연결해주는 값. 
        - Relationship - 부모 엔티티와 자식 엔티티간의 연관, 부모 1, 자식N을 가질 수 있음 
    - 카티션곱
        - 두 개 이상의 테이블의 조건과 관계없이 연결할 수 있는 경우의 수 모두 만든 데이터
        - 조인이전에 데이터 확인 - 실무에서 카티션곱으로 데이터를 사용할 일이 절대! 없음
    - 내부조인
        - 다중 테이블에서 보통 PK와 FK간의 일치하는 데이터를 한꺼번에 출력하기 위한 방법
        - 관계형 데이터베이스에서 필수로 사용해야 함
        - INNER JOIN 또는 오라클 간결문법 사용
    - 외부조인
        - PK와 FK간 일치하지 않는 데이터도 출력하고자 할때 사용하는 방법
        - LEFT OUTER JOIN, RIGHT OUTER JOIN 또는 오라클 간결문법 사용
- DDL 
    - CREATE - TABLE, PROCEDURE, FUNCTION, 개체를 생성하는 키워드
        - 타입형
        ```sql
        CREATE TABLE 테이블명(
            첫번째_컬럼  타입형 제약조건,
            두번째_컬럼  타입형 제약조건,
            ...
            마지막_컬럼  타입형 제약조건
            [,
            기본키, 외래키 등의 옵션...
            ]
        );
        ```
    - ALTER - 개체 중 테이블에서 수정이 필요할 때 사용하는 키워드
        ```sql
        ALTER TABLE 테이블명 ADD (컬럼명 타입형 제약조건);
        ALTER TABLE 테이블명 MODIFY (컬럼명 타입형 제약조건);
        ```
    - DROP - 개체 삭제시 사용하는 키워드
        ```sql
        DROP TABLE 테이블명 purge; -- purge - 휴지통
        ```
    - TRUNCATE - 테이블 완전 초기화 키워드
        ```sql
        TRUNCATE TABLE 테이블명;
        ```
## 4일차
- VS Code DB플러그인
    - 확장 > Database 검색 > Database Client(Weijan Chen) > 확장중 Database 선택

    <img src= "./image/db002.png" width="700">
- DML
    - INSERT - 테이블에 새로운 데이터를 삽입하는 명령
        - 한 건씩 삽입
        ```sql
        INSERT INTO 테이블명 [(컬럼리스트)]
        VALUE (값리스트);
        ```
        - 여러건 한꺼번에 삽입
    - UPDATE
    - DELETE - 데이터 삭제. WHERE 조건 없이 실행하면 테이블 모든 데이터가 삭제됨(주의요망!)
        ```sql
        DELETE FROM 테이블명
        [WHERE 조건];
        ```
- 제약조건
- INDEX
- VIEW
- 서브쿼리
- 시퀀스
