from multiprocessing import Process, Semaphore, Lock, Queue
import time

def consumer(buffer, empty, full, lock):
    while True:
        full.acquire()
        lock.acquire()
        buffer.get()
        print('Consumer pop an element')
        time.sleep(1)
        lock.release()
        empty.release()

def producer(buffer, empty, full, lock):
    while True:
        empty.acquire()
        lock.acquire()
        buffer.put(1)
        print('Producer append an element')
        time.sleep(1)
        lock.release()
        full.release()


if __name__ == '__main__':
    buffer = Queue(10)
    empty = Semaphore(2)
    full = Semaphore(0)
    lock = Lock()
    
    p = Process(target=producer, args=[buffer, empty, full, lock])
    c = Process(target=consumer, args=[buffer, empty, full, lock])
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')
