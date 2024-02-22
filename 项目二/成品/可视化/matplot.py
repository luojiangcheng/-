import csv

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# 华容、岳阳楼、云溪、临湘、汨罗等区域的房价波动较小，而湘阴、君山、岳阳县、平江等区域的房价波动较大。
year = []
huar = []
xiangyin = []
yueylouq = []
yunxi = []
lingxiang = []
miluo = []
junshan = []
yueyxian = []
pjiang = []
qita = []
file = open(r'D:\LJH\local\python\项目\项目二\成品\数据\15~23.csv', 'r', encoding='utf-8')
info = csv.reader(file)
for i in info:
    year.append(i[0])
    huar.append(i[1])
    xiangyin.append(i[2])
    yueylouq.append(i[3])
    yunxi.append(i[4])
    lingxiang.append(i[5])
    miluo.append(i[6])
    junshan.append(i[7])
    yueyxian.append(i[8])
    pjiang.append(i[9])
    qita.append(i[10])
plt.plot(year,huar)
plt.plot(year,xiangyin)
plt.plot(year,yueylouq)
plt.plot(year,yunxi)
plt.plot(year,lingxiang)
plt.plot(year,miluo)
plt.plot(year,yueyxian)
plt.plot(year,pjiang)
plt.plot(year,qita)
plt.show()
# 湘阴、平江等区域的房价在 2017 年上半年下降，之后有所回升，但房价整体波动较大，市场不稳定。

# 岳阳楼地区的房价在 2017 年下半年迅速攀升，并在 2018 年达到顶峰，之后略有下降，表现出市场的强势和泡沫。

# 各个区域的房价变化趋势基本上都表现出明显的季节性波动，每年 1-3 月份和 7-10 月份，房价相对高，而 4-6 月份和 11-12 月份则相对较低。

# 从 2019 年开始，房价整体呈现逐年上升的趋势，其中华容地区的涨幅最为明显，云溪地区的涨幅最小。

# 从每个地区的房价涨幅来看，存在明显的“土豪效应”，即房价上升快慢与地区地价水平和生活水平密切相关。
