#coding=utf-8
####定义单例的日志logger模块

import  logging
import logging.config
import os


class logControl:


	logging.config.fileConfig(os.path.join(os.path.dirname(__file__),r"logger.conf"))


	##create logger
	@staticmethod
	def getLogger():
		logger = logging.getLogger('run')

		return logger