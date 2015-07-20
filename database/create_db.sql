drop database if exists finance;
create database finance;

grant all privileges on finance.* to finance@'localhost' identified by 'finance_fb3efc4'; 

use finance;

drop table if exists stocks;
create table stocks (
	id int primary key auto_increment,
	stockCode nchar(6) unique,
	stockName varchar(16),
	market varchar(4),
	updateTime datetime default now()
)engine=innodb charset=utf8;

drop table if exists stocks_daily;
create table stocks_daily (
	id int(11) primary key auto_increment,
	stockId int,
	openPrice float,
	yesterdayClosePrice float,
	curPrice float,
	averagePrice float,
	high float, 
	low float,
	tradeVolume float,
	tradeValue float,
	turnoverRate float,
	marketValue float,
	circulationValue float,
	pb float,
	pe float,
	buyVolume float,
	sellVolume float,
	amountRatio float,
	entrustRatio float,
	totalFlowIn float,
	totalFlowOut float,
	superFlowIn float,
	superFlowOut float,
	bigFlowIn float,
	bigFlowOut float,
	middleFlowIn float,
	middleFlowOut float,
	littleFlowIn float,
	littleFlowOut float,
	updateDate date,
	updateTime datetime default now(),
	constraint fk_stock_daily_info_stockId foreign key (stockId) references stocks(id)
)engine=innodb charset=utf8;

drop table if exists stock_categories;
create table stock_categories (
	id int(11) primary key auto_increment,
	categoryName varchar(16),
	categoryBy int,
	updateTime datetime default now()
)engine=innodb charset=utf8;

drop table if exists stock_category_relationships;
create table stock_category_relationships (
	id int(11) primary key auto_increment,
	stockId int(11),
	categoryId int(11),
	updateTime datetime default now(),
	constraint fk_stock_category_relationships_stockId foreign key (stockId) references stocks(id),
	constraint fk_stock_category_relationships_categoryId foreign key (categoryId) references stock_categories(id),
	constraint uq_stock_category_relationships unique(stockId, categoryId)
)engine=innodb charset=utf8;

drop table if exists stock_trades;
create table stock_trades (
	id bigint primary key auto_increment,
	stockId int(11),
	tradeTime datetime,
	tradePrice float,
	tradeVolume int(11),
	trend tinyint,
	updateTime datetime default now(),
	constraint fk_stock_trades_stockId foreign key (stockId) references stocks(id)
)engine=innodb charset=utf8;