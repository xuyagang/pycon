import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# logger 与 handler是一对多的关系
# 一个logger可以有多种输出方式（handler）

# streamHandler
stream_handler = logging.StreamHandler(sys.stdout)
# 可以对handler配置级别
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

# FileHandler
file_handler = logging.FileHandler('output.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# HttpHandler
# 暂时略过

# log
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
