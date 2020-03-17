'''
想要主线程等待子线程运行完毕之后才退出，
可以让每个子线程对象都调用下 join 方法
'''

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
# 创建一个列表存储线程对象
threads = []
for i in [1,4]:
    # 创建线程，传入参数（args 以列表的形式传递）
    thread = threading.Thread(target=target,args=[i])
    # 添加线程到列表中
    threads.append(thread)
    # 开始线程的运行
    thread.start()
# 对线程对象调用join方法，让主线程等待子线程运行结束再终止
for thread in threads:
    # Wait until the thread terminates
    thread.join()
print(f'Threading {threading.current_thread().name} is ended')