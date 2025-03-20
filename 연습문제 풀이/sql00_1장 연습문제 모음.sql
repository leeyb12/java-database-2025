-- 1장 p.39 ~ 40 
-- 연습문제 1
-- Student 테이블에서 모든 학생의 이름과 ID, 체중을 아래 화면과 같이 출력하세요. 컬럼 이름은 "ID AND WEIGHT"로 나오게 하세요. 
SELECT * 
  FROM Student;

SELECT name ||'''s ID : '||ID||', WEIGHT is ' || WEIGHT || 'Kg' "ID AND WEIGHT"
  FROM Student;


-- 연습문제 2 
-- emp 테이블을 조회하여 모든 사람의 이름과 직업을 아래와 같이 출력하세요.
SELECT *
  FROM emp;

SELECT ename || '('||job||') , '||ename||''''||job||'''' "NAME AND JOB"
  FROM emp;


-- 연습문제 3 
-- emp 테이블을 조회하여 모든 사원의 이름과 급여를 아래와 같이 출력하세요.
SELECT ename || '''s sal is $'|| sal "NAME AND SAL"
  FROM emp;
