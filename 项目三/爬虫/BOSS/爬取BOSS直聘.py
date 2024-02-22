import time
import requests
import random

uas = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]
def fake_user_agent():
    return random.choice(uas)

with open(r'D:\LJH\local\python\项目\项目三\爬虫\BOSS\地址.txt', 'r', encoding='UTF-8') as f:
    for g in f.readlines():
        for i in range(1, 11):

            # 爬四页需要换一次cookieb
            cookies = {
                'Cookie':'wd_guid=868b5c03-425b-4256-ab0a-380d902802e4; historyState=state; YD00951578218230%3AWM_TID=NKh5IclJo7hEUUUFURbFmLXgzp6weJKw; _bl_uid=y7l6nmb2yOszXvfte0Is79Cc1dq4; lastCity=101070300; sid=sem_pz_bdpc_dasou_title; __zp_seo_uuid__=8ef7c65d-1a4f-425c-85f3-2d2334fc052a; __g=sem_pz_bdpc_dasou_title; __l=r=&l=%2Fwww.zhipin.com%2Fchengshi%2Fc101070300%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&s=1&g=%2Fwww.zhipin.com%2Fchengshi%2Fc101070300%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1698980486,1701175997; boss_login_mode=sms; gdxidpyhxdE=MM4c5RAZPvO2mdoy2w4ptN4i9ymiGUjj%2F2n3BaJTJpYYmZ%2BeAkigf54jsmJnJNR465Os3zi3Lsyg03Jy14eCvwOlQaL60zkjmynsTi3v%2BRYNZaJt%2FMVpK4dDr%2BHtkb6OnZRf2ehgM2R62c3%2Fs7u3CPcwu%2FMx6vwyCyQ%2BihHkpRHdVhyy%3A1701176911565; YD00951578218230%3AWM_NI=%2FtnFG%2Fea90TyDZ1Thjjfszz7AStahpngrBSf1rBPvo3vv1FR0H7SuN5IWPt4yoIM7XR0E7CC%2Bpj1MvgzNFbUWDN42naPQgWsgBaFhwwrsh57aaPlvlmh%2FImVREZp8xQpc2I%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee9bbc5ca5b48bd8c665fc928eb3d15e968b9a83d47c9692a697ae6bb4ef84b6cb2af0fea7c3b92aedaca2a7c625a7bff7d1d7738886ffb5eb62aababd9bf93d838dbc82eb7caeb9bea3d26ef3ae8eb1f565f1aabad2c55af498f9b4f846f79799b1f740bbb187aeb65492f08bd8c249e9b0a6d2d07ea5a682a7e15f959c82d5b166a3909f88d679a59eafa7eb7db5aebd89b83da3bfa08df568afb8e1aaf05e929b9691bb7493b0add3cc37e2a3; wt2=D6zzdFP-je-J-kwnEqPD99wXid7DyiLMo65GCUuLgd-GYCzmgkejeQwMeNkdzvBBaH8M15-dBgImBFfv8khXj_Q~~; wbg=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1701176048; __c=1701175997; __a=18963858.1695651476.1698980485.1701175997.39.7.9.9; geek_zp_token=V1RN0iFeP52V5rVtRuzxwZLiy29z9ezU8~; __zp_stoken__=0a91eGi9DZSprTmxdcHdYWG1GdkJIVj9oZTp9UUwiHCZBdhVdXVMnFQIqNjtBBxV%2BPGQcd2NdJWcMTTcVLwgeCT5GQTUAe2hrXEMpWhATZ0sRAzA7OAtYAwEufk4edTo1fl1GfTh9TwUwfjk%3D'

            }

            print(cookies)
            headers = {
                'user-agent': str(fake_user_agent())
            }
            print(headers)
            params = {
                'scene': '1',
                'query': '大数据',
                'city': str(g).strip(),
                'experience': '',
                'payType': '',
                'partTime': '',
                'degree': '',
                'industry': '',
                'scale': '',
                'stage': '',
                'position': '',
                'jobType': '',
                'salary': '',
                'multiBusinessDistrict': '',
                'multiSubway': '',
                'page': str(i),
                'pageSize': '30',
            }
            # time.sleep(2)
            time.sleep(10)
            session = requests.Session()
            response = requests.get(
                'https://www.zhipin.com/wapi/zpgeek/search/joblist.json',
                params=params,
                cookies=cookies,
                headers=headers,
                # proxies=proxies,
            ).json()
            if response['code'] == '0':
                with open('BOOSS岗位信息.csv', 'a', encoding='utf-8') as f2:
                    # print(response["code"])
                    for y in response["zpData"]['jobList']:
                        print(str(y['jobName'])+"\t"+str(y['jobExperience']) + '\t' + str(y['jobDegree']) + '\t' + str(
                            y['cityName']) + '\t' + str(y['areaDistrict']) + '\t' + str(y['businessDistrict']) + '\t' + str(
                            y['salaryDesc']) + '\t' + str(y['brandName']) + '\t' + str(".".join(y['skills']) + '\n'))
                        f2.write(
                            str(y['jobName'])+","+str(y['jobExperience']) + ',' + str(y['jobDegree']) + ',' + str(y['cityName']) + ','
                            + str(y['areaDistrict']) + ',' + str(y['businessDistrict']) + ',' + str(
                                y['salaryDesc']) + ',' + str(y['brandName'])
                            + ',' + str(".".join(y['skills']) + '\n'))
                print('以上是' + "{}".format(g) + "城市第" + "{}".format(i) + '页')
            else:
                time.sleep(20)


# 101280600深圳
# 101020100上海
# 101280100广州
# 101010100北京
# 101210100杭州
# 101250100长沙
# 101230200厦门
# 101200100武汉
# 101270100成都

