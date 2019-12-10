class rec: pass

# 没有写任何方法，所以我们需要无操作的pass语句
# 可通过赋值变量名给类增加属性
rec.name = 'Bob'
rec.age = 40
print('hello')

# 创建两个实例
x = rec()
y = rec()
print(x.name, y.name)

# 实例并没有属性，它们只是从类对象取出name属性
# 如果把一个属性赋值给一个实例，就会在对象内创建（或修改）该属性
# 属性赋值运算只会影响属性赋值所在对象
x.name = 'adam'
print(rec.name, x.name, y.name)

print(rec.__dict__)
print(x.__dict__.keys())
print(y.__dict__.keys())

print(x.__class__)


print(rec.__bases__)


def upperName(self):
    print(self.name.upper())
print('_'*7)
print(upperName(x))

rec.method = upperName

x.method()
y.method()
rec.method(x)