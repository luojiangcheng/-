import csv
from pyecharts.charts import Bar
from pyecharts import options as opts

with open(r'D:\LJH\local\python\第一个项目\项目二\成品\数据\最近数据.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    diqu = next(reader)
    fangjia = next(reader)

bar = (
    Bar()
    .add_xaxis(diqu)
    .add_yaxis("各地区房价",fangjia)
    .set_global_opts(title_opts=opts.TitleOpts("岳阳市各地区最近房价")
))
bar.render("岳阳市各地区最近房价.html")

