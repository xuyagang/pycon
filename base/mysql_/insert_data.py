import pymysql


def main():
    # 创建链接
    conn = pymysql.connect(host='localhost',
                           port=3308,
                           user='root',
                           passwd='devil',
                           db='test_db',
                           charset='utf8')
    # 获取游标
    curs = conn.cursor()
    # 执行insert语句
    count = curs.execute('insert into fatboy_hobby values(0, '
                         '"肥仔白","打dota、吃槟榔","挨踢攻城狮","铜锣湾")')
    print(f'受影响的行数：{count}')
    # 提交更改
    conn.commit()
    # 关闭游标和连接
    curs.close()
    conn.close()
if __name__ == '__main__':
    main()