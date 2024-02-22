# C:\Users\昔日里\Desktop\波\可视化\shuj\岳阳18-22年空气质量变化趋势.csv
from pyecharts.charts import Line
import pyecharts.options as opts

year = []
zuihao = []
zuicha = []
with open(r"C:\Users\昔日里\Desktop\波\可视化\shuj\岳阳18-22年空气质量变化趋势.csv", "r", encoding='utf-8') as f:
    for i in f.readlines()[1:]:
        year.append(i.split(',')[0])
        zuihao.append(float(i.split(',')[1]))
        zuicha.append(float(i.split(',')[2]))
print(zuihao)
print(zuicha)
my_theme_opts = {
    "color": {
        'x': 0,
        'y': 0,
        'x2': 0,
        'y2': 1,
        'colorStops': [{
            'offset': 0, 'color': 'blue'
        }, {
            'offset': 0.5, 'color': 'white'
        }, {
            'offset': 1, 'color': 'red'
        }]
    }
}
my_max_temp_opts = {
    "color": {
        'x': 0,
        'y': 0,
        'x2': 0,
        'y2': 1,
        'colorStops': [{
            'offset': 0, 'color': 'red'
        }, {
            'offset': 0.5, 'color': 'orange'
        }, {
            'offset': 1, 'color': 'yellow'
        }],
    }
}
my_min_temp_opts = {
    "color": {
        'x': 0,
        'y': 0,
        'x2': 1,
        'y2': 0,
        'colorStops': [{
            'offset': 0, 'color': 'violet'
        }, {
            'offset': 0.5, 'color': 'green'
        }, {
            'offset': 1, 'color': 'blue'
        }]
    }
}

bar = (
    Line(init_opts=opts.InitOpts(width="100%", height="900px", bg_color=my_theme_opts['color']))
        .add_xaxis(year)
        .add_yaxis("最好空气", zuihao, itemstyle_opts={
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
    }, areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color=my_max_temp_opts['color']), is_smooth=True,
                   linestyle_opts=opts.LineStyleOpts(color="cyan", width=1.5))
        .add_yaxis("最差空气", zuicha, itemstyle_opts={
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
    }, areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color=my_min_temp_opts['color']), is_smooth=True,
                   linestyle_opts=opts.LineStyleOpts(color="cyan", width=1.5))
        .set_global_opts(datazoom_opts=opts.DataZoomOpts(
        type_="slider",  # 区域缩放样式设置为滑块
        range_start=0,  # 数据起始百分比设置为0%
        range_end=20,  # 终止百分比设置为5%；
    ), legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="岳阳18-22年空气质量变化趋势.csv", pos_left="center",
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=30, color="black")))
        .set_series_opts(label_opts=opts.LabelOpts(font_size=19))

)

bar.render("岳阳18-22年空气质量变化趋势.csv.html")
