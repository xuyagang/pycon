# 可用 star expression 解压多个元素给变量
# 比如获取列表中排除首末元素的元素
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212') 
_, *data, _ = record
print(data)			# ['dave@example.com', '773-555-1212']

# star expression 都会返回一个列表，解压的元素个数是为0时为空列表

# 星号表达式在迭代元素为可变长元组的序列时是很有用
records = [('foo', 1, 3), 
		   ('bar', 'hello'), 
		   ('foo', 3, 4)]

for tag, *data in records:
	# print(tag)
	print(data)



# 你想解压一些元素后丢弃它们，你不能简单就使用 * ，
# 但是你可以使用一 个普通的废弃名称，比如 或者 ign
record = ('ACME', 50, 123.45, (12, 18, 2012)) 
name, *_, (*_, year) = record
print('name:',name,'\nyear:',year)