#encoding: utf-8

from models.BaseModel import BaseModel

class StockBaseModel(BaseModel):
	"""股票基础模型，只包括股票代码和股票名称"""
	def __init__(self, stockId = None, stockCode = None, stockName = None, market = None):
		super(StockBaseModel, self).__init__()
		self.id = stockId
		self.stockCode = stockCode
		self.stockName = stockName
		self.market = market

	def getEastMoneyStockCode(self):
		"""返回东方财富网股票的唯一标识"""
		marketId = ''
		if self.market == 'sh':
			marketId = '1'
		elif self.market == 'sz':
			marketId = '2'
		return self.stockCode + marketId
