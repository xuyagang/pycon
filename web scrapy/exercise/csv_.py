import csv 

with open('./exercise/csv_data.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    # 调用 writerow（）方法传入每行的数据即可完成写入
    writer.writerow(['id', 'name', 'age'])
    # 调用一次 writerow（）方法即可写入一行数据
    writer.writerow(['10001', ' Mike', 20])
    writer.writerow(['10002', 'Bob', '22'])

# 修改列与列之间的分隔符，可以传入 delimiter 参数
with open('./exercise/csv_data.csv','w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    # 调用 writerow（）方法传入每行的数据即可完成写入
    writer.writerow(['id', 'name', 'age'])
    # 调用一次 writerow（）方法即可写入一行数据
    writer.writerow(['10001', ' Mike', 20])
    writer.writerow(['10002', 'Bob', '22'])

# 以调用 writerows（）方法同时写入多行, 此时参数就需要为二维列表，
import csv

with open('./exercise/data.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerows([['10001','Mike',20], ['10002','Bob', 22]])

# csv写入字典对象
import csv
with open('./exercise/data_.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 10})
    writer.writerow({'id':'10002 ', 'name': 'Bob', 'age': 22}) 

# 追加写入
import csv
with open('./exercise/data_.csv', 'a', encoding='utf-8') as csvfile:
    # 先定义头部信息
    fieldnames = ['id', 'name', 'age']
    # 定义写入对象
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 写入文件
    writer.writerow({'id':'10005', 'name': 'adam', 'age': 29})


# 可通过 Pandas 的 to_csv() 方法将数据写入csv文件
import pandas as pd
df = pd.Dataframe(data)
df.to_csv('test.csv',header=True, index=True)


# 读取
# 使用csv读取文件
# 如果csv文件中包含中文，需要指定文件编码
import csv
with open('./exercise/data.csv', 'r', encoding='utf-8') as csvfile:
    # 读操作：对打开的文件使用csv库的 reader 构造读取对象
    # 写操作：对打开的文件使用csv库的 writer, DictWriter 构造写对象
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


# Pandas读取csv
import pandas as pd
df = pd.read_csv('./exercise/data.csv')
print(df)


