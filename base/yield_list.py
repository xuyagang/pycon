def foo(num):
    print('starting')
    while num < 100:
        num += 1
        yield num
        
for i in foo(0):
    print(i)