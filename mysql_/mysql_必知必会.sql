SHOW DATABASES;
USE easysql;



--  																																											第九章 Mysql 正则表达式
-- 匹配包含1000的项
SELECT prod_name 
FROM products
WHERE prod_name  REGEXP '1000'
ORDER BY prod_name;

-- 匹配包含 .000的项目
SELECT prod_name
FROM products
WHERE prod_name REGEXP '.000'
ORDER BY prod_name;

-- like的等价
-- like匹配整列，匹配值在列值中出现，like找不到
-- 下面查询无返回
SELECT prod_name
FROM products
WHERE prod_name LIKE '1000'
ORDER BY prod_name;

-- OR 匹配,选这个或另一个
SELECT prod_name
FROM products
WHERE prod_name REGEXP '1000|2000'
ORDER BY prod_name;

-- 匹配几个字符之一
SELECT prod_name
FROM products
WHERE prod_name REGEXP '[123] Ton';

-- 匹配1、2 或 3 Ton
SELECT prod_name
FROM products
WHERE prod_name REGEXP '1|2|3 Ton';

-- 匹配范围
SELECT prod_name
FROM products
WHERE prod_name REGEXP '[1-5] ton';

-- 匹配特定字符
SELECT prod_name
FROM products
WHERE prod_name REGEXP '\\.';

-- 匹配多个实例
-- ? 使得 s 可选
-- 同时匹配 stick 和 sticks
SELECT prod_name
FROM products
WHERE prod_name REGEXP '\\([0-9] sticks?\\)';

-- 匹配连在一起的任意四位数
SELECT prod_name
FROM products
WHERE prod_name REGEXP '[[:digit:]]{4}';

--  																																											第十章 创建计算字段
-- concat 
SELECT CONCAT(vend_name, '(', vend_country) as vnvc
FROM vendors
ORDER BY vend_name;

-- RTrim()
SELECT CONCAT(RTRIM(vend_name), '(', RTRIM(vend_country)) as vnvc
FROM vendors
ORDER BY vend_name;

-- 订单号中的物品
SELECT prod_id, item_price, quantity
FROM orderitems
WHERE order_num = 20005;

-- 加入计算总额
SELECT prod_id,
       item_price, 
			 quantity,
			 quantity*item_price AS expand_price
FROM orderitems
WHERE order_num = 20005;

-- SELECT省去from 可以简单的访问和处理表达式
SELECT 3*2;
SELECT NOW();


--  																																											第十一章  数据处理函数
-- UPPER函数
SELECT vend_name, UPPER(vend_name) as vend_name_upcase
FROM vendors
ORDER BY vend_name;

-- LOCATE(substr,str)
SELECT LOCATE('s',vend_name) as num
FROM vendors;

-- LEFT(str,len)
SELECT LEFT(vend_name,2) as ls
FROM vendors;

-- SUBSTRING(str FROM pos FOR len)
-- SUBSTRING(str,pos)
-- SUBSTRING(str FROM pos)
-- SUBSTRING(str,pos,len)
SELECT SUBSTRING("Hellow world" from 3 for 9);
SELECT SUBSTRING("hellow world", 4, 8);

-- SOUNDEX(str)
-- 发音比较——同音筛选
SELECT cust_name, cust_contact
FROM customers
WHERE SOUNDEX(cust_contact) = SOUNDEX("Y Lie");
SELECT DATE(NOW()), NOW();

-- 九月下的所有订单
SELECT * 
FROM orders 
WHERE DATE(order_date) 
BETWEEN '2005-09-01' AND '2005-09-30'; -- 时间对象需要用引号包起来

-- 等价实现，不用考虑闰月和月的天数
SELECT * 
FROM orders 
WHERE YEAR(order_date) = 2005 AND MONTH(order_date) = 9;

-- 数值处理函数
SELECT ABS(-1);
SELECT COS(45);
SELECT EXP(4); -- 返回自然常数的幂
SELECT MOD(5,3); -- 返回余数
SELECT PI();
-- rand sin sqrt tan 

