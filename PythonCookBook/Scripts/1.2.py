# 星号表达式
def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phoneNumbers = record
print(phoneNumbers, name, email, sep="---")

# 看下最近一个月数据和前面 7 个月的平均值的对比
*others, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(current)

# 星号表达式在迭代元素为可变长元组的序列时是很有用的
records = [
	("foo", 1, 2),
	("bar", "hello"),
	("foo", 3, 4),
]
def do_foo(x, y):
	print("foo", x, y)
def do_bar(s):
	print("bar", s)
for tag,*args in records:	# 对遍历元素进行处理
	if tag == "foo":
		do_foo(*args)
	elif tag == "bar":
		do_bar(*args)

#字符串的分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(":")
print(uname, fields, homedir, sh, sep="\n")

#把列表分割成前后两部分
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head, tail)

#实现递归算法
def sum(items):
	head, *tail = items
	if(tail):
		head += sum(tail)
	else:
		head
	return head

def sum1(items):	# 高级写法
	head, *tail = items
	return head + sum1(tail) if tail else head
print(sum(items))