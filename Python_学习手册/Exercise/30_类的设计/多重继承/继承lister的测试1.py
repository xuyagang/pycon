import lister
class C(lister.ListInstance):
    pass
x = C()
x.a = 1
x.b = 2
x.c = 3
print(x)
print(dir(x))