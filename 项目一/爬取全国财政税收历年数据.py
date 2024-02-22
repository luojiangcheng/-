import csv
from urllib import request
from lxml import etree


def initUrls():
    urls = ['https://finance.gotohui.com/fdata-0/0000']
    return urls


def get(urls):
    # 爬取数据
    for url in urls:
        data = request.urlopen(url).read().decode('utf-8')
        # data = 'test1 data!'
        pData = parse(data)
        out(pData)


def parse(data):
    # 解析和提取数据
    pData = etree.HTML(data)
    # items = pData.xpath('//*[@id="finance_login"]//td[1]/a')
    items = pData.xpath('//*[@id="finance_login"]//tr')[1:]

    itemDatas = []
    for item in items:
        itemData = {}
        # itemData['zzs'] = item.xpath('./td/text()')[4]
        tds = item.xpath('./td')
        texts = tds[0].xpath('//text()')
        itemData['year'] = '' if (len(texts) == 0) else texts[0]

        texts = tds[0].xpath('.//text()')
        itemData['year'] = '' if (len(texts) == 0) else texts[0]
        texts = tds[1].xpath('.//text()')
        itemData['gjczsr'] = '' if (len(texts) == 0) else texts[0]
        texts = tds[2].xpath('.//text()')
        itemData['gjczzc'] = '' if (len(texts) == 0) else texts[0]
        texts = tds[3].xpath('.//text()')
        itemData['sssr'] = '' if (len(texts) == 0) else texts[0]
        texts = tds[4].xpath('.//text()')
        itemData['zzs'] = '' if (len(texts) == 0) else texts[0]
        texts = tds[5].xpath('.//text()')
        itemData['grsds'] = '' if (len(texts) == 0) else texts[0]
        texts = tds[6].xpath('.//text()')
        itemData['cysds'] = '' if (len(texts) == 0) else texts[0]

        itemDatas.append(itemData)
    return itemDatas


def out(data):
    # print(data)
    with open('data.csv', 'w', encoding='utf-8', newline='') as f:
        csvf = csv.DictWriter(f, fieldnames=['year', 'gjczsr', 'gjczzc', 'sssr', 'zzs', 'grsds', 'qysds'])
        # print(csvf)
        csvf.writeheader()
        csvf.writerows(data)


get(initUrls())
