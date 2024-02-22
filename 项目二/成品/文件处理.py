# -----------------------------替换数据段---------------------
with open(r'D:\LJH\local\python\项目\项目二\成品\数据\13~23.csv', 'r', encoding='utf-8') as f:
    with open(r'D:\LJH\local\python\项目\项目二\成品\数据\13~22.csv', 'a', encoding='utf-8') as f2:
        for i in f.readlines():  # .replace(' ', '')
            f2.write(i.replace(' ', ','))
            # c = str(i.strip().split(",")[0:7])+"\n"
            # f2.write(c)
print("完成")
# ------------------------------去除空行----------------------------
# def clearBlankLine():
#     file1 = open('data.csv', 'r', encoding='utf-8') # 要去掉空行的文件
#     file2 = open('data3.csv', 'w', encoding='utf-8') # 生成没有空行的文件
#     try:
#         for line in file1.readlines():
#             if line == '\n':
#                 line = line.strip("\n")
#             file2.write(line)
#     finally:
#         file1.close()
#         file2.close()
#
#
# if __name__ == '__main__':
#     clearBlankLine()
# import csv
# "华容","湘阴","岳阳楼","云溪","临湘","汨罗","君山","岳阳县","平江","其他"