# 创建库
CREATE DATABASE IF NOT EXISTS test_db CHARACTER SET utf8 COLLATE utf8_general_ci;

# 创建表
# UNSIGNED 将数字类型无符号化
# int的范围 -2147483648 ~ 2147483648 
# INT UNSIGNED 范围 0 ~ 2147483648 
CREATE TABLE fatboy_hobby(
    id int UNSIGNED PRIMARY KEY auto_increment NOT NULL,
		name VARCHAR(40) DEFAULT NULL COMMENT '肥仔名称',
		hobby VARCHAR(40) DEFAULT NULL COMMENT '肥仔爱好',
		professional VARCHAR(40) DEFAULT NULL COMMENT '肥仔职业',
		adress VARCHAR(40) DEFAULT NULL COMMENT '肥仔居住地'
)

# 插入数据
INSERT INTO fatboy_hobby VALUES(null, '胖子老板', '斗地主', '小卖铺老板', '西九龙');
insert into fatboy_hobby VALUES(null,"肥仔白","打dota、吃槟榔","挨踢攻城狮","铜锣湾");
insert into fatboy_hobby VALUES(null,"肥仔超","吃槟榔、养养猫","挨踢攻城狮","大上海");


SELECT * FROM fatboy_hobby