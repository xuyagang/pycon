# 插入数据实例
import pymysql

# data示例
name = '二黑'
hobby = '抽烟'
professional = '菜贩子'
adress = '奈何桥'

db = pymysql.connect(host='localhost', port='33080', user='root',
                     passwd='devil', db='test_db')
cursor = db.cursor()
# 构造sql语句，使用 %s 格式化符来实现， 有几个 value 写几个 %s
# 然后再execute()方法第二个参数用元组传入value
sql = 'insert into fatboy_hobby(name,hobby,professional,adress) values(%s,%s,%s)'
try:
    cursor.execute(sql,(name,hobby,professional,adress))
    # 执行commit才可实现数据插入，真正将数据提交到数据库
    db.commit()
except:
    db.rollback()
db.close()

# 该操作有一个不足，比如突然增加了gender字段，此时句需要改为：
sql = 'insert into fatboy_hobby(name,hobby,professional,adress,gender)\
                   values(%s,%s,%s,%s)'
# execute的传入参数也会变


# 很多情况下，我们要达到的效果是不做改变，需要做成一个通用方法
# 只需要传入一个动态字典就，sql语句根据字典动态构造，元组也动态构造
data = {
    'name':'新管病毒',
    'hobby':'飞行',
    'professional':'杀人',
    'gender':'NP'
}
table = 'fatboy_hobby'
keys = ','.join(data.keys())
# 当时出错的地方，多加注意
value = ','.join(['%s']*len(data))
sql = 'insert into {} ({}) values({})'.format(table, keys, values)
try:
    if cursor.execute(sel):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()