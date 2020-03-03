import pymysql

# 参数
user = 'root'
password = 'devil'
port = 3308
host = 'localhost'
db = 'easysql'
# 连接数据库
db = pymysql.connect(host=host, user=user, 
                     passwd=password, port=port, db = db)
# 创建游标
cursor = db.cursor()
# 执行命令 execute()
cursor.execute('select version()')
data = cursor.fetchone()
print(data)
tables = cursor.execute('show tables')
print(tables)
db.close()

# 创建表
import pymysql

db = pymysql.connect(host='localhost', user='root',
                     passwd='devil', port=3308, db='easysql')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS test (id VARCHAR(25) NOT NULL , name VARCHAR(25) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()

# 插入数据
import pymysql

db = pymysql.connect(host='localhost', user='root', passwd='devil', 
                     port=3308, db='test_db')
cursor = db.cursor()
sql = 'insert into students(id, name, age) values(%s, %s,  %s)'
try:
    cursor.execute(sql,(id, name, age))
    db.commit()
except:
    db.rollback()
finally:
    cursor.close()
    db.close()