-- 4장 

-- 연습문제 p.254 ~ 257

-- 1. 학생 테이블(student)과 학과 테이블(department)을 사용하여 학생이름, 1전공 학과 번호(deptno1), 1전공 학과 이름을 출력하세요(ANSI Join 문법과 Oracle 문법으로 각각 SQL으르 작성하세요).
-- Oracle 문법
SELECT s.name "STU_NAME", s.deptno1, d.dname 
  FROM student s, department d 
 WHERE s.deptno1 = d.deptno 
 ORDER BY s.studno;
-- ANSI Join 문법
SELECT s.name, s.deptno1, d.dname
  FROM student s JOIN department d
  ON s.deptno1 = d.deptno 
 ORDER BY s.studno; 

-- 2. emp2 테이블과 p_grade 테이블을 조회하여 현재 직급이 있는 사원의 이름과 직급, 현재 연봉, 해당 직급의 연봉의 하한 금액과 상한 금액을 아래 결과 화면과 같이 출력하세요.
select e.name, e.position, to_char(e.pay, '999,999,999') "PAY",
       to_char(p.s_pay, '999,999,999') "Low PAY", 
       to_char(p.e_pay, '999,999,999') "High PAY"
from emp2 e join p_grade p
on e.position = p.position;
 
select e.name, e.position, to_char(e.pay, '999,999,999') "PAY",
       to_char(p.s_pay, '999,999,999') "Low PAY", 
       to_char(p.e_pay, '999,999,999') "High PAY"
from emp2 e, p_grade p
where e.position = p.position;

-- 3. Emp2테이블과 p_grade테이블을 조회하여 사원들의 이름과 나이, 현재 직급, 예상 직급을 출력하세요. 예상 직급은 나이로 계산하며 해당 나이가 받아야 하는 직급을 의미합니다. 나이는 오늘(sysdate)을 기준으로 하되 trunc로 소수점 이하는 절삭해서 계산하세요.
SELECT e.name, trunc(months_between(sysdate, e.birthday) / 12) "Age",
       e.POSITION "CURR_POSITION", p.POSITION "BE_POSITION"
  FROM emp2 e, p_grade p
 WHERE trunc(months_between(sysdate, e.birthday) / 12) >= p.s_age 
 AND trunc(MONTHS_BETWEEN(sysdate, e.birthday) / 12) <= p.e_age;

SELECT e.name, trunc(months_between(sysdate, e.birthday) / 12) "AGE",
       e.POSITION "CURR_POSITION", p.POSITION "BE_POSITION"
  FROM emp2 e JOIN p_grade p 
  ON trunc(months_between(sysdate, e.birthday) / 12) >= p.s_age 
  AND trunc(months_between(sysdate, e.birthday) / 12) <= p.e_age;

-- 4. customer테이블과 gift테이블을 Join하여 고객이 자기 포인트보다 낮은 포인트의 상품 중 한 가지를 선택할 수 있다고 할 때 Notebook을 선택할 수 있는 고객명과 포인트, 상품명을 출력하세요.
SELECT c.gname, c.point, g.gname "Notebook"
  FROM customer c, gift g
 WHERE c.point >= g.g_start 
 AND g.gname = 'Notebook';

SELECT c.gname, c.point, g.gname "Notebook"
  FROM customer c JOIN gift g
  ON c.point >= g.g_start
  AND g.gname = 'Notebook';

-- 5. professor테이블에서 교수의 번호, 교수 이름, 입사일, 자신보다 입사일 빠른 사람 인원수를 출력하세요. 단, 자신보다 입사일이 빠른 사람 수를 오름차순으로 출력하세요(Oracle Join 구문과 ANSI Join 구문으로 각각 SQL를 작성하세요).
SELECT p1.profno, p1.name, to_char(p1.hiredate, 'YYYY-MM-DD') "HIREDATE",
       count(p2.hiredate) "COUNT"
  FROM professor p1, professor p2
 WHERE p1.hiredate > p2.hiredate(+)
 GROUP BY p1.profno, p1.name, p1.hiredate 
 ORDER BY 4;

SELECT p1.profno, p1.name, to_char(p1.hiredate, 'YYYY-MM-DD') "HIREDATE",
       count(p2.hiredate) "COUNT"
  FROM professor p1 LEFT OUTER JOIN professor p2 
  ON p1.hiredate > p2.hiredate 
  GROUP BY p1.profno, p1.name, p1.hiredate 
  ORDER BY 4;

-- 6. emp 테이블에서 사원번호, 사원이름, 입사일, 자신보다 먼저 입사한 사람 인원수를 출력하세요. 단, 자신보다 입사일이 빠른 사람수를 오름차순으로 출력하세요(Oracle Join 구문과 ANSI Join 구문으로 각각 SQL를 작성하세요.)
SELECT e1.empno, e1.ename, to_char(e1.hiredate, 'DD/MM/YY') "HIREDATE",
       count(e2.hiredate) "COUNT" 
  FROM emp e1, emp e2
 WHERE e1.hiredate > e2.hiredate(+)
 GROUP BY e1.empno, e1.ename, e1.hiredate 
 ORDER BY 4;

SELECT e1.empno, e1.ename, to_char(e1.hiredate, 'DD/MM/YY') "HIREDATE",
       count(e2.hiredate) "COUNT" 
  FROM emp e1 LEFT OUTER JOIN emp e2 
  ON e1.hiredate > e2.hiredate 
  GROUP BY e1.empno, e1.ename, e1.hiredate 
  ORDER BY 4;