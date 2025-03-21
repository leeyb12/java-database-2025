-- 2장 
-- p.78 
-- 사용 예1
-- Student 테이블의 tel컬럼을 사용하여 1전공번호(deptno1)가 201번인 학생의 이름과 전화번호, ')'가 나오는 위치를 출력하세요.
SELECT name, tel, instr(tel,')')
  FROM student
 WHERE deptno1 = 201;


-- p.79 
-- 사용 예2
-- Student 테이블에서 1전공이 101번인 학생들의 tel 컬럼을 조회하여 3이 첫 번째로 나오는 위치를 이름과 전화번호와 함께 출력하세요.
SELECT name, tel, instr(tel,'3')
  FROM student
 WHERE deptno1 = 101;

-- SUBSTR/INSTR 퀴즈
-- Student 테이블을 참조해서 아래 화면과 같이 1전공이(deptno1 컬럼) 201번인 학생의 이름과 전화번호와 지역번호를 출력하세요. 단, 지역번호는 숫자만 나와야 합니다.
SELECT name, tel, substr(tel,1,instr(tel,')', 1, 1)-1) "AREA CODE"
  FROM student 
 WHERE deptno1 = 201;


-- p.80
-- 사용 예 
-- student 테이블에서 1전공이 201번인 학과 학생들의 id를 총 10자리로 출력하되 왼쪽 빈자리는 '*'기호로 채우세요.
SELECT name, id, LPAD(id, 10, '*')
  FROM student
 WHERE deptno1 = 201;


-- p.81
-- LPAD 퀴즈
-- emp 테이블을 사용하여 아래 화면과 같이 deptno가 10번인 사원들의 사원 이름을 총 9바이트로 출력하되 빈자리에는 해당 자리의 숫자로 채우세요.
SELECT LPAD(ename, 9, '1234') "LPAD"
  FROM emp 
 WHERE deptno = 10;

-- 사용 예
-- emp테이블에서 아래와 같이 deptno가 10번인 사원들의 ename을 10자리로 출력하되 오른쪽 빈자리에는 '-'로 채우세요.
SELECT RPAD(ename, 10, '-') "RPAD"
  FROM emp 
 WHERE deptno = 10;


-- p.82
-- RPAD 퀴즈
-- 아래 화면과 같이 emp테이블에서 deptno가 10번인 사원들의 이름을 총 9자리로 출력하되 오른쪽 빈자리에는 해당 자릿수에 해당되는 숫자가 출력되도록 하세요.
SELECT RPAD(ename, 9, substr('123456789',LENGTH(ename)+ 1,9)) "RPAD"
  FROM emp 
 WHERE deptno = 10;


-- p.84 ~ 85
-- REPLACE 퀴즈 1
-- emp테이블에서 아래와 같이 20번 부서에 소속된 직원들의 이름과 2~3번째 글자만 '-'으로 변경해서 출력하세요.
SELECT ename, REPLACE(ename, substr(ename,2,2), '--') "REPLACE"
  FROM emp 
 WHERE deptno = 20;

-- REPLACE 퀴즈 2
-- Student테이블에서 아래와 같이 1전공(deptno1)이 101번인 학생들의 이름과 주민등록번호를 출력하되 주민등록번호의 뒤 7자리는 '-'과 '/'로 표시되게 출력하세요.
SELECT name, jumin, REPLACE(jumin, substr(jumin,7),'-/-/-/-') "REPLACE"
  FROM student 
 WHERE deptno1 = 101;

-- REPLACE 퀴즈 3
-- Student 테이블에서 아래 그림과 같이 1전공이 102번인 학생들의 이름과 전화번호, 전화번호에서 국번 부분만 '*'처리하여 출력하세요. 단, 모든 국번은 3자리로 간주합니다.
SELECT name, tel, REPLACE(tel, substr(tel,5,3),'***') "REPLACE"
  FROM student
 WHERE deptno1 = 102;

-- REPLACE 퀴즈 4
-- Student 테이블에서 아래와 같이 deptno1이 101번인 학과 학생들의 이름과 전화번호와 전화번호에서 지역번호와 국번을 제외한 나머지 번호를 *로 표시해서 출력하세요.
SELECT name, tel, REPLACE(tel, substr(tel, 9,4),'****') "REPLACE"
  FROM student
 WHERE deptno1 = 101;


