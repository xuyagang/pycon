import pymysql

conn = pymysql.connect(host='localhost',
                       port=3308,
                       user='root',
                       passwd='devil',
                       db='test_db',
                       charset='utf8')

curs = conn.cursor()
count = curs.execute('select * from fatboy_hobby')
result = curs.fetchall()
print(result)

curs.close()
conn.close()