from multiprocessing import Process, Lock, Semaphore, Queue
from random import random
import time


def consumer(buffer, empty, full, lock):
    while True:
        # print(f'full:{full}')
        full.acquire()
        lock.acquire()
        print(f'consumer get {buffer.get()}')
        time.sleep(1)
        lock.release()
        empty.release()
        # print(f'empty:{empty}')

def producer(buffer, empty, full, lock):
    while True:
        # print(f'empty:{empty}')
        empty.acquire()
        lock.acquire()
        num = random()
        print(f'Producer put {num}')
        buffer.put(num)
        time.sleep(1)
        lock.release()
        full.release()
        # print(f'full:{full}')

if __name__ == "__main__":
    buffer = Queue(10)
    empty = Semaphore(2)
    full = Semaphore(1)
    lock = Lock()

    p = Process(target=producer, args=[buffer, empty, full, lock])
    c = Process(target=consumer, args=[buffer, empty, full, lock])
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')