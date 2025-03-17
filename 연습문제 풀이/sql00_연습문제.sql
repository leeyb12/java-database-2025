-- p.39 ~ 40 : 
-- 1. Student 테이블에서 모든 학생의 이름과 ID, 체중을 아래 화면과 같이 출력하세요. 컬럼 이름은 "ID AND WEIGHT"로 나오게 하세요.  
SELECT name ||' ''s ID: ' || ID || ', WEIGHT is ' || WEIGHT || 'Kg' "ID AND WEIGHT"  
  FROM student; 

-- 2. emp테이블을 조회하여 모든 사람의 이름과 직업을 아래와 같이 출력하세요.
SELECT ename || '('||job||') , '||ename||''''||job||'''' "NAME AND JOB"
  FROM emp;

-- 3. emp테이블을 조회하여 모든 사원의 이름과 급여를 아래와 같은 형태로 출력하세요.
SELECT ename || ' ''s sal is $' || sal  "NAME AND Sal" 
  FROM emp;


-- p. 79 
-- SUBSTR/INSTR 퀴즈
-- Student 테이블을 참조하여 아래 화면과 같이 1전공이(deptno1 컬럼) 201번인 학생의 이름과 전화번호와 지역번호을 출력하세요. 단, 지역번호는 숫자만 나와야 합니다. 
SELECT name, tel, substr(tel, '1') "AREA CODE" 
  FROM student
 WHERE deptno1 = 201;

SELECT * 
  FROM student;

--p.81
-- LPAD 퀴즈
-- emp 테이블을 사용하여 아래 화면과 같이 deptno가 10번인 사원들의 사원이름을 총 9바이트로 출력하되 빈자리에는 해당 자리의 숫자로 채우세요.
SELECT LPAD(ename, 9, substr('123456789', LENGTH(ename)+1, 9)) "LPAD" 
  FROM emp
 WHERE deptno = '10'; 

-- p.82
-- RPAD 퀴즈 
-- 아래 화면과 같이 emp 테이블에서 deptno가 10번인 사원들의 사원이름을 총 9자리로 출력하되 오른쪽 빈자리에는 해당 자릿수에 해당되는 숫자가 출력되도록 하세요.
SELECT RPAD
  FROM emp;