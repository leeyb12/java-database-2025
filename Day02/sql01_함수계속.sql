/* 단일행함수 */ 
SELECT CONCAT('Hello',' Oracle')
  FROM dual;

-- 인덱스가 1부터, 일반프로그래밍언어의 배열이 0부터 시작하는 것과의 차이
-- SUBSTR(변환할값, 인덱스, 길이) - 파이썬 substring() 함수와 동일,
-- -인덱스 - 뒤에서부터 위치
SELECT substr(email, 1, 2)
     , substr(email, -2, 2)
     , email 
  FROM employees;

-- 전화번호자를때, 주민번호자를떄, SUBSTR()활용

-- INSTR(체크할문자열, 찾는글자, 시작위치, 몇번째)
SELECT '010-9999-8888'
     , instr('010-9999-8888', '-', 1, 2)
  FROM dual;

-- LPAD(문자열, 자리수, 채울문자), RPAD(문자열, 자리수, 채울문자)
-- 2025-11-23
-- 2025-3-12 -> 2025-03-12
-- 0000100 규칙인데
-- 101 -> 0000101
SELECT LPAD('100', 7, '0') -- 진짜 많이씀
     , RPAD('ABC', 7, '-') -- 잘 안씀
  FROM dual;

-- TRIM() 함수 트리플. == 파이썬 strip() 함수와 동일
-- LTRIM(), RTRIM(), TRIM()
SELECT '<<<' || '     Hello Oracle      ' || '>>>'
     , '<<<' || ltrim('     Hello Oracle      ') || '>>>'
     , '<<<' || rtrim('     Hello Oracle      ') || '>>>'
     , '<<<' || trim('     Hello Oracle      ') || '>>>'  -- 진짜 많이 씀
  FROM dual;

-- REPLACE(), 파이썬에도 동일하게 존재
SELECT phone_number
	 , REPLACE(phone_number, '123', '786') -- 많이 씀
  FROM employees;

/* 
 * 숫자함수
 * */
-- ROUND() 반올림 함수 - 파이썬 존재
SELECT 786.5427
     , round(786.5427)  -- 소수점없이
     , round(786.5427, 1)  -- 소수점1
  FROM employees;