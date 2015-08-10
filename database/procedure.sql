# 股价最低的股
select a.stockCode, a.stockName, b.curPrice 
from stocks a inner join stocks_daily b 
	on a.id = b.stockId 
where b.curPrice > 0 
order by b.curPrice asc 
limit 20;

# 主力流入最多的股
select a.stockCode, a.stockname, b.curprice, b.yesterdaycloseprice, (b.curprice-b.yesterdaycloseprice)/b.yesterdaycloseprice as rise,
			 b.netflowin 
from stocks as a inner join 
	(select stockid, curprice, yesterdaycloseprice, (superflowin+bigflowin+superflowout+bigflowout) as netflowin 
	from stocks_daily 
	where updatedate='2015-07-22') as b 
		on a.id = b.stockid 
order by b.netflowin desc limit 30;

# 主力流入最多的股第二天的涨势
select stockId, curprice, yesterdaycloseprice, (curprice-yesterdaycloseprice)/yesterdaycloseprice as rise from stocks_daily
where updatedate='2015-07-22' and stockid in 
	(select b.stockid from
		(select stockid, curprice, yesterdaycloseprice, (superflowin+bigflowin+superflowout+bigflowout) as netflowin 
			from stocks_daily 
			where updatedate='2015-07-21'
			order by netflowin desc limit 30) b
	);

