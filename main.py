#encoding: utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from services.stock.StockService import StockService
from services.stock.StockCrawlerService import StockCrawlerService
from models.stock.StockModel import StockModel

if __name__ == '__main__':
	# StockCrawlerService.fetchAllStockBaseModelsFromInternet()

	# StockCrawlerService.fetchAllStockCategoryModelsFromInternet()

	# StockCrawlerService.fetchAllStockCategoryRelationsFromInternet()

	# l = StockService.getAllStockBaseModels()
	# for model in l:
	# 	StockCrawlerService.fetchDailyStockModelFromInternet(model)

	l = StockService.getAllStockBaseModels()
	for model in l:
		StockCrawlerService.fetchStockTradeInfoFromInternet(model)

	