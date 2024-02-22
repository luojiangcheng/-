import time
import requests
from lxml import etree

# 处理反爬
headers = {
    'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/103',
    'cookie': 'cookie: isp=true; aQQ_ajkguid=100A9EC6-8906-F745-62F0-SX1025090325; id58=CroD4GNXNd5xR/E1FJ4TAg==; 58tj_uuid=e5aeae67-9c05-4b0c-9756-9f2911873c2d; ajk-appVersion=; als=0; wmda_uuid=c7019ea773f8e14cbdf96e426e3806c8; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; _ga=GA1.2.1364599187.1669029794; new_uv=15; sessid=65F81A1F-6324-5671-5D3E-DF3542AF2F72; ctid=139; twe=2; obtain_by=2; wmda_session_id_6289197098934=1686629408235-222d8f47-4193-7a3b; xxzl_cid=0be0a8b85689470f9f0d3bc4470e1d07; xxzl_deviceid=I9PRVG3NfCh9ACNHOLPMGWExSpf1q71F0Hes9k5vupNib7T3ajJw09y5EehYSqm9'
              'F2kicUKcT'
}
# 将每个链接地址的不同点加入
with open('./地区', 'r', encoding='utf-8') as f:
    time.sleep(0.5)
    for i in f.readlines():

        for t in range(2013, 2024):
            url = 'https://www.anjuke.com/fangjia/yueyang' + str(t) + '/' + str(i.split(',')[0])
            print(url)

            time.sleep(0.5)  # 延时0.5秒

            resp = requests.get(url, headers=headers)  # 发送请求，获取源代码

            yuanma = etree.HTML(resp.text)  # 将源代码转为html文本供xpath解释器解析

            year = yuanma.xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul/li/a/b/text()')  # 时间

            fangjia = yuanma.xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul/li/a/span/text()')  # 房价

            with open(r'D:\LJH\local\python\项目\项目二\成品\数据\13~22.csv', 'a', encoding='utf-8') as f2:  # 打开文本写入文件
                for e, p in zip(year, fangjia):  # 使用zip函数并排输出
                    f2.write(str(e) + ',' + str(p) + '\n')
# -----------------------------替换数据段---------------------
# with open('./13~22.csv', 'r', encoding='utf-8') as f3:
#
#     with open('./data.csv', 'a', encoding='utf-8') as f4:
#
#         for i in f3.readlines():#.replace(' ', '')
#
#             f4.write(i.replace('元/㎡', ''))#将元/㎡替换为空写入
f2.flush()
f2.close()
# 关闭文件
