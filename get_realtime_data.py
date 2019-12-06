# coding=UTF-8
import tushare as ts
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
test=ts.get_k_data('601688')
a=[]
for i in test["date"]:
    x=datetime.datetime.strptime(i,'%Y-%m-%d')
    a.append(x)
plt.plot(a,test["close"])
# plt.xticks(rotation=90)
plt.ylabel(U'收盘价')
plt.title(U'华泰证券')
plt.show()
#plt.plot(test.date,test.close)

plt.xlabel(U'日期')