'''
Climb inheritance trees using namespace links,
displaying higher superclasses with indentation
'''

def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    # 遍历类的基类
    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)

def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def selftest():
    class A:        pass
    class B(A):     pass
    class C(A):     pass
    class D(B,C):   pass
    class E:        pass
    class F(D,E):   pass
    instancetree(B())
    instancetree(F())

if __name__ == '__main__':
    selftest()

'''
Tree of <__main__.selftest.<locals>.B object at 0x000001D27B3D5B70>
...B
......A
.........object
Tree of <__main__.selftest.<locals>.F object at 0x000001D27B3D5B70>
...F
......D
.........B
............A
...............object
.........C
............A
...............object
......E
.........object
'''
