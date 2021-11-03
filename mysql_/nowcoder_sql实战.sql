select *
from employees
-- 子查询需要加括号
where hire_date = (select max(hire_date) from employees);