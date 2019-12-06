# 通过tushare获取股票信息
import tushare as ts
import matplotlib.pyplot as plt
import talib
df = ts.get_k_data('600519', start='2015-01-01', end='2019-11-21')
# 提取收盘价
closed = df['close'].values

upper, middle, lower = talib.BBANDS(closed, matype=talib.MA_Type.T3)
diff1 = upper - middle
diff2 = middle - lower

print(upper, middle, lower)
plt.plot(upper)
plt.plot(middle)
plt.plot(lower)
plt.plot(diff1)
plt.plot(diff2)
plt.show()

