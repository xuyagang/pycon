import multiprocessing
import time

def process(index):
    time.sleep(index)
    print(f'Process: {index}')

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=[i])
        p.start()
    print(f'CPU number:{multiprocessing.cpu_count()}')
    # 通过 active_children 获取到了当前正在活跃运行的进程列表
    for p in multiprocessing.active_children():
        # 利用 pid和name来获取进程号和进程名称
        print(f'Child process name: {p.name} id:{p.pid}')
    print('Process Ended')