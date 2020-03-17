# 需要使用Thread类创建线程
# target参数为运行的函数名，args为函数的参数
import threading
import time

# 声明一个任务，接受一个参数
def target(second):
    # 线程的名字我们通过 threading.current_thread().name 来获取
    # 主线程的话，其值就是 MainThread，如果是子线程的话，其值就是 Thread-*
    print(f'Threading{threading.current_thread().name} is running')
    print(f'Threading{threading.current_thread().name} sleep {second} s')
    time.sleep(second)
    print(f'Threading{threading.current_thread().name} is ended')

print(f'Threading {threading.current_thread().name} is running')
for i in [1,4]:
    # 创建线程，传入参数（args 以列表的形式传递）
    thread = threading.Thread(target=target,args=[i])
    # 开始线程的运行
    thread.start()
print(f'Threading {threading.current_thread().name} is ended')


'''
观察结果我们可以发现，这里一共产生了三个线程，分别是主线程 MainThread 
和两个子线程 Thread-1、Thread-2

主线程首先运行结束，紧接着 Thread-1、Thread-2 才接连运行结束，分别间隔
了 1 秒和 4 秒。这说明主线程并没有等待子线程运行完毕才结束运行，而是直
接退出了
'''