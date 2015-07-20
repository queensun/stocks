#encoding: utf-8

from models.BaseModel import BaseModel;

class StockTradeModel(BaseModel):
	"""股票交易模型"""
	def __init__(self, tradeId = None, stockId = None, tradeTime = None, tradePrice = None, tradeVolume = None, trend = None):
		super(StockTradeModel, self).__init__()
		self.id = tradeId
		self.stockId = stockId
		self.tradeTime = tradeTime
		self.tradePrice = tradePrice
		self.tradeVolume = tradeVolume
		self.trend = trend
