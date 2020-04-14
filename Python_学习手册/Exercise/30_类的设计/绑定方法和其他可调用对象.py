class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3
x = Number(2)
y = Number(3)
z = Number(4)
# 调用绑定对象
print(x.double(), y.double(), y.triple(), z.double())
#  4 6 9 8

bound = x.double
print(bound.__self__, bound.__func__)
print(bound.__self__.base)
# <__main__.Number object at 0x00000158466FE588> <function Number.double at 0x00000158466C6828>
# 2


def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, val):
        self.val = val
    def __call__(self, arg):
        return self.val + arg
class Product:
    def __init__(self, val):
        self.val = val
    def method(self, arg):
        return self.val * arg 
sobj = Sum(2)
pobj = Product(3)
actions = [square, sobj, pobj.method]
for act in actions:
    print(act(5))