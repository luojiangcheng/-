from pyecharts.charts import Bar
import pyecharts.options as opts
year = []
zuigao = []
zuidi = []
with open(r"C:\Users\昔日里\Desktop\波\可视化\shuj\九台近13年温度变化趋势.csv","r",encoding='utf-8') as f:
    for i in f.readlines()[1:]:
        year.append(i.split(',')[0])
        zuigao.append(float(i.split(',')[1]))
        zuidi.append(float(i.split(',')[2]))
print(zuigao)
print(zuidi)
my_theme_opts = {
    "color": {
        'x': 0,
        'y': 0,
        'x2': 0,
        'y2': 1,
        'colorStops': [{
            'offset': 0, 'color': 'blue'
        },{
            'offset': 0.5, 'color': 'white'
        },{
            'offset': 1, 'color': 'red'
        }]
    }
}




bar = (
    Bar(init_opts=opts.InitOpts(width="100%",height="900px",bg_color=my_theme_opts['color']))
    .add_xaxis(year)
    .add_yaxis("最好空气",zuigao,itemstyle_opts={
                       "color": {
                           'type': 'linear',
                           'x': 0,
                           'y': 0,
                           'x2': 0,
                           'y2': 1,
                           'colorStops': [{
                               'offset': 0, 'color': 'red'
                           }, {
                               'offset': 0.5, 'color': 'violet'
                           }, {
                               'offset': 1, 'color': 'white'
                           }],
                           'globalCoord': True
                       }
                   })
    .add_yaxis("最差空气",zuidi,itemstyle_opts={
                       "color": {
                           'type': 'linear',
                           'x': 0,
                           'y': 0,
                           'x2': 0,
                           'y2': 1,
                           'colorStops': [{
                               'offset': 0, 'color': 'blue'
                           }, {
                               'offset': 0.5, 'color': 'green'
                           }, {
                               'offset': 1, 'color': 'white'
                           }],
                           'globalCoord': True
                       }
                   })
    .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),title_opts=opts.TitleOpts(title="九台近13年温度变化趋势",pos_left="center",
                                                                                          title_textstyle_opts=opts.TextStyleOpts(font_size=30,color="black")))
    .set_series_opts(label_opts=opts.LabelOpts(font_size=19))

)

bar.render("九台近13年温度变化趋势.html")
