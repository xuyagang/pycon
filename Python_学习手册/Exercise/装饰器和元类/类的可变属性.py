class C:
    # 类属性
    shared = []
    def __init__(self):
        # 实例属性
        self.perobj = []

x = C()
y = C()
print(y.shared, y.perobj)
# >>>[] []
x.shared.append('spam')
x.perobj.append('spam-s')
print(x.shared, x.perobj)
# ['spam'] ['spam-s']
print(y.shared, y.perobj)
# ['spam'] []