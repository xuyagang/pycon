# 变量的数量必须跟序列元素的数量一致
p = (4,5)
x,y = p
print(x,y)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, (year, mon, day) = data
print(shares)



# 变量个数和序列元素个数不匹配会产生一个异常
# a,b = data
# print(a)
# ValueError: too many values to unpack (expected 2)


# 解压赋值可作用在任何可迭代对象上面（列表，元组，字符串，生成器，迭代器，文件对象）
s = 'hello'
a,b,c,d,e = s
print(a,c)


# 可使用_做为占位变量，丢弃不需要的值
# 须保证占位变量在其他地方没有被使用
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_,shares,price,_ = data
print(price)
