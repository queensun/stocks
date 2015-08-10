#encoding: utf-8

import logging
import logging.config

logging.config.fileConfig('log/log.ini')
logger = logging.getLogger('financeLogger')

# class Logger(object):
# 	"""Logger"""
	
# 	def __init__(self):
# 		super(Logger, self).__init__()

# 	@staticmethod
# 	def debug(msg):
# 		logger.debug(msg)

# 	@staticmethod
# 	def info(msg):
# 		logger.info(msg)

# 	@staticmethod
# 	def warning(msg):
# 		logger.warning(msg)

# 	@staticmethod
# 	def error(msg):
# 		logger.error(msg)

# 	@staticmethod
# 	def critical(msg):
# 		logger.critical(msg)