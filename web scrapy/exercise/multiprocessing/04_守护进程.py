from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop
    
    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'Pid: {self.pid} LoopCount: {count}')

if __name__ == '__main__':
    for i in range(2,5):
        p = MyProcess(i)
        # 主进程会直接结束，同时终止所有子进程的运行
        p.daemon = True
        p.start()

print('Main Process Ended')

'''
可以有效防止无控制地生成子进程。这样的写法可以让我们在主进程
运行结束后无需额外担心子进程是否关闭，避免了独立子进程的运行
'''