# sql语句的参数化，可以有效防止sql注入
# 不同于python的字符串格式化，全部使用%s占位
import pymysql 

def main():
    conn = pymysql.connect(host='localhost',
                           port=3308,
                           user='root',
                           passwd='devil',
                           db='test_db',
                           charset='utf8')
    curs = conn.cursor()
    # 构造参数列表
    params = ['肥仔白']
    # 执行查询
    count = curs.execute('select * from fatboy_hobby where name=%s', params)
    # 如果要是有多个参数，需要进行参数化
    # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可
    print(count)
    # 获取结果
    result = curs.fetchall()
    print(f'result={result}')
    
    curs.close()
    conn.close()

if __name__ == '__main__':
    main()