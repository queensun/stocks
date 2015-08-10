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
	updateTime datetime default now(),
	constraint uq_stocks_stockcode unique(stockCode)
)engine=innodb charset=utf8;

drop table if exists stocks_daily;
create table stocks_daily (
	id bigint primary key auto_increment,
	stockId int,
	openPrice decimal(10, 4),
	yesterdayClosePrice decimal(10, 4),
	curPrice decimal(10, 4),
	averagePrice decimal(10, 4),
	high decimal(10, 4),
	low decimal(10, 4),
	tradeVolume bigint,
	tradeValue decimal(20, 4),
	turnoverRate decimal(10,4),
	marketValue decimal(20, 4),
	circulationValue decimal(20, 4),
	pb decimal(10, 4),
	pe decimal(10, 4),
	buyVolume bigint,
	sellVolume bigint,
	amountRatio decimal(10, 4),
	entrustRatio decimal(10, 4),
	superFlowIn decimal(20, 4),
	superFlowOut decimal(20, 4),
	bigFlowIn decimal(20, 4),
	bigFlowOut decimal(20, 4),
	middleFlowIn decimal(20, 4),
	middleFlowOut decimal(20, 4),
	littleFlowIn decimal(20, 4),
	littleFlowOut decimal(20, 4),
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
	tradePrice decimal(10, 4),
	tradeVolume int(11),
	trend tinyint,
	updateTime datetime default now(),
	constraint fk_stock_trades_stockId foreign key (stockId) references stocks(id)
)engine=innodb charset=utf8;