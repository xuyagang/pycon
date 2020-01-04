# global name/attribute
x = 11
def f():
    # access global x
    print(x)
def g():
    # local variable
    x = 22
    print(x)
class C:
    # class attribute
    x = 33
    def m(self):
        # local variable in method
        x = 44
        # instance attribute
        self.x = 55

if __name__ == '__main__':
    print(x)
    f()
    g()
    print(x)

    obj = C()
    print(obj.x)

    # obj.m()
    print(obj.x)
    print(C.x)
'''
11
11
22
11
33
33
33
'''