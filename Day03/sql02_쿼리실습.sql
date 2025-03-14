-- 1장 SELECT 명령을 이용하여 데이터를 조회합니다


-- 1. 모든 컬럼 조회하기

SELECT * FROM emp ; 

SELECT * 
  FROM emp ;

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

-- 7. 원하는 조건만 골라내기 - WHERE 절 사용
SELECT empno, ename 
  FROM emp 
  WHERE empno=7900;

SELECT ename, sal 
  FROM emp 
  WHERE sal < 900;

SELECT empno, ename, sal
  FROM emp 
 WHERE ename='SMITH';

SELECT ename, hiredate
  FROM emp 
 WHERE ename = 'SMITH';

SELECT empno, ename, sal
  FROM emp 
 WHERE hiredate = '80/12/17';

-- 8. SQL에서 산술 연산자 사용하기
SELECT ename, sal 
  FROM emp
 WHERE deptno = 10;

SELECT ename, sal, sal+100
  FROM emp 
 WHERE deptno = 10;

SELECT ename, sal, sal*1.1
  FROM emp
 WHERE deptno = 10;

-- 9. 다양한 연산자를 활용하는 방법
-- 1) 비교 연산자 사용하기 
SELECT empno, ename, sal 
  FROM emp 
 WHERE sal >= 4000;

SELECT empno, ename, sal
  FROM emp 
 WHERE ename >= 'W';

SELECT ename, hiredate
  FROM emp;

SELECT ename, hiredate
  FROM emp 
 WHERE hiredate >= '81/12/25';

SELECT ename, hiredate 
  FROM emp;

-- 2) BETWEEN 연산자로 구간 데이터 조회하기
SELECT empno, ename, sal 
  FROM emp 
 WHERE sal >= 2000
 AND sal <= 3000;

SELECT ename FROM emp 
  ORDER BY ename;

SELECT ename FROM emp
 WHERE ename BETWEEN 'JAMES' AND 'MARTIN'
 ORDER BY ename;

-- 3) IN연산자로 여러 조건을 간편하게 검색하기
SELECT empno, ename, deptno 
  FROM emp 
 WHERE deptno IN (10, 20);

-- 4) LIKE연산자로 비슷한 것들 모두 찾기 
SELECT empno, ename, sal 
  FROM emp 
 WHERE sal LIKE '1%';

SELECT empno, ename, sal
  FROM emp 
 WHERE ename LIKE 'A%';

SELECT empno, ename, hiredate
  FROM emp 
 WHERE hiredate LIKE '80%';

-- 5) 값이 무엇인지 모를 경우 - IS NULL/IS NOT NULL 연산자 활용하기
SELECT empno, ename, comm
  FROM emp 
 WHERE deptno IN (20, 30);

SELECT empno, ename, comm 
  FROM emp 
 WHERE comm IS NULL;

SELECT empno, ename, comm 
  FROM emp 
 WHERE comm IS NOT NULL;

-- 6) 검색 조건이 두 개 이상일 경우 조회하기
SELECT ename, hiredate, sal
  FROM emp 
 WHERE hiredate >= '82-01-01'
 AND sal >= 1300;

SELECT ename, hiredate, sal
  FROM emp 
 WHERE hiredate > '82-01-01'
 OR sal >= 1300;

SELECT empno, ename, sal, comm
  FROM emp 
 WHERE sal > 1000
 AND (comm < 1000 OR comm IS NULL);

SELECT empno, ename, sal, comm
  FROM emp 
 WHERE sal > 1000
 AND comm < 1000 OR comm IS NULL;

-- 7) 사용자에게 조건을 입력받아서 조건에 맞는 값 출력하기
SET verify OFF
SELECT empno, ename, sal
  FROM emp 
 WHERE empno = &empno ; 