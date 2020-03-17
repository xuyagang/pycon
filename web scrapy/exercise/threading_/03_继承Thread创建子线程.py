import threading
import time


class MyThread(threading.Thread):
    def __init__(self, second):
        # 重用父类的方法初始化
        threading.Thread.__init__(self)
        self.second = second

    def run(self):
        print(f'Threading{threading.current_thread().name} is running')
        print(f'Threading{threading.current_thread().name} sleep {self.second} s')
        time.sleep(self.second)
        print(f'Threading{threading.current_thread().name} is ended')

print(f'Threading {threading.current_thread().name} is running')
# 创建一个列表存储线程对象
threads = []
for i in [1,4]:
    # 创建线程，传入参数（args 以列表的形式传递）
    thread = MyThread(i)
    # 添加线程到列表中
    threads.append(thread)
    # 开始线程的运行
    thread.start()
# 对线程对象调用join方法，让主线程等待子线程运行结束再终止
for thread in threads:
    # Wait until the thread terminates
    thread.join()
print(f'Threading {threading.current_thread().name} is ended')