from multiprocessing import Pool
import time


# apply 方法是阻塞的
# 就是等待当前子进程执行完毕在执行下一个进程
# 这样好像跟单进程串行执行没什么区别了
def say(msg):
    print(f'msg :{msg}')
    time.sleep(2)
    print('end')
    

if __name__ == '__main__':
    print('Main Process start')
    pool = Pool(3)
    print('start to execute:')
    for i in range(3):
        pool.apply(say, [i])
    print('Main process ended')