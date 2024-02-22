import pandas as pd

filepath = r"C:\Users\昔日里\Desktop\波\数据\全部天气处理完成.csv"
data = pd.read_csv(filepath, names=['city', 'date_week', 'hightest_tem', 'lowest_tem', 'weather', 'wind'])
# 分列
date = []
week = []

for i in data['date_week'].str.split(' '):
    date.append(i[0])
    week.append(i[1])

data['date'] = date
data['week'] = week

wind_direction = []
wind_level = []
for i in data['wind'].str.split(' '):
    wind_direction.append(i[0])
    wind_level.append(i[1])
data["wind_direction"] = wind_direction
data["wind_level"] = wind_level

# print(data)

data.drop("date_week", axis=1, inplace=True)
data.drop("wind", axis=1, inplace=True)
# 访问字符串需要加.str
# 将温度去掉字符串
data['hightest_tem'] = data['hightest_tem'].str.replace("℃", "")
data['lowest_tem'] = data['lowest_tem'].str.replace("℃", "")
data['wind_level'] = data['wind_level'].str.replace("级", "")

# 计算平均值并填充缺失值
avg = data.mean()
data.fillna(avg, inplace=True)
print("============================================================")
# print(data.isnull())
# 检查填充后的缺失值数量
# print(data.isna().sum())
data['week'] = data['week'].str.replace("周", "星期")

# 填充众数值
mode_values = data['weather'].mode()
data['weather'].fillna(mode_values.iloc[0], inplace=True)

mode_values1 = data['wind_level'].mode()
data['wind_level'].fillna(mode_values1.iloc[0], inplace=True)
# 再次检查填充后的缺失值数量
# print(data.isnull().sum())
# print()
d = data.drop_duplicates(data)
print(d)
# 将星期数据填充为其他相同日期的数据
data['date'] = pd.to_datetime(data['date'])
filled_df = data.groupby(data['date'].dt.day)['week'].transform(lambda x: x.fillna(method='bfill'))
data['week'] = filled_df

data = pd.read_csv(r"C:\Users\昔日里\Desktop\波\数据\全部天气.csv", header='infer')

# todo 1城市近10年平均气温
# 按城市分组
grouped = data.groupby("city")
# 获取每个城市的平均最高气温和平均最低气温取2位小数
city_stats = grouped.agg({'hightest_tem': 'mean', 'lowest_tem': 'mean'}).round(2)
# print(city_stats)
# 获取索引列（城市列）
shuj = city_stats.reset_index()
shuj.to_csv(r"C:\Users\昔日里\Desktop\波\数据\城市近10年平均气温.csv", index=False)
#
# todo 2 各城市持续最长的天气类型
data['date'] = pd.to_datetime(data['date']).dt.year
grouped2 = data.groupby(['city', 'date', 'weather']).size().reset_index(name='count')
# 找出每个城市每年出现次数最多的天气类型
shuj2 = grouped2.loc[grouped2.groupby(['city', 'date'])['count'].idxmax()]
da = pd.DataFrame(shuj2)
zu = da.groupby(['city', 'weather']).agg({'count': 'sum'}).reset_index()
zu1 = zu.groupby(['city']).max().reset_index()
zu1.to_csv(r"C:\Users\昔日里\Desktop\波\可视化\shuj\各城市每年持续最长的天气类型.csv", index=False)

# todo 3多个城市不同季节的温度、天气类型和风向风力变化情况
# 假设日期时间字段为 'date_time'
data['date'] = pd.to_datetime(data['date'])

# 提取月份信息
data['month'] = data['date'].dt.month

# 利用月份信息映射到季节
season_map = {1: '冬季', 2: '冬季', 3: '春季', 4: '春季', 5: '春季', 6: '夏季', 7: '夏季', 8: '夏季', 9: '秋季', 10: '秋季', 11: '秋季',
              12: '冬季'}
