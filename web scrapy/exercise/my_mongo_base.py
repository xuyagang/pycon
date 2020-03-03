import pymongo

# 创建连接
client = pymongo.MongoClient(host='localhost', port=27017)
# 另外一中连接方式，也是mongdb compass的连接方式
# client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# 数据库的另外一种指定方式
# db = client['test']

# 指定集合
# 数据库包含很多集合（collection），类似sql中的表
# 两种指定方式
collection = db.students
collection = db['students']

# 插入数据
