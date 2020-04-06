import logging

# 创建记录器
# __name__ = '__main__'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建处理器
handler = logging.FileHandler('logging_stepbystep_config_output.log',mode='a',encoding=None, delay=False)
# 创建格式器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              datefmt='%Y/%m/%d %H:%M:%S',
                              style='%')
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
handler.set_name('output-log')

# 给记录器添加处理器
logger.addHandler(handler)

try:
    result = 10 / 0
except:
    logger.error('Faild to get result', exc_info=0)
