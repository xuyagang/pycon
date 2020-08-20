import pymysql

# https://www.jianshu.com/p/8bb139f4b430

def main():
    # 创建连接
    conn = pymysql.connect(host='localhost',
                           port=3308,
                           user='root',
                           passwd='devil',
                           database='test_db',
                           charset='utf8')
    # 获取游标
    cursor = conn.cursor()
    # 执行select语句，返回手影响行数
    count = cursor.execute('SELECT * FROM fatboy_hobby')
    print('查询到{}条数据'.format(count))

    for i in range(count):
        # 获取查询结果
        result = cursor.fetchone()
        print(result)
    # 关闭游标和连接
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()