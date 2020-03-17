import multiprocessing

def process(index):
    print(f'Process: {index}')

if __name__ == '__main__':
    for i in range(5):
        # 要传入参数名，args:Iterable[Any]
        # 单个元素的agrs要么是list形式，要么是元组，记得加逗号
        p = multiprocessing.Process(target=process, args=[i], name=f'线程-{i}')
        p.start()
        print(p.name)