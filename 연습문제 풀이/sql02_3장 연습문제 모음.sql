-- 3장

-- 연습문제 p.210 ~ 216
-- 1. emp 테이블을 사용하여 사원 중에서 급여(sal)와 보너스(comm)를 합친 금액이 가장 많은 경우와 가장 적은 경우, 평균 금액을 구하세요. 단, 보너스가 없을 경우는 보너스를 0으로 계산하고 출력 금액은 모두 소수점 첫째 자리까지만 나오게 하세요. 
SELECT max(sal+nvl(comm, 0)) "MAX",
       min(sal+nvl(comm, 0)) "MIN",
       round(avg(sal+nvl(comm, 0)), 1) "AVG"
  FROM emp;

-- 2. student 테이블의 birthday컬럼을 참조해서 아래와 같이 월별로 생일자 수를 출력하세요.
SELECT count(birthday) || 'EA' "TOTAL",
       count(decode(substr(birthday, 4, 2), '01','0')) || 'EA' "JAN",
       count(decode(substr(birthday, 4, 2), '02','0')) || 'EA' "FEB",
       count(decode(substr(birthday, 4, 2), '03','0')) || 'EA' "MAR",
       count(decode(substr(birthday, 4, 2), '04','0')) || 'EA' "APR",
       count(decode(substr(birthday, 4, 2), '05','0')) || 'EA' "MAY",
       count(decode(substr(birthday, 4, 2), '06','0')) || 'EA' "JUN",
       count(decode(substr(birthday, 4, 2), '07','0')) || 'EA' "JUL",
       count(decode(substr(birthday, 4, 2), '08','0')) || 'EA' "AUG",
       count(decode(substr(birthday, 4, 2), '09','0')) || 'EA' "SEP",
       count(decode(substr(birthday, 4, 2), '10','0')) || 'EA' "OCT",
       count(decode(substr(birthday, 4, 2), '11','0')) || 'EA' "NOV",
       count(decode(substr(birthday, 4, 2), '12','0')) || 'EA' "DEC"
 FROM student;

-- 3. Student 테이블의 tel컬럼을 참고하여 아래와 같이 지역별 인원수를 출력하세요. 단, 02-SEOUL, 031-GYEONGGI, 051-BUSAN, 052-ULSAN, 053-DAEGU, 055-GYEONGNAM으로 출력하세요.
SELECT count(tel) || 'EA' "TOTAL", 
       count(decode(substr(tel, 1, instr(tel,')')-1), '02', '0')) "SEOUL", 
       count(decode(substr(tel, 1, instr(tel,')')-1), '031', '0')) "GYEONGGI",
       count(decode(substr(tel, 1, instr(tel,')')-1), '051', '0')) "BUSAN",
       count(decode(substr(tel, 1, instr(tel,')')-1), '052', '0')) "ULSAN",
       count(decode(substr(tel, 1, instr(tel,')')-1), '053', '0')) "DAEGU",
       count(decode(substr(tel, 1, instr(tel,')')-1), '055', '0')) "GYEONGNAM"
  FROM student; 

-- 4. 먼저 emp테이블에 아래 두 건의 데이터를 입력한 후 작업하세요. Emp테이블을 사용하여 아래의 화면과 같이 부서별로 직급별로 급여 합계 결과를 출력하세요.
INSERT INTO emp (empno, deptno, ename, sal)
VALUES (1000, 10, 'Tiger', 3600);

INSERT INTO emp (empno, deptno, ename, SAL)
VALUES (2000, 10, 'Cat', 3000); 

COMMIT;

SELECT deptno,
       sum(decode(job, 'CLERK', sal, 0)) "CLERK",
       sum(decode(job, 'SALESMAN', sal, 0)) "SALESMAN",
       sum(decode(job, 'MANAGER', sal, 0)) "MANAGER",
       sum(decode(job, 'PRESIDENT', sal, 0)) "PRESIDENT",
       sum(decode(job, 'ANALYST', sal, 0)) "ANALYST",
       sum(nvl2(job, sal, 0)) "TOTAL"
  FROM emp
  GROUP BY rollup(deptno)
  ORDER BY deptno;

-- 5. emp테이블을 사용하여 직원들의 급여와 전체 급여의 누적 급여금액이 아래와 같도록 출력하세요. 단, 급여를 오름차순으로 정렬해서 출력하세요.
SELECT deptno, ename, sal, sum(sal) over(ORDER BY sal)
  FROM emp;

-- 6. fruit테이블을 아래와 같은 형태로 출력하세요.
SELECT sum(decode(name, 'apple', price)) "APPLE",
       sum(decode(name, 'grape', price)) "GRAPE",
       sum(decode(name, 'orange', price)) "ORANGE"
  FROM fruit;

