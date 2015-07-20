#encoding: utf-8

import httplib
from storages.stock.StockStorage import StockStorage

class StockService(object):
	"""docstring for StockService"""
	def __init__(self):
		super(StockService, self).__init__('')

	@staticmethod
	def getStockBaseModelByCode(stockCode):
		return StockStorage.getStockBaseModelByCode(stockCode)

	@staticmethod
	def getAllStockBaseModels():
		return StockStorage.getAllStockBaseModels()

	@staticmethod
	def getAllStockCategoryModels():
		return StockStorage.getAllStockCategoryModels()
