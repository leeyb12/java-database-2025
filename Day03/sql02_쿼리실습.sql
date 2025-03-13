-- 
-- 1. 모든 컬럼 조회하기

SELECT * FROM emp ; 

SELECT * 
  FROM emp ;

SELECT * fr  -- FROM 키워드 줄을 바꿔서 에러 남!
  om emp;

SELECT *   -- 테이블 이름 줄을 바꿔서 에러 남!  
  FROM em 
  p;

SELECT em   -- 컬럼 이름 줄을 바꿔서 에러 남!
  pno FROM emp;

SELECT * FROM tab ;

-- 2. 원하는 컬럼만 조회하기 

SELECT empno , ename 
  FROM emp;

SET PAGESIZE 15
SET LINESIZE 200

SELECT empno , ename 
  FROM emp;

COL deptno FOR 9999
COL dname FOR a15
COL loc FOR a15

SELECT deptno, dname, loc 
  FROM dept;

-- 3.SELECT 명령에 표현식을 사용하여 출력하기

SET PAGESIZE 50 
COL name FOR a20

SELECT name, 'good morning~~!' "Good Morning"
  FROM professor;

SELECT dname, ',it''s deptno: ', deptno "DNAME AND DEPTINO"
  FROM dept;

SELECT dname, q'[,it's deptno : ]', deptno "DNAME AND DEPTINO"
  FROM dept;

-- 4. 컬럼 별칭 사용하여 출력하기 

SELECT profno, name, pay 
  FROM professor;

SELECT profno "Prof's NO", name AS "Prof's NAME", pay Prof_Pay
  FROM professor;

-- 5. DISTNICT 명령어 - 중복된 값을 제거하고 출력하기

SELECT deptno FROM emp;  

SELECT DISTINCT deptno 
  FROM emp;

SELECT job, ename 
  FROM emp
  ORDER BY 1, 2;

SELECT DISTINCT job, ename
  FROM emp
  ORDER BY 1, 2;

SELECT job, DISTINCT ename
  FROM emp
  ORDER BY 1, 2;

-- 6. 연결 연산자로 컬럼을 붙여서 출력하기 

SELECT ename, job FROM emp;

SELECT ename || job FROM emp;

SELECT ename || '-' || job FROM emp;

SELECT ename||'''s job is '||  job "NAME AND JOB"
  FROM emp;

-- 연습문제
-- student 테이블에서 모든 학생의 이름과 ID, 체중을 아래 화면과 같이 출력하세요. 컬럼 이름은 "ID AND WEIGHT"로 나오게 하세요.
SELECT *
  FROM student;

SELECT name ||'''s ID: '|| ID || ,IS ''kg || WEIGHT  "ID AND WEIGHT"
  FROM student;