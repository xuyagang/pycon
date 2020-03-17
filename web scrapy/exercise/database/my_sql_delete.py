import pymysql

db = pymysql.connect(
    host='localhost',
    port=3308,
    user='root',
    passwd='devil',
    db='test_db',
    charset='utf8'
)
cursor = db.cursor()
table = 'students'
condition = 'age > 20'

sql = 'DELETE from {table} where {condition}'.format(table,condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()