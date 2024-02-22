import csv
from pyecharts.charts import Line, Timeline, Pie
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

file = open(r'D:\LJH\local\python\第一个项目\项目二\成品\数据\13~22.csv', 'r', encoding='utf-8')
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
tl = Timeline()

for y, t in zip((huar, xiangyin, yueylouq, yunxi, lingxiang, miluo, junshan, yueyxian, pjiang, qita)
        , ('华容县', '湘阴县', '岳阳楼区', '云溪县', '临湘县', '汨罗市', '君山区', '岳阳县', '平江县', '其他市区县')):
    line = (
        Line()
            .add_xaxis(year)
            .add_yaxis("{}".format(t), y, symbol='diamond', symbol_size=8)
            .set_global_opts(title_opts=opts.TitleOpts("岳阳市{}近10年房价趋势".format(t)),
                             legend_opts=opts.LegendOpts(type_="scroll", pos_left="right", orient="vertical"))
    )
    tl.add(line, "{}".format(t)
           )
tl.add_schema(is_auto_play=True, play_interval=1000)  # 自动播放，跳动的间隔为1000ms
tl.render('岳阳市各地区房价图.html')
