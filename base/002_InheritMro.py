'''
新式类的搜索方法采用了“广度优先”的方式查找属性
新式类有__mro__属性

'''

# MRO算法--生成一个列表保存继承顺序表
# I>G>D>E>H>F>C>B>A
class A:
    def test(self):
        print('frome A')

class B(A):
    def test(self):
        print('frome B')

class C(A):
    def test(self):
        print('frome C')

class D(B):
    def test(self):
        print('frome D')

class E(C,B):
    def test(self):
        print('frome E')

class F(C):
    def test(self):
    	super(self).test()
    	print('frome F')

class G(D,E):
	def test(self):
		print('from G')

class H(F):
	def test(self):
		print('from H')

class I(G,H):
	def test(self):
		print('from I')

# 使用方法一
print(I.__mro__)
# 使用方法二
print()


# I>G>D>B>H>F>C>A
# class A:
#     def test(self):
#         print('frome A')

# class B(A):
#     def test(self):
#         print('frome B')

# class C(A):
#     def test(self):
#         print('frome C')

# class D(B):
#     def test(self):
#         print('frome D')

# class F(C):
#     def test(self):
#     	super(self).test()
#     	print('frome F')

# class G(D):
# 	def test(self):
# 		print('from G')

# class H(F):
# 	def test(self):
# 		print('from H')

# class I(G,H):
# 	def test(self):
# 		print('from I')

# print(I.__mro__)