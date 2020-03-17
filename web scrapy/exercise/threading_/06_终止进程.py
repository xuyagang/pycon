import multiprocessing
import time

def process():
    print('Starting')
    time.sleep(5)
    print('Finished')

if __name__ == '__main__':
    p = multiprocessing.Process(target=process)
    print('Before:', p, p.is_alive())
    
    p.start()
    print('During:', p, p.is_alive())

    p.terminate()
    print('Terninate:', p, p.is_alive())

    p.join()
    print('Joined:', p, p.is_alive())

'''
Before: <Process(Process-1, initial)> False
During: <Process(Process-1, started)> True
Terninate: <Process(Process-1, started)> True
Joined: <Process(Process-1, stopped[SIGTERM])> False

这里有一个值得注意的地方，在调用 terminate 方法之后，
我们用 is_alive 方法获取进程的状态发现依然还是运行状态。
在调用 join 方法之后，is_alive 方法获取进程的运行状态才变为终止状态。

所以，在调用 terminate 方法之后，记得要调用一下 join 方法，
这里调用 join 方法可以为进程提供时间来更新对象状态，用来反映
出最终的进程终止效果。
'''