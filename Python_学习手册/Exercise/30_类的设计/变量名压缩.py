# # __例1__：假设一个程序员编写一个类，他认为属性名称X是在该实例中，在类的方法中，变量被设定，然后取出
# class C1:
#     def meth1(self): self.X = 88             # I assume X is Mine
#     def meth2(self): print(self.X)
# # __例2__: 另一个程序员独立作业，他对类也有同样的假设
# class C2:
#     def metha(self): self.X = 99             # Me too
#     def methb(self): print(self.X)
# # 这两个类各行其事，当混合在相同类树中，问题就出现了
# class C3(C1, C2):
#     def test(self):
#         self.X = 9
#         print(C1().meth2(), C2().methb())



class C1:
    def meth1(self): self.__X = 88
    def meth2(self): print(self.__X)
class C2:
    def metha(self): self.__X = 99
    def methb(self): print(self.__X)
class C3(C1, C2): pass

I = C3()
print(I.__dict__)
I.meth1(); I.meth2()
print(I.__dict__)
I.metha(); I.methb()
print(I.__dict__)