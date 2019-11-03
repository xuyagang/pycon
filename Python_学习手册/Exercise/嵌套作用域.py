x = 99

def f1():
	x = 88
	def f2():
		print(x)
	# f2是f1本地作用域中的变量，f2是一个临时函数
	f2()

# f1()

def ff():
	x = 88
	def fff():
		print(x)
	return fff

action = ff()
action()