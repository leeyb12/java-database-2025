-- p.84 
-- emp테이블에서 아래와 같이 20번 부서에 소속된 직원들의 이름과 2~3번째 글자만 '-'으로 변경해서 출력하세요.
SELECT * 
  FROM emp;

SELECT ename, REPLACE(ename, substr(ename,2,3), '--') "REPLACE"
  FROM emp
 WHERE deptno = 20;

-- Student 테이블에서 아래와 같이 1전공(deptno1)이 101번인 학생들의 이름과 주민등록번호를 출력하되 주민등록번호의 뒤 7자리는 '-'과 '/'로 표시되게 출력하세요.
SELECT * 
  FROM Student;

SELECT name, REPLACE(jumin, substr(jumin,7),'-/-/-/-') "REPLACE"
  FROM Student
 WHERE deptno1 = 101;

-- Student 테이블에서 아래 그림과 같이 1전공이 102번인 학생들의 이름과 전화번호, 전화번호에서 국번 부분만 '*'처리하여 출력하세요.단, 모든 국번은 3자리로 간주합니다.
SELECT *
  FROM Student;

SELECT name, REPLACE(tel, substr(tel,5,3), '***') "REPLACE"
  FROM Student
 WHERE deptno1 = 102;

-- Student 테이블에서 아래와 같이 deptno1이 101번인 학과 학생들의 이름과 전화번호와 전화번호에서 지역번호와 국번을 제외한 나머지 번호를 *로 표시해서 출력하세요.
SELECT *
  FROM Student;

SELECT name, REPLACE(tel, substr(tel,9,4), '****') "REPLACE"
  FROM Student
 WHERE deptno1 = 101;

-- p.105~106, 108
-- Student 테이블의 birthday 컬럼을 사용하여 생일이 1월인 학생의 이름과 birthday를 아래 화면과 같이 출력하세요.(아래 두 개 그림 중 독자 여러분의 OS에 맞는 것으로 실행하세요)
SELECT * 
  FROM Student;

SELECT studno, name, to_char(birthday,'DD-MM-YY') "birthday"
  FROM Student
 WHERE to_char(birthday,'MM') = '01'

SELECT studno, name, to_char(birthday,'DD/MM/YY') "birthday"
  FROM Student
 WHERE to_char(birthday,'MM') = '01'

-- emp테이블의 hiredate 컬럼을 사용하여 입사일이 1,2,3월인 사람들의 사번과 이름, 입사일을 출력하세요. (아래 두 개 그림 중 독자 여러분의 OS에 맞는 것으로 실행하세요)
SELECT *
  FROM emp;

SELECT empno, ename, to_char(hiredate, 'YY-MM-DD') "hiredate"
  FROM emp 
 WHERE to_char(hiredate,'MM') in ('01','02','03');

SELECT empno, ename, to_char(hiredate, 'YY/MM/DD') "hiredate"
  FROM emp 
 WHERE to_char(hiredate,'MM') in ('01','02','03');

-- emp 테이블을 조회하여 comm값을 가지고 있는 사람들의 empno, ename, hiredate, 총 연봉, 