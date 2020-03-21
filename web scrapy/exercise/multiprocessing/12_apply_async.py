# apply_async 是异步非阻塞的
# 不用等待当前进程执行完毕，随时根据系统调度来进行进程切换
from multiprocessing import Pool
import time

def say(msg):
    print(f'msg :{msg}')
    time.sleep(2)
    print('end')
    

if __name__ == '__main__':
    print('Main Process start')
    pool = Pool(3)
    print('start to execute:')
    for i in range(3):
        pool.apply_async(say, [i])
    # 异步非阻塞的apply_async，需要加join让主进程等待子进程执行完毕
    pool.close()
    pool.join()
    print('Main process ended')