-- 7. student 테이블의 Tel 컬럼을 사용하여 아래와 같이 지역별 인원수와 전체 대비 차지하는 비율을 출력하세요. 단, 02-SEOUL, 031-GYEONGGI, 051-BUSAN, 052-ULSAN, 053-DAEGU, 055-GYEONGNAM으로 출력하세요.
SELECT count(tel) ||'EA'||'('||round(count(tel)/count(tel)*100, 0)||'%)' "TOTAL", 
       count(decode(substr(tel, 0, instr(tel, ')')-1), '02', 0))||'EA'||' ('||round(count(decode(substr(tel, 0, instr(tel, ')')-1), '02', 0))/count(tel)*100, 0)||'%)' "SEOUL",
       count(decode(substr(tel, 0, instr(tel, ')')-1), '031', 0))||'EA'||' ('||round(count(decode(substr(tel, 0, instr(tel, ')')-1), '031', 0))/count(tel)*100, 0)||'%)' "GYEONGGI",
       count(decode(substr(tel, 0, instr(tel, ')')-1), '051', 0))||'EA'||' ('||round(count(decode(substr(tel, 0, instr(tel, ')')-1), '051', 0))/count(tel)*100, 0)||'%)' "BUSAN",
       count(decode(substr(tel, 0, instr(tel, ')')-1), '052', 0))||'EA'||' ('||round(count(decode(substr(tel, 0, instr(tel, ')')-1), '052', 0))/count(tel)*100, 0)||'%)' "ULSAN",
       count(decode(substr(tel, 0, instr(tel, ')')-1), '053', 0))||'EA'||' ('||round(count(decode(substr(tel, 0, instr(tel, ')')-1), '053', 0))/count(tel)*100, 0)||'%)' "DAEGU",
       count(decode(substr(tel, 0, instr(tel, ')')-1), '055', 0))||'EA'||' ('||round(count(decode(substr(tel, 0, instr(tel, ')')-1), '055', 0))/count(tel)*100, 0)||'%)' "GYEONGNAM"
  FROM student;

-- 8. emp 테이블을 사용하여 아래와 같이 부서별로 급여 누적 합계가 나오도록 출력하세요. 단, 부서 번호로 오름차순 출력하세요.
SELECT deptno, ename, sal,sum(sal) over(PARTITION BY deptno ORDER BY sal) "TOTAL"
  FROM emp;

-- 9. emp 테이블을 사용하여 아래와 같이 각 사원의 급여액이 전체 직원 급여 총액에서 몇 %의 비율을 차지하는지 출력하세요. 단, 급여 비중이 높은 사람이 먼저 출력되도록 하세요.
SELECT deptno, ename, sal, sum(sal) over() "TOTAL_SAL", round(ratio_to_report(sum(sal)) over()*100, 2) "%"
  FROM emp 
 GROUP BY deptno, ename, sal
 ORDER BY sal DESC;

-- 10. emp테이블을 조회하여 아래와 같이 각 직원들의 급여가 해당 부서 합계금액에서 몇 %의 비중을 차지하는지를 출력하세요. 단, 부서 번호를 기준으로 오름차순으로 출력하세요.
SELECT deptno, ename, sal, sum(sal) over(PARTITION BY deptno ORDER BY deptno) "SUM_DEPT", round(ratio_to_report(sum(sal)) over(PARTITION BY deptno)*100, 2) "%"
  FROM emp 
 GROUP BY deptno, ename, sal;

-- 11. loan 테이블을 사용하여 1000번 지점의 대출 내역을 출력하되 대출일자, 대출종목코드, 대출건수, 대출총액, 누적대출금액을 아래와 같이 출력하세요.
SELECT l_date "대출일자", l_code "대출종목코드", l_qty "대출건수", l_total "대출총액", sum(l_total) over(ORDER BY l_date) "누적대출금액"
  FROM loan
 WHERE l_store=1000;

-- 12. loan 테이블을 사용하여 전체 지점의 대출종목코드, 대출지점, 대출일자, 대출건수, 대출액을 대출코드와 대출지점별로 누적 합계를 구하세요.
SELECT l_code "대출종목코드", l_store "대출지점", l_date "대출일자", l_qty "대출건수", l_total "대출액",
       sum(l_total) over(PARTITION BY l_code, l_store ORDER BY l_date) "누적대출금액"
  FROM loan;

-- 13. loan 테이블을 조회하여 1000번 지점의 대출 내역을 대출 코드별로 합쳐서 대출일자, 대출구분코드, 대출건수, 대출총액, 코드별 누적대출금액을 아래와 같이 출력하세요.
SELECT l_date "대출일자", l_code "대출구분코드", l_qty "대출건수", l_total "대출총액", 
       sum(l_total) over(PARTITION BY l_code ORDER BY l_qty)
  FROM loan 
 WHERE l_store = 1000;

-- 14. professor 테이블에서 각 교수들의 급여를 구하고 각 교수의 급여액이 전체 교수의 급여 합계에서 차지하는 비율을 출력하세요.
SELECT deptno, name, pay, sum(pay) over() "TOTAL_PAY", round(ratio_to_report(sum(pay)) over()*100,2) "RATIO %"
  FROM professor
 GROUP BY deptno, name, pay
 ORDER BY pay DESC;

-- 15. professor 테이블을 조회하여 학과번호, 교수명, 급여, 학과명 급여 합계를 구하고 각 교수의 급여가 해당 학과별 급여 합계에서 차지하는 비율을 출력하세요.
SELECT deptno, name, pay, sum(pay) over(PARTITION BY deptno) "TOTAL_DEPTNO", round(ratio_to_report(sum(pay)) over(PARTITION BY deptno)*100, 2) "RATIO(%)"
  FROM professor 
 GROUP BY deptno, name, pay;