def foo():
    print('starting...')
    while True:
        res = yield 4
        print('res:',res)

g = foo()

print(next(g))
print('*'*20)
print(next(g))
print(next(g))

'''
https://blog.csdn.net/mieleizhi0522/article/details/82142856/
程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g

直到调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环

程序遇到yield关键字，然后把yield想想成return,return了一个4之后，程序停止并没有执行赋值给res操作，
此时next(g)语句执行完成，所以输出的前两行（第一个是while上面的print的结果,第二个是return出的结果）
是执行print(next(g))的结果开始执行下面的print(next(g)),这个时候和上面那个差不多，不过不同的是，
这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作，这时候要注意，这个时
候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），所以这个
时候res赋值是None,所以接着下面的输出就是res:None

程序会继续在while里执行，又一次碰到yield,这个时候同样return 出4，然后程序停止
'''