--  																																											第十二章  汇总数据
SELECT AVG(DISTINCT prod_price) as avg_price
FROM products
WHERE vend_id = 1003;

-- 组合聚集函数
SELECT COUNT(*) AS num_items,    -- COUNT(*) 对所有行计数,不忽略null; count(column)对列计数，忽略null
			 MIN(prod_price) AS price_min, 
			 MAX(prod_price) AS price_max,
			 AVG(prod_price) as price_avg
FROM products;

--  																																											第十三章  分组数据
SELECT vend_id, COUNT(*) AS num_prods
FROM products
GROUP BY vend_id;

-- WITH ROLLUP
SELECT vend_id, COUNT(*) as num_prods
FROM products
GROUP BY vend_id WITH ROLLUP;

-- 过滤分组
SELECT cust_id, COUNT(*) AS orders
FROM orders 
GROUP BY cust_id
HAVING COUNT(*) >= 2;

-- 双重过滤
SELECT vend_id, prod_price, COUNT(*) as num_prods
FROM products
WHERE prod_price >= 10
GROUP BY vend_id
HAVING COUNT(*) >= 2;

--
SELECT order_num, SUM(quantity*item_price) AS ordertotal
FROM orderitems
GROUP BY order_num
HAVING SUM(quantity*item_price) >= 50;

-- ORDER BY排序
SELECT order_num, SUM(quantity*item_price) as order_total
FROM orderitems
GROUP BY order_num
HAVING SUM(quantity*item_price) >= 50
ORDER BY order_total;

--  																																											第十四章  使用子查询
SELECT * FROM orders;
SELECT * FROM orderitems;
SELECT * FROM customers;

-- 分步查询
SELECT order_num
FROM orderitems
WHERE prod_id = 'TNT2';

SELECT cust_id 
FROM orders 
WHERE order_num in (20005,20007)

-- 每个客户的订单总数
SELECT cust_name,
       cust_state,
			 (SELECT COUNT(*)
			  FROM orders
				WHERE orders.cust_id = customers.cust_id) AS orders_
FROM customers
ORDER BY cust_name;

--  																																									第十五章  链接表
SELECT vend_name, prod_name, prod_price
FROM vendors, products
WHERE vendors.vend_id = products.vend_id
ORDER BY vend_name, prod_name;

SELECT * 
FROM customers, orders
WHERE customers.cust_id = orders.cust_id
ORDER BY customers.cust_id;


--  																																									第十六章  高级联结
-- 子查询操作
SELECT prod_id, prod_name
FROM products
WHERE vend_id = (SELECT vend_id
                 FROM products
								 WHERE prod_id = 'DTNTR'
);

-- 自联结操作
SELECT *
FROM products AS p1, products AS p2
WHERE p1.vend_id = p2.vend_id
  AND p2.prod_id = 'DTNTR'

-- 自然联结
SELECT c.*, o.order_num, o.order_date,
       oi.prod_id, oi.quantity, oi.item_price
FROM customers AS c, orders as o, orderitems AS oi
WHERE c.cust_id = o.cust_id
  AND oi.order_num = o.order_num
	AND prod_id = 'FB'

--  外部联结
SELECT customers.cust_id, orders.order_num
FROM customers LEFT JOIN orders
ON orders.cust_id = customers.cust_id;

SELECT customers.cust_id, orders.order_num
FROM customers RIGHT JOIN orders
ON orders.cust_id = customers.cust_id;

-- 使用带聚集函数的联结
--  检索所有客户及每个客户所下的订单数
SELECT customers.cust_name, 
       customers.cust_id,
       COUNT(orders.order_num)
FROM customers INNER JOIN orders
ON customers.cust_id = orders.cust_id
GROUP BY customers.cust_id;

SELECT customers.cust_id,
       customers.cust_name,
			 COUNT(orders.order_num) AS num_ord
FROM customers LEFT JOIN orders
ON customers.cust_id = orders.cust_id
GROUP BY customers.cust_id;



 
























