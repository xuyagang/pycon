class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    
    # *args中保留了被装饰函数的参数
    def __call__(self, *args):
        self.func(*args)
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))

@tracer
def spam(a,b,c):
    print(a,b,c)

spam(1,2,3)
spam('a', 'b', 'c')
spam(4,5,6)