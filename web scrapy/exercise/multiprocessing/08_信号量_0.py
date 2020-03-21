import threading
import time

sem = threading.Semaphore(3)

class DemoThread(threading.Thread):
    def run(self):
        print('{} is waiting semaphone'.format(self.name))
        sem.acquire()
        print('{} acquired semaphore({})'.format(self.name, time.ctime()))
        time.sleep(3)
        print('{} release semaphone.'.format(self.name))
        sem.release()

if __name__ == "__main__":
    threads = []
    for i in range(4):
        threads.append(DemoThread(name='Thread-{}'.format(str(i))))
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
