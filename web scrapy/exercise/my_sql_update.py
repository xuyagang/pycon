sql = 'updata sutdents set age = %s where name = %s'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

# 利用占位符构造SQL，简单的数据更新可以用此方法
# 实际使用中，大部分的情况需要插入数据，我们关心的是会不会出现重复数据
# 如果出现了我们希望更新数据（不存在插入，存在就更新）
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'insert into {table} ({keys}) values ({values}) on duplicate key update'.format(
    table=table, keys=keys, values=values)
# ON DUPLICATE KEY UPDATE
# 如果主键存在就更新操作
update = ','.join(["{key} = %s".format(key=key)for key in data])
sql += update
try:
    # 元组和数字相乘是扩展
    if cursor.execute(sql,tuple(data.values())*2):
        print('successful')
        db.commit()
except:
    print('Faild')
    db.rollback()
db.close()
