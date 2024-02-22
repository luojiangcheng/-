# # J-N
#

import random
import requests
from lxml import etree
import time
import traceback
import time
import sys


def countDowd(sleep_time):
    for i in range(sleep_time, 0, -1):
        # 清除上一次的输出
        sys.stdout.write('\r')
        sys.stdout.flush()
        # 显示倒计时
        sys.stdout.write(f"{i}秒后再次请求，不用动程序！！！！！ ")
        sys.stdout.flush()
        time.sleep(1)
    # 清除最后一次输出
    sys.stdout.write('\r')
    sys.stdout.flush()


uas = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
]
coo = [
    "Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1698404777,1698413021,1698460402,1699343198; Hm_lvt_30606b57e40fddacb2c26d2b789efbcb=1698406273,1698413151,1699363229; Hm_lpvt_30606b57e40fddacb2c26d2b789efbcb=1699363229; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1699363281",
    "Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1698404777,1698413021,1698460402,1699343198; Hm_lvt_30606b57e40fddacb2c26d2b789efbcb=1698406273,1698413151,1699363229; Hm_lpvt_30606b57e40fddacb2c26d2b789efbcb=1699363229; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1699363294",
    "Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1698404777,1698413021,1698460402,1699343198; Hm_lvt_30606b57e40fddacb2c26d2b789efbcb=1698406273,1698413151,1699363229; Hm_lpvt_30606b57e40fddacb2c26d2b789efbcb=1699363229; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1699363317",
    "Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1698404777,1698413021,1698460402,1699343198; Hm_lvt_30606b57e40fddacb2c26d2b789efbcb=1698406273,1698413151,1699363229; Hm_lpvt_30606b57e40fddacb2c26d2b789efbcb=1699363229; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1699363347"
]
headers1 = {
    "User-Agent": str(random.choice(uas)),
    "Cookie": str(random.choice(coo))

}

url = 'https://lishi.tianqi.com/'

resp = requests.get(url, headers=headers1)

obj = etree.HTML(resp.text)

