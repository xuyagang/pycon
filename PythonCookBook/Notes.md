[toc]

## 第一章：数据结构与算法

经常碰到到诸如查询，排序和过滤等等 这些普遍存在的问题，这一章的目的就是讨论这些比较常见的问题和算法。另 外，我们也会给出在集合模块 collections 当中操作这些数据结构的方法。 

### 1.1_解压序列  赋值给多变量

现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值 给 N 个变量？

```python
# 通过一个简单的赋值语句解压并赋值给多个 变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的。 
# 如果变量个数和序列元素的个数不匹配，会产生一个异常
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data 
```

这种解压赋值可以用在任何可迭代对象上面，不仅仅是列表或者元组。 包括字符串，文件对象，迭代器和生成器

```python
s = 'Hello' 
a, b, c, d, e = s 
```

只想解压一部分，丢弃其他的值。对于这种情况 Python 并没有提 供特殊的语法。但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了

```python
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data 
```

### 1.2_解压可迭代对象赋值给多个变量

```python
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
```

### 1.3保留最后N个元素

保留有限历史记录正是 collections.deque 大显身手的时候

```python
from collections import deque
# deque有一个maxlen参数，当append的时候，如果超过，那么最前面的就被挤出队列
def search(lines, pattern, history=5):
    # 限制队列长度
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

if __name__ == "__main__":
    with open(r'D:/project/pycon/PythonCookBook/Scripts/1.3.txt',encoding="utf-8") as f:
        for line, prevlines in search(f, "Python", 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print("-" * 20)
```

- 在写查询元素的代码时，通常会使用包含 yield 表达式的生成器函数,这样可以将搜索过程代码和使用搜索结果代码解耦
- deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并 且这个队列已满的时候，最老的元素会自动被移除掉,相比列表更加的快捷优雅
- q = deque()   如 果你不设置最大队列大小，那么就会得到一个无限大小队列
- 队列两端插入或删除元素时间复杂度都是 O(1) ，而在列表的开头插入或删除元 素的时间复杂度为 O(N) 