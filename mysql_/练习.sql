



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

--  第十章 创建计算字段
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
