data = obj.xpath('//ul[@class="table_list"]/li/a/@href')
chenshi = obj.xpath('//ul[@class="table_list"]/li/a/text()')
# for w, e in zip(data, chenshi):
#     if w == 'yueyang':
#         url2 = url + w
urls = 'https://lishi.tianqi.com/yueyang'#url2.replace("/index.html", "")
for r in range(2018, 2023):
    flag = True
    for u in range(1, 13):
        if u < 10:
            headers = {
                "User-Agent": str(random.choice(uas)),
                "Cookie": str(random.choice(coo))

            }

            url3 = urls + '/' + str(r) + '0' + str(u) + '.html'
            print(url3)
            time.sleep(4)
            try:
                resp2 = requests.get(url3, headers=headers).text
                # if response.status_code == 200:
                # #     print("请求成功")......

                obj = etree.HTML(resp2)
                # print(resp.text)
                data2 = obj.xpath('//ul[@class="tian_two"]')
                for i in data2:
                    pjgaow = i.xpath('./li[1]/div[1]/div[1]/text()')
                    pjdiwen = i.xpath('./li[1]/div[2]/div[1]/text()')
                    jidaungaow = i.xpath('./li[2]/div[1]/text()')
                    jiduandiwen = i.xpath('./li[3]/div[1]/text()')
                    pjunkqzhishu = i.xpath('./li[4]/div[1]/text()')
                    hkqizuihao = i.xpath('./li[5]/div[1]/text()')
                    hkqizuihaorqi = i.xpath('./li[5]/div[2]/span/text()')
                    ckqizuicha = i.xpath('./li[6]/div[1]/text()')
                    ckqizuichariqi = i.xpath('./li[6]/div[2]/span/text()')
                    with open(r"C:\Users\昔日里\Desktop\波\数据\\" + '岳阳' + ".csv",
                              "a",
                              encoding="utf-8") as f2:
                        print('岳阳' + "," + str(r) + "-" + str(u) + "," + str(pjgaow) + "," + str(
                            pjdiwen) + "," + str(jidaungaow) + "," +
                              str(jiduandiwen) + "," + str(pjunkqzhishu) + "," + str(hkqizuihao) + "," + str(
                            hkqizuihaorqi) + "," + str(
                            ckqizuicha) + "," + str(ckqizuichariqi) + "\n")

                        f2.write('岳阳' + "," + str(r) + "-0" + str(u) + "," +
                                 str(pjgaow).replace("[", "").replace("]", "").replace("'", "") + "," +
                                 str(pjdiwen).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(jidaungaow).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(jiduandiwen).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(pjunkqzhishu).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(hkqizuihao).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(hkqizuihaorqi).replace("['(", "").replace(")']", "").replace("'", "") +
                                 "," + str(ckqizuicha).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(ckqizuichariqi).replace("['(", "").replace(")']", "").replace("'","") +
                                 "\n")
            except Exception as t:
                with open(r"C:\Users\昔日里\Desktop\波\数据\异常报告.txt", "a", encoding="utf-8") as f3:
                    f3.write(str(traceback.print_exc()) + "\n" + str(t) + "\n")
                    print(str(url3), str(traceback.print_exc()))
                    countDowd(100)
        else:
            headers = {
                "User-Agent": str(random.choice(uas)),
                "Cookie": str(random.choice(coo))

            }
            url3 = urls + '/' + str(r) + str(u) + '.html'
            print(url3)
            time.sleep(4)
            try:
                resp1 = requests.get(url3, headers=headers).text
                obj1 = etree.HTML(resp1)
                # print(resp1.text)
                data2 = obj1.xpath('//ul[@class="tian_two"]')
                for i in data2:
                    pjgaow = i.xpath('./li[1]/div[1]/div[1]/text()')
                    pjdiwen = i.xpath('./li[1]/div[2]/div[1]/text()')
                    jidaungaow = i.xpath('./li[2]/div[1]/text()')
                    jiduandiwen = i.xpath('./li[3]/div[1]/text()')
                    pjunkqzhishu = i.xpath('./li[4]/div[1]/text()')
                    hkqizuihao = i.xpath('./li[5]/div[1]/text()')
                    hkqizuihaorqi = i.xpath('./li[5]/div[2]/span/text()')
                    ckqizuicha = i.xpath('./li[6]/div[1]/text()')
                    ckqizuichariqi = i.xpath('./li[6]/div[2]/span/text()')
                    with open(r"C:\Users\昔日里\Desktop\波\数据\\" + '岳阳' + ".csv",
                              "a",
                              encoding="utf-8") as f2:
                        print('岳阳' + "," + str(r) + "-" + str(u) + "," + str(pjgaow) + "," + str(
                            pjdiwen) + "," + str(jidaungaow) + "," +
                              str(jiduandiwen) + "," + str(pjunkqzhishu) + "," + str(hkqizuihao) + "," + str(
                            hkqizuihaorqi) + "," + str(
                            ckqizuicha) + "," + str(ckqizuichariqi) + "\n")

                        f2.write('岳阳' + "," + str(r) + "-" + str(u) + "," +
                                 str(pjgaow).replace("[", "").replace("]", "").replace("'", "") + "," +
                                 str(pjdiwen).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(jidaungaow).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(jiduandiwen).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(pjunkqzhishu).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(hkqizuihao).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(hkqizuihaorqi).replace("['(", "").replace(")']", "").replace("'", "") +

                                 "," + str(ckqizuicha).replace("[", "").replace("]", "").replace("'", "") +
                                 "," + str(ckqizuichariqi).replace("['(", "").replace(")']", "").replace("'","") +
                                 "\n")
            except Exception as t:
                with open(r"C:\Users\昔日里\Desktop\波\数据\异常报告.txt", "a", encoding="utf-8") as f4:
                    f4.write(str(traceback.print_exc()) + "\n" + str(t) + "\n")
                    print(str(url3), str(traceback.print_exc()))
                    countDowd(100)
