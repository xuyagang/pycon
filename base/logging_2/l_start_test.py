import logging

# 设置Formatter主要包括两种方式，
# 一种是通过Formatter类构建Formatter实例，并将其绑定到特定的handler上；
# 一种是通过logging.basicConfig设置
# format是字符串格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# <RootLogger root (INFO)>
logger = logging.getLogger()
# <Logger __main__ (INFO)>
logger = logging.getLogger(__name__)
# 输出指定级别及以上的日志，默认loglevel是warning
logger.info('This is a log info')
logger.debug('This is a debug info')
logger.warning('Warning exists')
logger.info('Finish')
# 默认loglevel是warning，但logger.level输出0
print(logger.level)

print('-'*11)
logger.setLevel(logging.DEBUG)
logger.info('This is a log info')
logger.debug('This is a debug info')
logger.warning('Warning exists')
logger.info('Finish')
print(logger.level)