from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'Pid: {self.pid} Count: {count}')

processes = []
if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        processes.append(p)
        p.daemon = True
        p.start()
    for p in processes:
        p.join(1)

'''
默认情况下，join 是无限期的。也就是说，如果有子进程没有
运行完毕，主进程会一直等待。这种情况下，如果子进程出现
问题陷入了死循环，主进程也会无限等待下去。怎么解决这个
问题呢？可以给 join 方法传递一个超时参数，代表最长等待
秒数。如果子进程没有在这个指定秒数之内完成，会被强制返
回，主进程不再会等待。也就是说这个参数设置了主进程等待
该子进程的最长时间。(该参数对于非守护进程无效，会一直
等待执行完成)
'''