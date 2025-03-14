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

SELECT ename, sal, sal