from streams import Processor
'''
class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
'''
class Uppercase(Processor):
    # 继承并重写converter方法
    def converter(self, data):
        return data.upper()

# 定义一个writer
class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())

if __name__ == '__main__':
    import sys

    obj = Uppercase(open('spam.txt'), sys.stdout)
    obj.process()
    Uppercase(open('spam.txt'), HTMLize()).process()