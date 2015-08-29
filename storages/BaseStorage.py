#encoding: utf-8
import MySQLdb

class BaseStorage(object):
	"""docstring for BaseStorage"""
	db = MySQLdb.connect(host="192.168.1.5", user="finance", passwd="finance_fb3efc4", db="finance", charset="utf8")
	def __init__(self):
		super(BaseStorage, self).__init__()
