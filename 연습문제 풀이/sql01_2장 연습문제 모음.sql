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


-- p.114
-- 유형1 - A가 B일 경우 '1'을 출력하는 경우
-- 유형1 예제: professor 테이블에서 학과번호와 교수명, 학과명을 출력하되 deptno가 101번인 교수만 학과명을 "Computer Engineering"으로 출력하고 101번이 아닌 교수들은 학과명에 아무것도 출력하지 마세요.
SELECT deptno, name, decode(deptno, 101, 'Computer Engineering') "DNAME"
  FROM professor;


-- p.115
-- 유형2 - A가 B일 경우 '1'을 출력하고 아닐 경우 '2'을 출력하는 경우
-- 유형2 예제: professor 테이블에서 학과번호와 교수명과 학과명을 출력하되 deptno가 101번인 교수만 "Computer Engineering"으로 출력하고 101번이 아닌 교수들은 학과명에 "ETC"로 출력하세요.
SELECT deptno, name, decode(deptno, 101, 'Computer Engineering', 'ETC') "DNAME"
  FROM professor;


-- p.116 
-- 유형3 - A가 B일 경우 '1'을 출력하고 A가 C일 경우 '2'을 출력하고 둘 다 아닐 경우 '3'을 출력하는 경우 
-- 유형3 예제: Professor 테이블에서 교수의 이름과 학과명을 출력하되 학과 번호가 101번 이면 'Computer Enginerring', 102번이면 'Multimedia Engineering', 103번이면 'Software Engineering' 나머지는 'ETC'로 출력하세요.
SELECT deptno, name, decode(deptno, 101, 'Computer Engineering'
                                  , 102, 'Multimedia Engineering'
                                  , 103, 'Software Engineering'
                                       , 'ETC') "DNAME"
  FROM professor;


-- p.117 
-- 유형4 - A가 B일 경우 중에서 C가 D를 만족하면 '1'을 출력하고 C가 D가 아닐 경우 NULL을 출력하는 경우(DECODE 함수 안에 DECODE 함수가 중첩되는 경우)
-- 유형4 예제: professor 테이블에서 교수의 이름과 부서번호를 출력하고 101번 부서 중에서 이름이 "Audie Murphy" 교수에게 "BEST!"라고 출력하고 101번 부서 중에서 이름이 "Audie Murphy" 교수가 아닌 나머지에는 NULL값을 출력하세요. 만약 101번 외 다른 학과에 "Audie Murphy" 교수가 있어도 "BEST!"가 출력되면 안 됩니다. 
SELECT deptno, name, decode(deptno, 101, decode(name, 'Audie Murphy', 'BEST!')) "ETC"
  FROM professor;


-- p.118
-- 유형5 - A가 B일 경우 중에서 C가 D를 만족하면 '1'을 출력하고 C가 D가 아닐 경우 '2'를 출력하는 경우
-- 유형5 예제: professor 테이블에서 교수의 이름과 부서번호를 출력하고 101번 부서 중에서 이름이 "Audie Murphy"교수에게 비고란에 "BEST!"라고 출력한 다음 101번 학과의 "Audie Murphy"교수 외에는 비고란에 "GOOD!"을 출력하고 101번 교수가 아닐 경우는 비고란이 공란이 되도록 출력하세요.
SELECT deptno, name, decode(deptno, 101, DECODE(name, 'Audie Murphy', 'BEST!', 'GOOD!')) "ETC"
  FROM professor;


-- p.119
-- 유형6 - professor테이블에서 교수의 이름과 부서번호를 출력하고 101번 부서 중에서 이름이 "Audie Murphy"교수에게 비고란에 "BEST!"라고 출력하고 101번 학과의 "Audie Murphy"교수 외에는 비고란에 "GOOD!"을 출력하며 101번 교수가 아닐 경우는 비고란에 "N/A"을 출력하세요.
SELECT deptno, name, decode(deptno, 101, decode(name, 'Audie Murphy', 'BEST!', 'GOOD!'),'N/A') "ETC"
  FROM professor;


-- p.120
-- decode 퀴즈 1
-- Student 테이블을 사용하여 제1전공(deptno1)이 101번인 학과 학생들의 이름과 주민번호, 성별을 출력하되 성별은 주민번호(jumin) 컬럼을 이용하여 7번째 숫자가 1일 경우 "MAN", 2일 경우 "WOMAN"으로 출력하세요.
SELECT name, jumin, decode(substr(jumin, 7,1), 1, 'MAN', 2, 'WOMAN') "Gender"
  FROM student
 WHERE deptno1 = 101;

