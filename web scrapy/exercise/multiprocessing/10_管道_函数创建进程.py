from multiprocessing import Process, Pipe
import time

def consumer(pipe):
    
    pipe.send('consumer message')
    print(f'Consumer received: {pipe.recv()}')

def producer(pipe):
    
    pipe.send('Producer message')
    print(f'Producer received:{pipe.recv()}')

if __name__ == '__main__':
    pipe = Pipe()
    p = Process(target=producer, args=[pipe[0]])
    c = Process(target=consumer, args=[pipe[1]])
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()