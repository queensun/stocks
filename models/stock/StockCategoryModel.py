#encoding: utf-8

from models.BaseModel import BaseModel

class StockCategoryModel(BaseModel):
	"""股票所属板块模型"""
	def __init__(self, categoryId = None, categoryName = None, categoryBy = None):
		super(StockCategoryModel, self).__init__()
		self.id = categoryId
		self.categoryName = categoryName
		self.categoryBy = categoryBy				# 0: none; 1: 行业板块; 2: 概念板块; 3: 地域板块
