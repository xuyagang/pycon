from multiprocessing import Pool
import time

def func(index):
    print(f'Start Process: {index}')
    time.sleep(2)
    print(f'End process: {index}')

if __name__ == '__main__':
    st = time.time()
    pool = Pool(processes=3)
    for i in range(5):
        pool.apply_async(func, args=[i])
    print('Main Process started')
    pool.close()
    pool.join()
    print(f'总耗时：{int(time.time()-st)} s')
    print('Main Process Ended')
