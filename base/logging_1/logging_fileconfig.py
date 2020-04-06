import logging
import logging.config

# fileConfig(fname, defaults=None, disable_existing_loggers=True)
logging.config.fileConfig('logging.conf', disable_existing_loggers=True)

logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


'''
fileConfig文件的解读主要基于configparser，它必须包含 [loggers], 
[handlers] 和 [formatters] section。这是一个比较老的API，不支持配置Filter，
估计后面也不会更新了，所以建议大家使用dictConfig。
'''