import requests
from lxml import etree
import time

# 循环页码

for i in range(2011, 2023):
    url = 'https://www.anjuke.com/fangjia/yueyang/' + str(i) + '/'  # 将页码带入

    # 设置请求头，防止反爬
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
        'cookie': 'aQQ_ajkguid=1B666CC2-9A23-4912-9B81-B1796C58FB42; sessid=2A53E01A-B54F-4C1C-B361-0BF3BF4FC6EE; '
                  'ajk-appVersion=; id58=CrIcnGM8IidIO8ehB2+tAg==; isp=true; 58tj_uuid=25c7e159-6ebe-43cb-a5d4-1e1e68492ffc; als=0; '
                  'wmda_uuid=d910984001b396cca7704cbbc837378d; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; wmda_uuid=4fa65738187b6eb3d07011fd4f3a038b; '
                  'wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; _ga=GA1.2.456159365.1668683385; '
                  'xxzl_cid=05d084ccf0c147698dac291254e0f4c3; xxzl_deviceid=/vaTgRBpc++WFogUUOQC0vsCtaRHU67P8bLLDd4XQWKzkqHOnki/W48/sjglh6fV; seo_source_type=2; '
                  'init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DgH8Cha0N-Kn-IeBH-LDU4QK6uW9YvNtzvIAEMYsgvGSxr0Dc9yVQXJf-1Dw-'
                  'TBJV%2526wd%253D%2526eqid%253Deaaf1bd600013d9900000005637a074a; new_uv=15; new_session=0; '
                  'fzq_h=97de1f807257b012559c21f8ecebb961_1668943421175_ec50730f5f534b54beb5de5974c85322_974423890; twe=2; '
                  'wmda_session_id_6289197098934=1668943570984-6d6640f5-d9bb-5085; _gid=GA1.2.1927314721.1668943658; ctid=139; '
                  'obtain_by=2; '
                  'xxzl_cid=b384580712dc41a487ff99a1b8604ca6; xxzl_deviceid=6vabLTj0XjGCI0Lgn5tqvrp8aVikJpWEv1JYAXYtXSd4HYzXgSwnjE'
                  '/F2kicUKcT '
    }
    # 发送请求，获取网页源代码
    resp = requests.get(url, headers=headers)
    # 将网页源代码转换为，HTML文本供xpath，筛选
    data = etree.HTML(resp.text)
    # print(resp.text)
    # 时间路径
    year = data.xpath('/html/body/div[2]/div[3]/div/div/ul/li[1]/a/b/text()')
    # 房价路径
    jiage = data.xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul/li/a/span/text()')
    # 房价变化情况路径
    zt = data.xpath('/html/body/div[2]/div[5]/div[1]/div[1]/ul/li/a/em/text()')
    time.sleep(2)
    # 将爬取的数据写入文本
    with open('./房价变化', 'a', encoding='utf-8') as f:
        # for i in range(len(jiage)):
        time.sleep(0.5)
        # for i in range(len(jiage)):
        # 将数据依次循环写入
        for e, t, r in zip(year, jiage, zt):
            f.write(str(e) + ',' + str(t[:4]) + ',' + str(r) + '\n')

# 写入完毕，关闭文本
f.flush()
f.close()