data['season'] = data['month'].map(season_map)

# 按季节进行分组：利用groupby函数按季节对数据进行分组。
grouped3 = data.groupby('season')

# 获取每个季节的温度、天气类型、风向和风力等数据

for season, data2 in grouped3:
    print(f"Season: {season}")
    s = data2[['city', 'hightest_tem', 'lowest_tem', 'weather', 'wind_direction', 'wind_level']]
    a = s.groupby('city').first().reset_index()
    # print(a)
    a.to_csv(r"C:\Users\昔日里\Desktop\波\数据\春季数据之最.csv", index=False)
# todo  月份数据处理
data['hightest_tem'] = data['hightest_tem'].round(1)
data['lowest_tem'] = data['lowest_tem'].round(1)
data = data.iloc[:, 2:]
data.to_csv(r"C:\Users\昔日里\Desktop\波\数据\全部天气.csv")


def extract_first_wind_level(wind_level):
    return str(wind_level.split('~')[0].split('-')[0].replace("小于", ""))


# 应用函数到 wind_level 列
data['wind_level'] = data['wind_level'].apply(extract_first_wind_level)

# todo 4 各城市最大风力分析
data['wind_level'] = data['wind_level'].str.replace('\D', '', regex=True)
pd.DataFrame(data['wind_level'])
print(data[data['wind_level'] == data['wind_level'].max()])
data[data['wind_level'] == data['wind_level'].max()].to_csv("./各城市最大风力分析.csv", index=False)

# todo 5 九台近13年温度变化趋势
year = pd.to_datetime(data['date']).dt.year
print(data[data['city'] == '九台'].groupby(year).agg({'hightest_tem': 'mean', 'lowest_tem': 'mean'}).round(2))
shu = data[data['city'] == '九台'].groupby(year).agg({'hightest_tem': 'mean', 'lowest_tem': 'mean'}).reset_index().round(
    2)
shu.to_csv(r"C:\Users\昔日里\Desktop\波\可视化\shuj\九台近13年温度变化趋势.csv", index=False)

# todo 岳阳市数据分析----------------------------------------------
data = pd.read_csv(r"C:\Users\昔日里\Desktop\波\数据\岳阳16年-22年数据.csv", header='infer',
                   names=['city', 'date', 'pjgaow', 'pjdiw', 'jiduangaow', 'jiduandiw', 'kqizhil', 'kqizuihao',
                          'zuihaorqi', 'kqizuicha', 'zuicharqi'])

data['pjgaow'] = data['pjgaow'].str.replace("℃", "")
data['pjdiw'] = data['pjdiw'].str.replace("℃", "")
data['jiduangaow'] = data['jiduangaow'].str.replace("℃", "")
data['jiduandiw'] = data['jiduandiw'].str.replace("℃", "")
data['zuihaorqi'] = data['zuihaorqi'].str.replace("/", "-")
data['zuicharqi'] = data['zuicharqi'].str.replace("/", "-")
data.to_csv(r"C:\Users\昔日里\Desktop\波\数据\岳阳16年-22年数据.csv", index=False)

data = pd.read_csv(r"C:\Users\昔日里\Desktop\波\数据\岳阳16年-22年数据.csv", header="infer")
# # todo 6 岳阳18-22年空气质量变化趋势
data1 = ['date','kqizuihao','kqizuicha']

data[data1].to_csv(r"C:\Users\昔日里\Desktop\波\可视化\shuj\岳阳18-22年空气质量变化趋势.csv", index=False)
# # todo 7 岳阳每年空气质量最好的月份

year = pd.to_datetime(data['date']).dt.month
data1 = data.groupby(year).agg({'kqizuihao': 'mean', 'kqizuicha': 'mean'}).round(2).reset_index()

data1.to_csv(r"C:\Users\昔日里\Desktop\波\可视化\shuj\岳阳18-22年空气质量最好的月份.csv", index=False)
