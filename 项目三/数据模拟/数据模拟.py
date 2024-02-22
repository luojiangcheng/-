# # 3-5年,本科,成都,12,20K·13薪,博普云,Kafka.Hive.Hadoop,
import random

# 打开文件
with open(r'D:\LJH\local\python\项目\项目三\数据模拟\城市.txt', 'r', encoding="utf-8") as f1:
    for i in f1.readlines():
        line = i.split(",")
        start = random.randint(30,60)
        end = random.randint(100,200)

        for field in line:
            for f in range(random.randint(start,end)):
                with open(r'D:\LJH\local\python\项目\项目三\数据模拟\工作经验.txt', 'r', encoding="utf-8") as f2:
                    lines2 = f2.readlines()
                with open(r'D:\LJH\local\python\项目\项目三\数据模拟\学历.txt', 'r', encoding="utf-8") as f3:
                    lines3 = f3.readlines()
                with open('D:\LJH\local\python\项目\项目三\数据模拟\最低工资-最高工资.txt', 'r', encoding="utf-8") as f4:
                    lines4 = f4.readlines()
                with open('D:\LJH\local\python\项目\项目三\数据模拟\公司.txt', 'r', encoding="utf-8") as f5:
                    lines5 = f5.readlines()
                with open('D:\LJH\local\python\项目\项目三\数据模拟\技术.txt', 'r', encoding="utf-8") as f6:
                    lines6 = f6.readlines()

                    weights = [0.73, 0.16, 0.04, 0.03, 0.009, 0.004, 0.004, 0.0004]  # 学历抽中概率
                    weights2 = [0.203, 0.425, 0.189, 0.144, 0.014, 0.006, 0.016] # 工作经验概率

                    # 从列表中随机选择一个值
                    random_value2 = random.choices(lines2,weights2,k=1)[0].strip()
                    random_value3 = random.choices(lines3, weights, k=1)[0].strip()
                    random_value4 = random.choice(lines4)
                    random_value5 = random.choice(lines5)
                    random_value6 = random.choice(lines6)
                    # 10年以上,初中及以下新星市12,21K,行云集团Java,C++,Python,计算机相关专业,数学/统计相关专业,留学生优先,英美留学生
                    # 输出随机值
                    with open("D:\LJH\local\python\项目\项目三\数据\shuj.csv", "a",
                              encoding="utf-8") as f7:
                        f7.write(
                            str(random_value2.strip()) + (str(random_value3)).strip() + "," + str(
                                field) + "," + str(random_value4.strip()) +
                            "," + str(random_value5.strip()) + "," + str(random_value6.strip()) + "\n")
print("完成！！！！")

# 本科0.73
# 大专0.16
# 学历不限0.04
# 硕士0.03
# 博士0.009
# 高中0.004
# 中专/中技0.004
# 初中及以下0.0004
