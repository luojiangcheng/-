import pandas as pd

# with open(r'D:\LJH\local\python\项目\项目三\可视化\全国数据\数据\_todo_1_.csv', 'r', encoding='utf-8') as f:
#     with open(r'D:\LJH\local\python\项目\项目三\可视化\全国数据\数据\_todo_1_.csv', 'a', encoding='utf-8') as f2:
#         for i in f.readlines():  # .replace(' ', '')
#             f2.write(i.replace('| ','').replace("|",""))
# print("完成")
# # 1-3年,本科,深圳,龙岗区,坂田,15,30K,华为,Python.Java.Spark.Hadoop.Storm.Streaming.Flink
# data = pd.read_csv(r"D:\LJH\local\python\项目\项目三\数据\处理完成2.csv",
#                    names=['工作经验','学历','城市','a','b','最低薪资','最高薪资','公司','技术要求'])
# data.drop(columns=['a','b'],axis=1,inplace=True)
#
# print(data.iloc[:,:5].head(5))
# data.to_csv(r"./1.csv",index=False)
#


# df = pd.read_csv(r"D:\LJH\local\python\项目\项目三\数据\BOSS.csv",
#                  names=['工作经验','学历','城市','最低薪资','最高薪资','公司','技术要求'])
# JiShu = df['技术要求']
# JiShu.to_csv(r"D:\LJH\Java\Scala\scala1\Spark\src\main\java\BOSS项目\数据\技术要求.txt",index=False)



pd.set_option('display.width', None)

# print(df.iloc[df[df['最低薪资'] > 40].index])
#
# print(df)
# mask = df['最低薪资'] > 50
# row = df[mask].index
#
# df.drop(row,inplace=True)
# df.dropna(axis=0,inplace=True)
# df.to_csv("./1.csv",index=False)
df = pd.read_csv(r"D:\LJH\local\python\项目\项目三\数据\BOSS.csv", header='infer')
df = df[df['学历'] == '大专']
print(df['最低薪资'].mean())
