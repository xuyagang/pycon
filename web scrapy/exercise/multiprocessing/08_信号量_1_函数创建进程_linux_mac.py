from multiprocessing import Process, Semaphore, Lock, Queue
import time

buffer = Queue(10)
empty = Semaphore(3)
full = Semaphore(0)
lock = Lock()

def consumer():
    global buffer, empty, full, lock
    while True:
        full.acquire()
        lock.acquire()
        buffer.get()
        print('Consumer pop an element')
        time.sleep(1)
        lock.release()
        empty.release()

def producer():
    global buffer, empty, full, lock
    while True:
        empty.acquire()
        lock.acquire()
        buffer.put(1)
        print('Producer append an element')
        time.sleep(1)
        lock.release()
        full.release()

if __name__ == '__main__':
    p = Process(target= producer)
    c = Process(target=consumer)
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')