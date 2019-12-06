import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import  pandas_datareader as pdr
goog=pdr.get_data_yahoo("AAPL",'01-01-2000','22-09-2017')
# print(type(goog))
# print(goog.tail(5))
plot(goog['Date'],goog['Adj Close'])
plot.show()