#encoding: utf-8

from models.BaseModel import BaseModel

class StockModel(BaseModel):
	"""股票信息模型"""
	def __init__(self):
		super(StockModel, self).__init__()
		self.id = None
		self.stockId = None						# 股票ID
		self.openPrice = 0						# 开盘价
		self.yesterdayClosePrice = 0			# 昨日收盘价
		self.curPrice = 0						# 当前价
		self.averagePrice = 0					# 均价
		self.high = 0							# 最高价
		self.low = 0							# 最低价
		self.tradeVolume = 0					# 成交量
		self.tradeValue = 0						# 成交额
		self.turnoverRate = 0					# 换手率
		self.marketValue = 0					# 市值
		self.circulationValue = 0				# 流通值
		self.pb = 0								# 市净率
		self.pe = 0								# 市盈率
		self.buyVolume = 0						# 外盘
		self.sellVolume = 0						# 内盘
		self.amountRatio = 0					# 量比
		self.entrustRatio = 0					# 委比
		self.superFlowIn = 0					# 超大单流入
		self.superFlowOut  = 0					# 超大单流出
		self.bigFlowIn = 0						# 大单流入
		self.bigFlowOut = 0						# 大单流出
		self.middleFlowIn = 0					# 中单流入
		self.middleFlowOut = 0					# 中单流出
		self.littleFlowIn = 0					# 小单流入
		self.littleFlowOut = 0					# 小单流出
		self.updateDate = None					# 股票数据更新日期

	@staticmethod
	def stockModelFromList(list):
		stockModel = StockModel()
		try:
			stockModel.openPrice = float(list[29])
			stockModel.yesterdayClosePrice = float(list[23])
			stockModel.curPrice = float(list[26])
			stockModel.averagePrice = float(list[44])
			stockModel.high = float(list[30])
			stockModel.low = float(list[31])
			stockModel.tradeVolume = int(list[36])
			stockModel.tradeValue = float(list[37])
			stockModel.turnoverRate = float(list[34]) * 0.01
			stockModel.marketValue = float(list[40])
			stockModel.circulationValue = float(list[41])
			stockModel.pb = float(list[39])
			stockModel.pe = float(list[38])
			stockModel.buyVolume = int(list[46])
			stockModel.sellVolume = int(list[45])
			stockModel.amountRatio = float(list[35])
			stockModel.entrustRatio = float(list[42]) * 0.01
		except Exception, e:
			raise e
		finally:
			return stockModel
