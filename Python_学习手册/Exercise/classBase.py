class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

# 通过继承进行定制
class SecondClass(FirstClass):
    def display(self):
        # 定义了不同格式的打印，取代了与FirstClass中同名的属性
        print('Current value = {}'.format(self.data))

# SecondClass覆盖了FirstClass中的display
# 我们把这种较低处发生的重新定义的、取代属性的动作称为重载
# 结果就是SecondClass改变了继承方法display的行为，把FirstClass特定化了
z = SecondClass()
z.setdata(111)
z.display()


class ThridClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self,other):
        return ThridClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other

print('-'*15)
# 创建实例时，传入类名括号里的变量是 __init__ 初始化函数的变量
# __init__被调用
a = ThridClass('abc')
# 调用继承方法
a.display()
# 调用 __str__ 函数
print(a)
# 创建新的实例
b = a + 'xyz'
# 调用继承方法
b.display()
print(b)
a.mul(3)
print(a)