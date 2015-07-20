# 股价最低的股
select a.stockCode, a.stockName, b.curPrice from stocks a inner join stocks_daily b on a.id = b.stockId where b.curPrice > 0 order by b.curPrice asc limit 20;