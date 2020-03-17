'''
一个线程被设置为守护线程，那这个线程是“不重要的”
如果主线程结束了而该守护线程还没有运行完，它将被强制结束
python中通过 setDeamon 来将某个线程设置为守护线程
'''

import threading
import time

def target(second):
    print(f'Threading {threading.current_thread().name} is running')
    print(f'Threading {threading.current_thread().name} sleep{second} s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')


ts = time.time()
print(f'Threading {threading.current_thread().name} is running')
# 创建一个线程
t1 = threading.Thread(target=target,args=[2])
# 启动线程
t1.start()
# 正常主线程不会等待子线程运行完毕，而自己先结束
# 加了join,让主线程等待子线程运行完毕再终止
# join方法可加入等待时限参数
t1.join()
t2 = threading.Thread(target=target, args=[5])
# 设置线程2为守护线程，主线程结束时会将其强制结束
# setDeamon必须再启动线程start之前设置
t2.setDaemon(True)
# t2线程不调用join方法，将不会看到它的结束信息
# 如果对一个线程调用了join方法，不管其是否为守护线程，主线程都会等待其运行结束
t2.start()
# join方法必须再start之后
t2.join()
print(f'Threading {threading.current_thread().name} is ended')
te = time.time()
print(f'耗时：{int(te - ts)}')