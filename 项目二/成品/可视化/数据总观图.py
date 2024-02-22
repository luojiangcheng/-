import csv
from pyecharts.charts import Line
from pyecharts import options as opts

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
next(info)
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
line = (
    Line()
    .add_xaxis(year)
    .add_yaxis("华容",huar)
    .add_yaxis("湘阴",xiangyin)
    .add_yaxis("岳阳楼区",yueylouq)
    .add_yaxis("云溪",yunxi)
    .add_yaxis("临湘",lingxiang)
    .add_yaxis("汨罗",miluo)
    .add_yaxis("君山",junshan)
    .add_yaxis("岳阳县",yueyxian)
    .add_yaxis("平江",pjiang)
    .add_yaxis("其它区市",qita)
    .set_global_opts(title_opts=opts.TitleOpts("岳阳市各地区近10年房价趋势"),
                             legend_opts=opts.LegendOpts(type_="scroll", pos_left="right", orient="vertical"))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)
line.render("岳阳各地区房价总观图.html")
