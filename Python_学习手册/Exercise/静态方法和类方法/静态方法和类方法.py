class Methods:
    def imeth(self,x):
        print(self, x)
    def smeth(x):
        print(x)
    def cmeth(cls,x):
        print(cls, x)
    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)
# make an instance
obj = Methods()

# 常规实例调用方式,第一个参数自动传入
obj.imeth(1)
# 等价方法，类调用，手动传入实例参数
Methods.imeth(obj, 2)

# 静态方法
Methods.smeth(3)
obj.smeth(4)

# # 类方法
Methods.cmeth(4)
obj.cmeth(5)