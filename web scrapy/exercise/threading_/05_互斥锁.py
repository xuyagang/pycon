import threading
import time
# 一个进程中多个线程是共享资源的，用全局count来计数
count = 0
# 声明多个线程，每个线程运行时都 + 1
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        global count
        temp = count + 1
        time.sleep(0.001)
        count = temp

threads = []
for _ in range(1000):
    thread = MyThread()
    # 下面两步没有必须的先后顺序
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
print(f'Final count:{count}')

# 最后的结果居然只有 69，而且多次运行或者换个环境运行结果是不同的
# 因为count这个值是共享的，每个线程都可以在执行temp=count这行代码时
# 拿到当前count的值，但是这些线程中的一些线程可能是并发或者并行执行的，
# 这就导致不同的线程拿到的可能是同一个 count 值，最后导致有些线程的
#  count 的加 1 操作并没有生效

# 如果多个线程同时对某个数据进行读取或修改，就会出现不可预料的结果。
# 为了避免这种情况，我们需要对多个线程进行同步，要实现同步，我们可
# 以对需要操作的数据进行加锁保护，这里就需要用到threading.Lock

# 加锁保护是什么意思呢？就是说，某个线程在对数据进行操作前，需要先加
# 锁，这样其他的线程发现被加锁了之后，就无法继续向下执行，会一直等待
# 锁被释放，只有加锁的线程把锁释放了，其他的线程才能继续加锁并对数据
# 做修改，修改完了再释放锁。这样可以确保同一时间只有一个线程操作数据，
# 多个线程不会再同时读取和修改同一个数据，这样最后的运行结果就是对的了。

#　修改代码为如下
import threading
import time

count = 0
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        lock.acquire()
        temp = count + 1
        time.sleep(0.001)
        count = temp
        lock.release()

# 声明一个lock对象，就是threading.lock的实例
lock = threading.Lock()
threads = []
for _ in range(1000):
    thread = MyThread()
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print(f'Final count: {count}')