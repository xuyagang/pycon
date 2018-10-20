# 1.若函数内部有和全局变量的同名变量被赋值，则函数内部的为局部变量，函数外的为全局变量
	# 此时函数内和全局变量同名的局部变量一定要先赋值再调用，否则会报错，如例1所示
	# （UnboundLocalError: local variable 'a' referenced before assignment）

# 例1
# def fun():
# 	print(a)
# 	a = 'xyz'
# 	print(a)

# a = 'abc'
# fun()

# 结果：
# 直接报错
# -------------------------------------------
# 例2
# 作为参数传入后，没有了局部变量，变成了全局变量在函数内的重新赋值
# def fun(a):
# 	a = '123'
# 	print(a)
# 	a = 'abc'
# 	print(a)
# a = 'xyz'
# fun(a)

# 结果：
# 123
# abc
# -------------------------------------------


# 2.当函数内有一变量名和某个外部函数同名，在该函数内部调用外部同名函数可使用globals,
	# globals() 和 locals() 提供了基于字典的访问全局和局部变量的方式
# def a():
# 	return 'it is a'
# 	# print('it is a')
# def fun():
# 	a = 'it is fun'
# 	f1 = globals()['a']()
# 	print(a)
# 	print(f1)
# 	print(globals())
# 	print(locals())
# fun()