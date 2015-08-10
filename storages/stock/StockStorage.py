#encoding: utf-8

import MySQLdb
from storages.BaseStorage import BaseStorage
from models.stock.StockBaseModel import StockBaseModel
from models.stock.StockCategoryModel import StockCategoryModel
from models.stock.StockTradeModel import StockTradeModel

class StockStorage(BaseStorage):
	"""股票存储相关接口"""
	def __init__(self):
		super(StockStorage, self).__init__()

	@staticmethod
	def saveStockBaseModel(stockBaseModel):
		cursor = BaseStorage.db.cursor()
		try:
			sql = 'insert into stocks(stockCode, stockName, market) values("%s", "%s", "%s")'
			cursor.execute(sql % (stockBaseModel.stockCode, stockBaseModel.stockName, stockBaseModel.market))
			BaseStorage.db.commit()
		except Exception, e:
			BaseStorage.db.rollback()
			raise e
		finally:
			cursor.close()

	@staticmethod
	def getStockBaseModelByCode(stockCode):
		cursor = BaseStorage.db.cursor();
		try:
			cursor.execute('select * from stocks where stockCode="%s"' % (stockCode))
			result = cursor.fetchone()
			stockBaseModel = StockBaseModel(result[0], result[1], result[2], result[3])
			return stockBaseModel
		except Exception, e:
			raise e
		finally:
			cursor.close()

	@staticmethod
	def getAllStockBaseModels():
		l = []
		cursor = BaseStorage.db.cursor();
		try:
			cursor.execute('select * from stocks')
			rows = cursor.fetchall()
			for row in rows:
				stockBaseModel = StockBaseModel(row[0], row[1], row[2], row[3])
				l.append(stockBaseModel)
		except Exception, e:
			raise e
		finally:
			cursor.close()
			return l

	@staticmethod
	def saveStockModel(stockModel):
		cursor = BaseStorage.db.cursor()
		try:
			sql = 'insert into stocks_daily(stockId, openPrice, yesterdayClosePrice, curPrice, \
				averagePrice, high, low, tradeVolume, tradeValue, turnoverRate, marketValue, \
				circulationValue, pb, pe, buyVolume, sellVolume, amountRatio, entrustRatio, \
				superFlowIn, superFlowOut, bigFlowIn, bigFlowOut, middleFlowIn, middleFlowOut, \
				littleFlowIn, littleFlowOut, updateDate) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "%s")'
			cursor.execute(sql % (stockModel.stockId, stockModel.openPrice, stockModel.yesterdayClosePrice,
				stockModel.curPrice, stockModel.averagePrice, stockModel.high, stockModel.low,
				stockModel.tradeVolume, stockModel.tradeValue, stockModel.turnoverRate, stockModel.marketValue,
				stockModel.circulationValue, stockModel.pb, stockModel.pe, stockModel.buyVolume, 
				stockModel.sellVolume, stockModel.amountRatio, stockModel.entrustRatio,
				stockModel.superFlowIn, stockModel.superFlowOut, stockModel.bigFlowIn, stockModel.bigFlowOut, 
				stockModel.middleFlowIn, stockModel.middleFlowOut, stockModel.littleFlowIn, 
				stockModel.littleFlowOut, stockModel.updateDate))
			BaseStorage.db.commit()
		except Exception, e:
			BaseStorage.db.rollback()
			raise e
		finally:
			cursor.close()

	@staticmethod
	def saveStockCategoryModel(stockCategoryModel):
		cursor = BaseStorage.db.cursor()
		try:
			sql = 'insert into stock_categories(categoryName, categoryBy) values("%s", %s)'
			print sql
			cursor.execute(sql % (stockCategoryModel.categoryName, stockCategoryModel.categoryBy))
			BaseStorage.db.commit()
		except Exception, e:
			BaseStorage.db.rollback()
			raise e
		finally:
			cursor.close()

	@staticmethod
	def getAllStockCategoryModels():
		l = []
		cursor = BaseStorage.db.cursor()
		try:
			cursor.execute('select * from stock_categories')
			rows = cursor.fetchall()
			for row in rows:
				stockCategoryModel = StockCategoryModel(row[0], row[1], row[2])
				l.append(stockCategoryModel)
		except Exception, e:
			raise e
		finally:
			cursor.close()
			return l

	@staticmethod
	def saveStockCategoryRelation(stockBaseModel, stockCagegoryModel):
		"""保存股票与所属板块关系"""
		cursor = BaseStorage.db.cursor()
		try:
		    cursor.execute('insert into stock_category_relationships(stockId, categoryId) values(%s, %s)' \
		    		 % (stockBaseModel.id, stockCagegoryModel.id))
		    BaseStorage.db.commit()
		except Exception, e:
			BaseStorage.db.rollback()
			raise e
		finally:
			cursor.close()
			pass
	
	@staticmethod
	def saveStockTradeModel(stockTradeModel):
		"""保存股票交易数据"""	
		cursor = BaseStorage.db.cursor()
		try:
		    cursor.execute('insert into stock_trades(stockId, tradeTime, tradePrice, tradeVolume, trend) values(%s, "%s", %s, %s, %s)' \
		    		 % (stockTradeModel.stockId, stockTradeModel.tradeTime, stockTradeModel.tradePrice, \
		    		 	stockTradeModel.tradeVolume, stockTradeModel.trend))
		    BaseStorage.db.commit()
		except Exception, e:
			BaseStorage.db.rollback()
			raise e
		finally:
			cursor.close()
			pass

