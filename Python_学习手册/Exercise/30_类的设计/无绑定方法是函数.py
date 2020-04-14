class Selfless:
    def __init__(self, data):
        self.data = data
    def selfless(arg1, arg2):
        return arg1 + arg2
    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2

X = Selfless(2)
print(X.normal(3,4))
# 9
print(Selfless.normal(X, 3, 4))
# 9
print(Selfless.selfless(3,4))
# 7
# 非绑定方法通过实例调用会报错
# X.selfless(3,4)
# 类调用绑定方法（不传实例）会报错，
Selfless.normal(3,4)