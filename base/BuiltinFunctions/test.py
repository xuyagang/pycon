# class absTest:
#     def __init__(self, x):
#         self.x = x

#     def __abs__(self):
#         print('调用定制的__abs__:%d' % abs(self.x))

# abstest = absTest(-123)
# abs(abstest)

def test (a,b):
    return a and b 
a = test(5,3)
print(a)