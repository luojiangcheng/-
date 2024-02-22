from pyecharts.charts import Line
import pyecharts.options as opts
month = []
zuihao = []
zuicha = []
with open(r"C:\Users\昔日里\Desktop\波\可视化\shuj\岳阳18-22年每个月平均空气质量.csv","r",encoding='utf-8') as f:
    for i in f.readlines()[1:]:
        month.append(i.split(',')[0])
        zuihao.append(float(i.split(',')[1]))
        zuicha.append(float(i.split(',')[2]))
print(month)
print(zuihao)
print(zuicha)


my_theme_opts = {
    "color": {
        'x': 0,
        'y': 0,
        'x2': 0,
        'y2': 1,
        'colorStops': [{
            'offset': 0, 'color': 'azure'
        }, {
            'offset': 0.5, 'color': 'purple'
        },{
            'offset': 1, 'color': 'white'
        }]
    }
}




line = (
    Line(init_opts=opts.InitOpts(width="100%",height="900px",bg_color=my_theme_opts['color']))
    .add_xaxis(month)
    .add_yaxis("最好空气",zuihao,itemstyle_opts={
                       "color": {
                           'type': 'linear',
                           'x': 0,
                           'y': 0,
                           'x2': 0,
                           'y2': 1,
                           'colorStops': [{
                               'offset': 0, 'color': 'violet'
                           }, {
                               'offset': 0.5, 'color': 'green'
                           }, {
                               'offset': 1, 'color': 'blue'
                           }],
                           'globalCoord': True
                       }
                   },symbol_size=8)
    .add_yaxis("最差空气",zuicha,itemstyle_opts={
                       "color": {
                           'type': 'linear',
                           'x': 0,
                           'y': 0,
                           'x2': 0,
                           'y2': 1,
                           'colorStops': [{
                               'offset': 0, 'color': 'violet'
                           }, {
                               'offset': 0.5, 'color': 'green'
                           }, {
                               'offset': 1, 'color': 'blue'
                           }],
                           'globalCoord': True
                       }
                   },symbol_size=8)
    .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),title_opts=opts.TitleOpts(title="岳阳18-22年空气质量最好的月份",pos_left="center",title_textstyle_opts=opts.TextStyleOpts(font_size=30,color="black")
                                               ,subtitle="每年的6-7-8月份空气最好",subtitle_textstyle_opts=opts.TextStyleOpts(font_size=20,color="black")))
    .set_series_opts(label_opts=opts.LabelOpts(font_size=19))

)

line.render("岳阳18-22年空气质量最好的月份.html")
