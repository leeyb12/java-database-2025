-- 5장 

-- 연습문제 p.285 ~ 286
-- 1. 아래와 같은 구조의 일반 테이블을 생성하세요.
CREATE TABLE new_tab 
(NO NUMBER(5), NANE varchar2(20), HIREDATE DATE, BOUNS NUMBER(6,2));

-- 2. 위 1번 문제에서 생성한 new_emp테이블에서 NO, NAME, HIREDATE컬럼만 가져와서 아래 그림과 같이 new_emp2테이블을 생성하는 쿼리를 쓰세요.
CREATE TABLE new_tab2
AS 
  SELECT NO, NANE, HIREDATE 
    FROM new_tab;

-- 3. 위 2번 문제에서 생성한 new_emp2테이블과 동일한 구조의 테이블을 new_emp3이름으로 생성하되 테이블 구조만 가져오고 데이터는 가져오지 않도록 하는 쿼리를 쓰세요.
CREATE TABLE new_tab3
AS 
  SELECT * FROM new_tab2
  WHERE 1 = 0;

-- 4. 위 2번 문제에서 생성한 new_emp2 테이블에 DATE 타입을 가진 BIRTHDAY 컬럼을 추가하는 쿼리를 쓰세요. 

