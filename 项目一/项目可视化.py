
import csv
from pyecharts.charts import Line
from pyecharts import options as opts

year = []
gjczsr = []
gjczzc = []
sssr = []
zzs = []
grsds = []
qysds = []
file = open(r'D:\LJH\local\python\项目\项目一\data.csv', 'r', encoding='utf-8')
info = csv.reader(file)
next(info)
for i in info:
    year.append(i[0])
    gjczsr.append(i[1])
    gjczzc.append(i[2])
    sssr.append(i[3])
    zzs.append(i[4])
    grsds.append(i[5])
    qysds.append(i[6])
#     # print(gjczsr)
#     # print(gjczzc)

line = (
    Line()
    .add_xaxis(year)
    .add_yaxis("国家财政收入",gjczsr,symbol='diamond',symbol_size=15)
    .add_yaxis("国家财政支出",gjczzc,symbol='diamond',symbol_size=15)
    .add_yaxis("增值税", zzs, symbol='diamond', symbol_size=15)
    .add_yaxis("企业所得税", qysds, symbol='diamond', symbol_size=15)
    .add_yaxis("税收收入", sssr, symbol='diamond', symbol_size=15)
    .set_global_opts(title_opts=opts.TitleOpts(title='国家财产收入图.html'))
)

line.render('国家财产收入图.html')





# import numpy as np
# plt.rcParams['font.sans-serif'] = 'SimHei'
# import matplotlib.pyplot as plt
# import pandas as pd
# df =pd.read_csv('data.csv')
# #print(df)
# df.plot(x='year',y=['gjczsr','gjczzc','sssr','zzs','qysds'])
#
# plt.show()