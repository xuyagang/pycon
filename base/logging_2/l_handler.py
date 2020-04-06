# 首先导入日志类
import logging

# 构造日志对象
logger = logging.getLogger(__name__)
# 配置
logger.setLevel(logging.INFO)
# 创建日志处理器
# logging.FileHandler(filename, mode='a', encoding=None, delay=False) 
handler = logging.FileHandler('output.log')
# 创建格式化对象,指定日志记录输出的具体格式
# asctime, name(logger name), levelname, message
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 给处理器绑定格式器
handler.setFormatter(formatter)
# 给日志对象绑定处理器
logger.addHandler(handler)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')