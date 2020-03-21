import time
import random
from multiprocessing import Process,Semaphore
def ktv(person,sem):
    sem.acquire()
    print("%s进入了ktv,正在唱歌"%(person))
    time.sleep(2)
    print("%s唱完了，离开了ktv"%(person))
    sem.release()

if __name__ == "__main__":
    sem = Semaphore(3)
    for i in range(10):
        p = Process(target=ktv,args=("person%s"%(i),sem))
        p.start()