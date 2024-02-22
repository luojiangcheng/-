from pyecharts.charts import Bar, Line, Pie, Grid
import pyecharts.options as opts
from pyecharts.options import LegendOpts

# todo 1. 统计各类型专辑的数量；

#
genre = []
shulian = []
data = []
with open(r"D:\LJH\local\python\项目\Spark音乐分析可视化\数据\_todo_1.csv", 'r', encoding="utf-8") as f:
    for i in f.readlines():
        genre.append(i.split(",")[0])
        shulian.append(int(i.split(",")[1]))
for z, d in zip(genre, shulian):
    data.append([z, d])
print(data)

# pie = (
#     Pie()
#         .add("音乐", data)
#         .set_global_opts(title_opts=opts.TitleOpts(title="各类型专辑的数量统计",pos_top="top"),
#                          legend_opts=LegendOpts(pos_bottom="bottom"),
# )
#         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#
# )
# pie.render("音乐分析1.html")
# print("生成成功")

# # todo 2. 统计各类型专辑的销量总数；
# genre = []
# shulian = []
# with open(r"D:\LJH\local\python\项目\Spark音乐分析可视化\数据\_todo_2.csv", 'r', encoding="utf-8") as f:
#     for i in f.readlines():
#         shulian.append(int(i.split(",")[0]))
#         genre.append(i.split(",")[1].strip())
# print(shulian)
# print(genre)
# bar = (
#     Bar()
#     .add_xaxis(genre)
#     .add_yaxis("各类型专辑的销量总数",shulian)
#     .set_series_opts(label_opts=LegendOpts(is_show=False))
#     .set_global_opts(title_opts=opts.TitleOpts(title="各类型专辑的销量总数"))
#
# ).render("音乐分析2.html")
# todo 3. 统计近20年每年发行的专辑数量和单曲数量；
# zhuanji = []
# danqu = []
# year = []
# with open(r"D:\LJH\local\python\项目\Spark音乐分析可视化\数据\_todo_3_.csv", 'r', encoding="utf-8") as f:
#     for i in f.readlines():
#         zhuanji.append(int(i.split(",")[0]))
#         danqu.append(int(i.split(",")[1]))
#         year.append(i.split(",")[2].strip())
# print(zhuanji)
# print(danqu)
# print(year)
#
# bar = (
#     Bar()
#     .add_xaxis(year)
#     .add_yaxis("专辑",zhuanji,stack="stack1")
#     .add_yaxis("单曲",danqu,stack="stack1")
#     .set_global_opts(title_opts=opts.TitleOpts(title="近20年每年发行的专辑数量和单曲数量图"))
# ).render("音乐分析3.html")
# print("成功")

# todo 4. 分析总销量前五的专辑类型的各年份销量；
# zonliang = []
# genre = []
# with open("D:\LJH\local\python\项目\Spark音乐分析可视化\数据\Result_4.csv", 'r', encoding="utf-8") as f2:
#     for a in f2.readlines():
#         zonliang.append(a.split(",")[0])
#         genre.append(a.split(",")[1].strip())
# print(zonliang)
# print(genre)
# data1 = []
# for z, g in zip(zonliang, genre):
#     data1.append([g, z])
# print(data1)
# year = []
# xioaliang = []
#
# Pop_Rock = []
# with open(r"D:\LJH\local\python\项目\Spark音乐分析可视化\数据\_todo_4.csv", 'r', encoding="utf-8") as f:
#     for i in f.readlines():
#         year.append(i.split(",")[2].strip())
#         xioaliang.append(i.split(",")[0])
#
# year1 = year[:20]
# Indie = xioaliang[:20]
# Pop = xioaliang[20:40]
# Rap = xioaliang[40:60]
# Latino = xioaliang[60:80]
# Pop_Rock = xioaliang[80:100]
# print(year1)
# print(Indie)
# print(Pop)
# print(Rap)
# print(Latino)
# print(Pop_Rock)
#
# line = (
#     Line()
#         .add_xaxis(year1)
#         .add_yaxis("Indie", y_axis=Indie)
#         .add_yaxis("Pop", Pop)
#         .add_yaxis("Rop", Rap)
#         .add_yaxis("Latino", Latino)
#         .add_yaxis("Pop_Rock", Pop_Rock)
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(title_opts=opts.TitleOpts(title="销量排名前五的各类专辑每年的销售额",pos_left="left")
#                          ,legend_opts=opts.LegendOpts(pos_top="top"))
#
#
# )
# bar = (
#     Bar()
#     .add_xaxis(genre)
#     .add_yaxis("总量",zonliang)
#     .set_series_opts(opts.TitleOpts(title="销量排名前五的类型总销量",subtitle="Spark"))
#     .set_global_opts(legend_opts=opts.LegendOpts(pos_bottom="bottom"))
# )
# grid = (
#     Grid()
#         .add(chart=line, grid_opts=opts.GridOpts(pos_bottom="50%"))
#         .add(chart=bar, grid_opts=opts.GridOpts(pos_top="55%"))
# )
# grid.render("音乐分析4.html")
#
# print("完成")
# todo 5. 分析总销量前五的专辑类型，在不同评分体系中的平均评分。
# rolling_stone_critic：滚石网站的评分
# 7. mtv_critic：全球最大音乐电视网MTV的评分
# 8. music_maniac_critic：音乐达人的评分
pftx = []
rsc = []
mc = []
mmc = []
Latino = []
Pop = []
Pop_Rock = []
Indie = []
Rap = []
tmp = []
with open(r"D:\LJH\local\python\项目\Spark音乐分析可视化\数据\_todo_5_.csv", 'r', encoding="utf-8") as f:
    for g in f.readlines():
        i = g.strip()
        pftx.append(i.split(",")[0])
        rsc.append(float(i.split(",")[1]))
        mc.append(float(i.split(",")[2]))
        mmc.append(float(i.split(",")[3]))

        split = g.split(',')
        list = [float(i.strip()) for i in split[1:]]
        tmp.append(list)
print(tmp)
Latino = tmp[0]
Pop = tmp[1]
Pop_Rock = tmp[2]
Indie = tmp[3]
Rap = tmp[4]

bar = (
    Bar()
    .add_xaxis(pftx)
    .add_yaxis("滚石网站的评分",rsc)
    .add_yaxis("MTV的评分",mc)
    .add_yaxis("音乐达人的评分",mmc)
    .set_series_opts(opts.TitleOpts(title="前五的音乐类型在各个评分系统上的平均评分图",pos_bottom="bottom"))
    .set_global_opts(LegendOpts(pos_bottom="center"))
)
bar2 = (
    Bar()
    .add_xaxis(["rolling_stone_critic","mtv_critic","music_maniac_critic"])
    .add_yaxis("Latino",Latino)
    .add_yaxis("Pop",Pop)
    .add_yaxis("Pop-Rock",Pop_Rock)
    .add_yaxis("Indie",Indie)
    .add_yaxis("Rap",Rap)
    .set_series_opts(opts.TitleOpts(title="前五的音乐类型在各个评分系统上的平均评分图",pos_top="bottom"))
    .set_global_opts(legend_opts=opts.LegendOpts(pos_top="bottom"))
)

grid = Grid()
grid.add(chart=bar,grid_opts=opts.GridOpts(pos_bottom="55%"))
grid.add(chart=bar2,grid_opts=opts.GridOpts(pos_top="55%"))
grid.render("音乐分析5.html")
print("完成")