-- decode 퀴즈 2
-- Student 테이블에서 1전공이(deptno1) 101번인 학생의 이름과 연락처와 지역을 출력하세요. 단, 지역번호가 02는 "SEOUL", 031은 "GYEONGGI", 051은 "BUSAN", 052는 "ULSAN", 055은 "GYEONGNAM"입니다. 
SELECT name, tel, decode(substr(tel, 1, 3), '02)', 'SEOUL'
                                          , '031', 'GYEONGGI'
                                          , '051', 'BUSAN'
                                          , '052', 'ULSAN'
                                          , '055', 'GYEONGNAM') "LOC"
  FROM STUDENt
 WHERE deptno1 = 101;


-- p.121
-- DECODE와 동일하게 '='조건으로 사용되는 경우
-- Student 테이블을 참조하여 deptno1이 201번인 학생의 이름과 전화번호, 지역명을 출력하세요. 단, 지역번호가 02면 "SEOUL", 031이면 "GYEONGGI", 051이면 "BUSAN", 052이면 "ULSAN", 055이면 'GYEONGNAM', 나머지는 "ETC"로 표시하세요.
SELECT name, tel, CASE(substr(tel, 1, instr(tel, ')')-1)) WHEN '02' THEN 'SEOUL'
                                                          WHEN '031' THEN 'GYEONGGI'
                                                          WHEN '051' THEN 'BUSAN'
                                                          WHEN '052' THEN 'ULSAN'
                                                          WHEN '055' THEN 'GYEONGNAM'
                                                                     ELSE 'ETC'
                                                                     END "LOC"
  FROM Student 
 WHERE deptno1 = 201;


-- p.122
-- 비교 조건이 '='가 아닌 경우
-- Student 테이블의 jumin 컬럼을 참조하여 학생들의 이름과 태어난 달, 그리고 분기를 출력하세요. 태어난 달이 01-03월은 1/4, 04-06월은 2/4, 07-09월은 3/4, 10-12월은 4/4로 출력하세요.
SELECT name, substr(jumin,3,2)  "MONTH",
	   CASE WHEN substr(jumin,3,2) BETWEEN '01' AND '03' THEN '1/4'
	        WHEN substr(jumin,3,2) BETWEEN '04' AND '06' THEN '2/4'
	        WHEN substr(jumin,3,2) BETWEEN '07' AND '09' THEN '3/4'
	        WHEN substr(jumin,3,2) BETWEEN '10' AND '12' THEN '4/4'
       END "Quarter"
  FROM student;


-- p.123
-- CASE문 퀴즈
-- emp 테이블을 조회하여 empno, ename, sal, LEVEL(급여등급)을 아래와 같이 출력하세요. 단, 급여등급은 sal을 기준으로 1-1000이면 Level 1, 1001-2000이면 Level 2, 2001-3000이면 Level 3, 3001-4000이면 Level 4, 4001보다 많으면 Level 5로 출력하세요.
SELECT empno, ename, sal,
       CASE WHEN sal BETWEEN '1' AND '1000' THEN 'Level 1'
            WHEN sal BETWEEN '1001' AND '2000' THEN 'Level 2'
            WHEN sal BETWEEN '2001' AND '3000' THEN 'Level 3'
            WHEN sal BETWEEN '3001' AND '4000' THEN 'Level 4'
            WHEN sal > 4001 THEN 'Level 5'
       END "LEVEL"
  FROM emp 
 ORDER BY sal DESC;


-- p.147
-- 사용 예1 
-- 교수테이블(professor)에서 홈페이지(hpage) 주소가 있는 교수들만 조사해서 아래의 화면처럼 나오게 출력하세요.
SELECT name, LTRIM(REGEXP_SUBSTR(hpage,'/([[:alnum:]]+\.?){3,4}?'),'/') "URL"
  FROM professor 
 WHERE hpage IS NOT NULL;

-- p.148
-- 사용 예2
-- Professor 테이블에서 101번 학과와 201번 학과 교수들의 이름과 메일 주소의 도메인 주소를 출력하세요. 단, 메일 주소는 @뒤에 있는 주소만 출력하세요. 
SELECT name, LTRIM(REGEXP_SUBSTR(email, '@([[:alnum:]]+\.?){3,4}?'),'@') DOMAIN
  FROM professor 
 WHERE deptno IN (101,201);