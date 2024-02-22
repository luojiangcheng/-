import os
from pyecharts.charts import Bar, Pie, Grid, Line, Page
import pyecharts.options as opts
# from djangoProject.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

from pyecharts.options import LegendOpts


# https://www.kdocs.cn/l/cjEPFKbqYV1y


my_theme_opts1 = {
    "color": {
        'x': 0,
        'y': 1,
        'x2': 1,
        'y2': 0,
        'colorStops': [{
            'offset': 0, 'color': 'pink'
        }, {
            'offset': 0.5, 'color': 'red'
        }, {
            'offset': 1, 'color': 'blue'
        }]
    }
}
#
# todo 1 各城市大专学历满足岗位需求的岗位数量
shulian1 = []
chenshi1 = []
with open(r"D:\LJH\local\python\项目\项目三\可视化\热门城市数据\数据\_todo_1_.csv", "r", encoding="utf-8") as f:
    for i in f.readlines():
        into = i.strip()
        shulian1.append(int(into.split(",")[0]))
        chenshi1.append(into.split(",")[1])
print(shulian1)
print(chenshi1)
bar1 = (
    Bar(init_opts=opts.InitOpts(width='100%', height='800px'))
        .add_xaxis(chenshi1)
        .add_yaxis("数量", shulian1, color=my_theme_opts1['color'], bar_width='80')
        .set_global_opts(title_opts=opts.TitleOpts(title="各城市大专学历满足岗位需求的岗位数量", pos_left='center',
                                                   title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
                         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(interval=0, rotate=30)),
                         legend_opts=opts.LegendOpts(is_show=False), )

)
bar1.render(os.path.join(BASE_DIR, 'app/templates/todo1.html'))
print("todo1完成！")
# # todo 2 全国大数据行业中对学历的要求比例
# shulian2 = []
# xueli2 = []
# sepdata2 = []
# with open(r"D:\LJH\local\python\项目\项目三\可视化\热门城市数据\数据\_todo_2_.csv", "r", encoding="utf-8") as f1:
#     for i in f1.readlines():
#         into = i.strip()
#         shulian2.append(int(into.split(",")[0]))
#         xueli2.append(into.split(",")[1])
# print(shulian2)
# print(xueli2)
# #
# for x, s in zip(shulian2, xueli2):
#     sepdata2.append([s, x])
# print(sepdata2)
#
# pie2 = (
#     Pie(init_opts=opts.InitOpts(width='900px'))
#         .add("各学历在各个城市大数据行业中所占的比例", sepdata2, center=["28%", "50%"])
#         .set_global_opts(title_opts=opts.TitleOpts(title="全国大数据行业中对学历的要求比例扇形图", pos_left="center",
#                                                    title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
#                          legend_opts=LegendOpts(pos_bottom="bottom", is_show=False),
#                          )
#         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# )
# bar2 = (
#
#     Bar(init_opts=opts.InitOpts(width='900px'))
#         .add_xaxis(xueli2)
#         .add_yaxis("学历", shulian2)
#         .set_global_opts(title_opts=opts.TitleOpts(title="全国大数据行业中对学历的要求比例柱形图"),
#                          xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(interval=0, rotate=30)),
#                          legend_opts=opts.LegendOpts(is_show=False))
# )
#
# page = (
#     Page(layout=Page.SimplePageLayout, page_title="全国大数据行业中对学历的要求比例", )
#         .add(pie2)
#         .add(bar2)
# )
# page.render(os.path.join(BASE_DIR, 'app/templates/todo2.html'))
# print("完成！")
# ## todo 3 各个城市中大专学历满足该专业平均薪资的岗位数量
# colors3 = ['#DF927C', '#A3C272', '#FED863', '#EE82EE', '#FF86C1', '#C2E67F', '#F3E69F', '#0000FF', '#FFF000']
# shul3 = []
# chenshi3 = []
#
# with open(r"D:\LJH\local\python\项目\项目三\可视化\热门城市数据\数据\_todo_3_.csv", "r", encoding="utf-8") as f:
#     for i in f.readlines():
#         into = i.strip()
#         shul3.append(int(into.split(",")[0]))
#         chenshi3.append(into.split(",")[1])
#
# print(shul3)
# print(chenshi3)
#
# y3 = []
# for j in range(9):
#     y3.append(
#         opts.BarItem(
#             name=chenshi3[j],
#             value=shul3[j],
#             itemstyle_opts=opts.ItemStyleOpts(color=colors3[j]),
#         )
#     )
# bar3 = (
#     Bar(init_opts=opts.InitOpts(width='90%', height='800%'))
#         .add_xaxis(chenshi3)
#         .add_yaxis("城市", y3)
#         .set_global_opts(title_opts=opts.TitleOpts(title="各个城市中大专学历满足该专业平均薪资的岗位数量", pos_right="center",
#                                                    title_textstyle_opts=opts.TextStyleOpts(font_size=30, color="red")),
#                          legend_opts=LegendOpts(is_show=False),
#                          )
#
# )
# bar3.render(os.path.join(BASE_DIR, 'app/templates/todo3.html'))
# print("todo3完成！")
# # # todo 4 大数据专业使用最广泛的技术排名top20
# jishu4 = []
# shul4 = []
# with open(r"D:\LJH\local\python\项目\项目三\可视化\热门城市数据\数据\使用数量最多的技术.csv", "r", encoding="utf-8") as f:
#     for y in f.readlines():
#         i = y.strip()
#         shul4.append(int(i.split(",")[1]))
#         jishu4.append(i.split(",")[0])
# print(jishu4)
# print(shul4)
# pie4 = (
#     Pie(init_opts=opts.InitOpts(theme="chalk"))
#         .add("技术", data_pair=[[q, w] for q, w in zip(jishu4, shul4)],
#              radius=["20%", "70%"],
#              center=["50%", "50%"],
#              rosetype="radius",
#              label_opts=opts.LabelOpts(
#                  position="outside",
#                  background_color="#b0eef9",
#                  border_width=1,
#                  border_radius=5,
#                  formatter="{a|{a}}{abg|}\n{hr|}\n{b|{b}:}{c} {per|{d}%}",
#                  rich={
#                      "a": {"color": "blue", "lineHeight": 20, "align": "center", "fontSize": 10},
#                      "abg": {"backgroundColor": "#7fcee4", "width": "100%", "align": "right",
#                              "borderRadius": [4, 4, 0, 0]},
#                      "hr": {"borderColor": "black", "width": "100%", "borderWidth": 0.2, "height": 0},
#                      "b": {"fontSize": 12, "lineHeight": 25},
#                      "d": {"color": "violet", "backgroundColor": "#334455", "borderRadius": 2, "padding": [2, 3]},
#                      "per": {"color": "violet", "backgroundColor": "#334455", "borderRadius": 2, "padding": [2, 3]}
#                  }
#              ))
#         .set_global_opts(legend_opts=LegendOpts(is_show=False),
#                          xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(interval=0, rotate=30))
#                          )
#
# )
# bar4 = (
#     Bar(init_opts=opts.InitOpts(theme="chalk"))
#         .add_xaxis(jishu4)
#         .add_yaxis("", shul4)
#         .set_global_opts(title_opts=opts.TitleOpts(title="大数据专业使用最广泛的技术排名top20", pos_left="center",
#                                                    title_textstyle_opts=opts.TextStyleOpts(font_size=40)),
#                          xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(interval=0, rotate=30)))
#
# )
# page4 = (
#     Page(layout=Page.SimplePageLayout)
#         .add(pie4)
#         .add(bar4)
# )
# page4.render(os.path.join(BASE_DIR, 'app/templates/技术排名top20.html'))
# print("todo4完成！")
#
# # # todo 5 大专学历在各地区的平均最低薪资是多少
# xinzi5 = []
# chenshi5 = []
#
# with open(r"D:\LJH\local\python\项目\项目三\可视化\热门城市数据\数据\_todo_5_.csv", "r", encoding="utf-8") as f:
#     for i in f.readlines():
#         xinzi5.append(float(i.split(",")[0]))
#         chenshi5.append(i.split(",")[1].strip())
# print(xinzi5)
# print(chenshi5)
# shul5 = []
# chenshi5 = []
#
# with open(r"D:\LJH\local\python\项目\项目三\可视化\热门城市数据\数据\_todo_3_.csv", "r", encoding="utf-8") as f2:
#     for i in f2.readlines():
#         into = i.strip()
#         shul5.append(int(into.split(",")[0]))
#         chenshi5.append(into.split(",")[1])
#
# print(shul5)
# print(chenshi5)
# bar5 = (  # 将整个过程代码赋值给bar
#     Bar()  # 绘制柱形图
#         .add_xaxis(chenshi5)  # 柱形图x轴数据
#         .add_yaxis("城市", xinzi5, label_opts=opts.LabelOpts(font_size=20))  # 柱形图y轴数据，需要两个参数，一个字符串一个数据
#         .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(interval=0, rotate=30, font_size=20)),
#                          yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=20)),
#                          title_opts=opts.TitleOpts(title="大专学历在各地区的平均最低薪资", pos_bottom="50%",
#                                                    title_textstyle_opts=opts.TextStyleOpts(font_size=30),
#                                                    pos_right="center"),
#                          legend_opts=opts.LegendOpts(is_show=False))
#
# )
# line5 = (
#     Line()
#         .add_xaxis(chenshi5)
#         .add_yaxis("", shul5, linestyle_opts=opts.LineStyleOpts(width=5), symbol_size=10,
#                    itemstyle_opts=opts.ItemStyleOpts(color=my_theme_opts1['color']),
#                    label_opts=opts.LabelOpts(font_size=20))
#         .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
#                          yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=20))
#                          , title_opts=opts.TitleOpts(title="各个城市中大专学历满足该专业平均薪资的岗位数量", pos_left='center',
#                                                      title_textstyle_opts=opts.TextStyleOpts(font_size=30),
#                                                      pos_right="center"),
#                          legend_opts=opts.LegendOpts(is_show=False))
# )
# # gid = bar.overlap(line)
# grid5 = (
#     Grid(init_opts=opts.InitOpts(width="90%", height="900px"))
#         .add(chart=bar5, grid_opts=opts.GridOpts(pos_top="45%"))
#         .add(chart=line5, grid_opts=opts.GridOpts(pos_bottom="60%"))
# )
# grid5.render(os.path.join(BASE_DIR, 'app/templates/todo5.html'))
# print("todo5完成")
#
# # todo 6 适合工作经验不足的新人的城市推荐
# zonshu6 = []
# shul6 = []
# chengshi6 = []
#
# with open(r"D:\LJH\local\python\项目\项目三\可视化\热门城市数据\数据\_todo_6_.csv", "r", encoding="utf-8") as f:
#     for i in f.readlines():
#         zonshu6.append(int(i.split(",")[0]))
#         shul6.append(int(i.split(",")[1]))
#         chengshi6.append(i.split(",")[2])
# sepdata = []
# for chen, shi in zip(chengshi6, shul6):
#     sepdata.append([chen.strip(), shi])
# print(sepdata)
# bar6 = (
#     Bar(init_opts=opts.InitOpts(width="90%", height="900px"))
#         .add_xaxis(chengshi6)
#         .add_yaxis("经验不足岗位数量", shul6, label_opts=opts.LabelOpts(font_size=20))
#         .add_yaxis("岗位总数量", zonshu6, label_opts=opts.LabelOpts(font_size=20))
#         .set_global_opts(legend_opts=opts.LegendOpts(pos_right="right", textstyle_opts=opts.TextStyleOpts(font_size=30))
#                          , yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=20)), title_opts=(
#             opts.TitleOpts(title="适合工作经验不足的新人的城市推荐", pos_right="center",
#                            title_textstyle_opts=opts.TextStyleOpts(font_size=30))),
#                          xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=20)
#                                                   )
#                          )
#         .set_series_opts()
# )
# bar6.render(os.path.join(BASE_DIR, 'app/templates/todo6.html'))
# print("todo6完成")
