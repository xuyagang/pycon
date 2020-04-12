class wrapper:
    def __init__(self, object):
        # object 是所有类的基类
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace', attrname)
        print(attrname)
        return getattr(self.wrapped, attrname)

'''
>>> from delegation import wrapper
>>> x = wrapper([1,2,3])
>>> x.append(4)
Trace append
append
'''