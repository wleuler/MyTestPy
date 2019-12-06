import tushare as ts
ts.set_token('e7266b70f7ea8a7e0be1a6c9fa8d944feca69993836d35273a06af71')
pro = ts.pro_api()
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
print(df)

