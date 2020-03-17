import pymongo

# 创建连接
client = pymongo.MongoClient(host='localhost', port=27017)
# 另外一中连接方式，也是mongdb compass的连接方式
# client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# 数据库的另外一种指定方式
db = client['test']

# 指定集合
# 数据库包含很多集合（collection），类似sql中的表
# 两种指定方式
collection = db.students
collection = db['students']

# 插入数据
# 字典形式数据
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
# 使用insert方法即可插入
result = collection.insert(student)
print(result)
# mongodb中每个数据都有一个 _id属性来唯一标识，没有显式的指定该属性
# mongodb会自动产生一个objectId类型的_id属性，insert方法执行后返回id值

# 也可插入多条，只需要以list形式传入即可
result = collection.insert([student1, student2])
# 返回结果是_id的集合

# 官方推荐使用insert_one() 和 insert_many() 分别插入一条和多条
# insert 不同的是此两个方法返回InsertOneResult对象，
# 我们可以调用其inserted_id获取_id
posts = db.posts
post_id = posts.insert_one(post).inserted_id

# insert_many()方法，我们可以将数据以列表方式传入
result = collection.insert_many([student1, student2])


# 查询
# 插入数据后可以使用find_one() 和 find() 方法查询
# find_one()返回单个结果，find()查多条数据，返回一个生成器对象
result = collection.find_one({'name':'mike'})
# 返回字典类型，会多一条_id属性，是自动添加的

# 也可以通过ObjectId 结合 _id 来查询数据
# 此时需要调用bson库里的objectid
from bson.objectid import ObjectId
result = collection.find_one({'_id':ObjectId('_id_numbers')})
# 返回同样的结果，不存在则返回None

# 利用find方法查询多条数据
# 返回结果是Cursor类型，相当于一个生成器，我们需要遍历获取结果
results = collection.find({'age':20})
print(result)
>>> <pymongo.cursor.Cursor object at 0x1032d1528>
for result in results:
    print(result)
    # 得到多个字典

# 查询年龄大于20的数据
results = collection.find({'age':{'$gt':20}})
# 查询条件是一个嵌套字典

# 还可以通过正则匹配查询，例如，查询名字以M开头的学生数据
result = collection.find({'name':{'$regex':'^M.*'}})



# 计数
# 要统计查询结果有多少条，可以使用count()
count = collection.find().count()

# 排序
# 排序调用sort() 方法，传入排序字段和升降序的标志
results = collection.find().sort('name',pymongo.ASCENDING)
print(results['name'])

# 偏移
# 某些情况下我们可能只想取某几个元素，这时可使用skip偏移几个位置
# 比如偏移2就忽略两个元素，得到后面的元素
results = collection.find().skip(2)
# 可以使用limit方法指定要获取的元素个数
results = collection.find().skip(2).limit(3)
# 在数据库非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量查询数据
# 这样可能导致内存溢出，可以使用如下操作查询
from bson.objectid import ObjectId
collection.find({'_id': {'$gt': ObjectId('id_num')}})
# 需要记录好上次查询的id

# 更新
# 方法一：
# 对于数据更新我们可以使用update,指定更新条件和数据
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
# 先指定查询条件，对查询的数据做修改，调用update更新数据
# 方法二：
# 使用$set操作符
result = collection.update(condition, {'$set': student})

# 使用$set只更新字典内存在的字段，如果之前有其他字段则不会更新不会删除
# 而不使用$set会把之前的数据全部用student字典替换，如果之前存在其他字段，则会删除
# update也不是官方推荐的方法，这里也分 update_one, update_many,用法更严格
result = collection.find({'name':'Jordan'}).skip(1)
collection.update_one({'_id': ObjectId(result[0]['_id'])}, 
                      {'$set': {'name':'Bob'}})
# update_one 第二个参数不能再直接传入修改后的字典，而是需要{'$set':student}这样
# 返回结果是updateResult类型，可调用 matched_count 和 modified_count属性
# 获取匹配的数据条数和影响的数据条数

# 例子
condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
# 查询条件为年龄大于20，修改条件为年龄加1
print(result.matched_count, result.modified_count)
# 得到匹配和修改的条数都为1

# 如果使用update_many() 则会将所有匹配的都更新

# 删除
# 调用remove()指定删除条件即可，符合条件的均被删除
result = collection.remove({'name': 'Kevin'})
# 这里有两个新的推荐方法 delete_one() 和 delete_many()
result = collection.delete_one({'name': 'Kevin'})
result2 = collection.delete_many({'age': {'$lt': 25}})
# delete_one() 删除符合条件的第一条
# delete_many() 删除符合条件的全部
# 返回结果是DeleteResult,可调用delete_count获取删除的条数


# 其他操作
find_one_and_delete()
find_one_and_replace()
find_one_and_update()
# 详细参见官网