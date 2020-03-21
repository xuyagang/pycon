from multiprocessing import Process, Semaphore
import time
import random

def grid(i,sem):
    sem.acquire()
    print(f'{i} 放入格子')
    time.sleep(1)
    print(f'{i} 拿出格子')
    sem.release()
    
if __name__ == "__main__":
    sem = Semaphore(3)
    for i in range(20):
        Process(target=grid, args=[i, sem]).start()