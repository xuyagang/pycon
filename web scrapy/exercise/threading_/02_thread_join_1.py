import threading
import time

# https://www.cnblogs.com/cnkai/p/7504980.html
def run():
    time.sleep(2)
    print('当前线程：{}'.format(threading.current_thread().name))
    time.sleep(2)

if __name__ == "__main__":
    st = time.time()
    print('主线程：{}'.format(threading.current_thread().name))
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)
    for t in thread_list:
        t.setDaemon(True)
        t.start()
        print('---')
    for t in thread_list:
        t.join()

    print('总耗时：{}'.format(int(time.time() - st)))