-- p.105 ~ 106
-- 형 변환 함수 퀴즈: 날짜 변환하기 1
-- Student테이블의 birthday 컬럼을 사용하여 생일이 1월인 학생의 이름과 birthday를 아래 화면과 같이 출력하세요. (아래 두 개 그림 중 독자 여러분의 OS에 맞는 것으로 실행하세요.)
SELECT studno, name, TO_CHAR(birthday, 'DD-MM-YY') "BIRTHDAY"
  FROM student
 WHERE TO_CHAR(birthday, 'MM') = '01';

SELECT studno, name, TO_CHAR(birthday, 'DD/MM/YY') "BIRTHDAY"
  FROM student
 WHERE TO_CHAR(birthday, 'MM') = '01';

-- 형 변환 함수 퀴즈: 날짜 변환하기 2
-- emp 테이블의 hiredate 컬럼을 사용하여 입사일이 1, 2, 3월인 사람들의 사번과 이름, 입사일을 출력하세요. (아래 두 개 그림 중 독자 여러분의 OS에 맞는 것으로 실행하세요)
SELECT empno, ename, TO_CHAR(hiredate, 'DD-MM-YY') "HIREDATE"
  FROM emp
 WHERE TO_CHAR(hiredate, 'MM') IN ('01','02','03');

SELECT empno, ename, TO_CHAR(hiredate, 'DD/MM/YY') "HIREDATE"
  FROM emp
 WHERE TO_CHAR(hiredate, 'MM') IN ('01','02','03');


-- p.107 
-- 사용 예 1 
-- emp 테이블을 조회하여 이름이 'ALLEN'인 사원의 사번과 이름과 연봉을 출력ㅎ사세요. 단, 연봉은 (sal*12)+comm로 계산하고 천 단위 구분 기호로 표시하세요.
SELECT empno, ename, sal, comm, TO_CHAR((sal*12)+comm, '999,999') "SALARY"
  FROM emp 
 WHERE ename = 'ALLEN';

-- 사용 예 2
-- professor 테이블을 조회하여 201번 학과에 근무하는 교수들의 이름과 급여, 보너스, 연봉을 아래와 같이 출력하세요. 단, 연봉은 (pay*12)+bonus로 계산합니다. 
SELECT name, pay, bonus, TO_CHAR((pay*12)+bonus, '999,999') "TOTAL"
  FROM professor
 WHERE deptno = 201;


-- p.108
-- 형 변환 함수 퀴즈 3
-- emp 테이블을 조회하여 comm값을 가지고 있는 사람들의 empno, ename, hiredate, 총 연봉, 15% 인상 후 연봉을 아래 화면처럼 출력하세요. 
-- 단, 총 연봉은 (sal*12)+comm으로 계산하고 아래 화면에서는 SAL로 출력되었으며 15% 인상한 값은 총 연봉의 15% 인상 값입니다. (HIREDATE 컬럼의 날짜 형식과 SAL 컬럼, 15% UP컬럼의 $표시와 기호가 나오게 하세요)
SELECT empno, ename, TO_CHAR(hiredate, 'YYYY-MM-DD') "HIREDATE",
                     TO_CHAR((sal*12)+comm, '$999,999') "SAL",
                     TO_CHAR((sal*12)+comm*1.15, '$999,999') "15% UP"
  FROM emp
 WHERE COMM IS NOT NULL;


-- p.112
-- NVL 함수 퀴즈
-- Professor 테이블에서 201번 학과 교수들의 이름과 급여, bonus, 총 연봉을 아래와 같이 출력하세요. 단, 총 연봉은 (pay*12+bonus)로 계산하고 bonus가 없는 교수는 0으로 계산하세요.
SELECT profno, name, pay, bonus, TO_CHAR((pay*12)+NVL(bonus,0), '999,999') "TOTAL"
  FROM professor
 WHERE deptno = 201;

-- 사용 예
-- emp 테이블에서 deptno가 30번인 사람들의 empno, ename, sal, comm 값을 출력하되 만약 comm 값이 null 아니면 sal+comm 값을 출력하고 comm값이 null이면 sal*0의 값을 출력하세요.
SELECT empno, ename, sal, comm, NVL2(comm, sal+comm, sal*0) "NVL2"
  FROM emp 
 WHERE deptno = 30;


-- p.113
-- NVL2 함수 퀴즈
-- 아래 화면과 같이 emp테이블에서 deptno가 30번인 사원들을 조회하여 comm값이 있을 경우 'Exist'을 출력하고 comm값이 null일 경우 'NULL'을 출력하세요.
SELECT empno, ename, comm, NVL2(comm, Exist, NULL) "NVL2"
  FROM emp 
 WHERE deptno = 30;
                                                   