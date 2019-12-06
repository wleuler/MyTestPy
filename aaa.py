import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data ,wb
sp500=data.DataReader('^GSPC',data_source='yahoo',start='1/1/2000',end='12/12/2017')
sp500['Close'].plot(grid=True,figsize=(8,5))
plt.show()