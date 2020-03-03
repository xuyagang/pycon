'''
import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level = logging.DEBUG)
# 每次运行，将日志信息追加写入日志文件
logging.debug('This message should go to the log file3')
# 查看日志文件
with open(LOG_FILENAME,'rt') as f:
    body = f.read()
print(body)
'''


'''
# 旋转日志文件

# 日志回滚的意思为：比如日志文件是chat.log，当chat.log达到指定的大小之后，
# RotatingFileHandler自动把文件改名为chat.log.1。不过，如果chat.log.1已
# 经存在，会先把chat.log.1重命名为chat.log.2。最后重新创建 chat.log，继
# 续输出日志信息。【这样保证了chat.log里面是最新的日志】

# 每次运行文件都创建新的日志文件，可使用 RotatingFileHandler
# 自动创建文件，同时保留原来的日志文件
import glob
import logging 
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# logging.getLogger(name)获取logger对象，如果不指定name则返回root对象，
# 多次使用相同的name调用getLogger方法返回同一个logger对象
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                               maxBytes=20,
                                               backupCount=5)
my_logger.addHandler(handler)

# log some messages
for i in range(20):
    my_logger.debug('i = %d' % i)

logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
    print(filename)

'''


# 将日志打印到屏幕
# import logging
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message') 



# # 配置日志级别，日志格式，输出位置
# import logging 
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d, %b, %Y, %H:%M:%S',
#                     filename='test.log',
#                     # 重写覆盖
#                     filemode='w')
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')



import logging

# 创建一个默认 logger
logger = logging.getLogger()

# 创建带名字的logger
logger1 = logging.getLogger('mylogger')
# 设置日志级别
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('mylogger')
logger2.setLevel(logging.INFO)

logger3 = logging.getLogger('mylogger.child1')
logger3.setLevel(logging.ERROR)

logger4 = logging.getLogger('mylogger.child1.child2')
logger4.setLevel(logging.INFO)

logger5 = logging.getLogger('mylogger.child1.child2.child3')
logger5.setLevel(logging.DEBUG)

# 创建一个handler, 用于写入日志文件(创建文件到当前路径)
# FileHandler(self, filename, mode='a', encoding=None, delay=False)
# delay为true时，文件直到emit方法被执行才会打开
fhandler = logging.FileHandler('file_handler_test.log','w')

# 创建一个handler, 用于输出到控制台
chandler = logging.StreamHandler()

# 定义handler的输出格式 formatter
# %(name)s Logger的名字
# def __init__(self, fmt=None, datefmt=None, style='%')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              datefmt='%a, %d, %b, %Y, %H:%M:%S')
fhandler.setFormatter(formatter)
chandler.setFormatter(formatter)

# 定义一个filter
# 定义了filter = logging.Filter('a.b.c'),并将这个Filter添加到了
# 一个Handler上，则使用该Handler的Logger中只有名字带a.b.c前缀的
# Logger才能输出其日志
# filter = logging.Filter('mylogger.child1.child2')
# fhandler.addFilter(filter)

# 给logger 添加handler
# logger.addFilter(filter)
logger.addHandler(fhandler)
logger.addHandler(chandler)

# logger1.addFilter(filter)
logger1.addHandler(fhandler)
logger1.addHandler(chandler)

logger2.addHandler(fhandler)
logger2.addHandler(chandler)

# logger3.addFilter(filter)
logger3.addHandler(fhandler)
logger3.addHandler(chandler)

# logger4.addFilter(filter)
logger4.addHandler(fhandler)
logger4.addHandler(chandler)

logger5.addHandler(fhandler)
logger5.addHandler(chandler)

# 记录日志信息
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')


logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')

logger3.debug('logger3 debug message')
logger3.info('logger3 info message')
logger3.warning('logger3 warning message')
logger3.error('logger3 error message')
logger3.critical('logger3 critical message')

logger4.debug('logger4 debug message')
logger4.info('logger4 info message')
logger4.warning('logger4 warning message')
logger4.error('logger4 error message')
logger4.critical('logger4 critical message')


logger5.debug('logger5 debug message')
logger5.info('logger5 info message')
logger5.warning('logger5 warning message')
logger5.error('logger5 error message')
logger5.critical('logger5 critical message')


