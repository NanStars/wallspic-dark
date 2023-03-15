import requests
import os
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}


# 实现爬取前10页略缩图片地址，并存放在列表中
def lue():
    list_lue = []
    for i in range(1, 11):
        if i > 1:
            url = f'http://www.netbian.com/shouji/dongman/index_{i}.htm'  # http://www.netbian.com/shouji/dongman/index_2.htm
        else:
            url = 'http://www.netbian.com/shouji/dongman/index.htm'
        response_text = requests.get(url, headers=headers, timeout=15).text
        print(response_text)

        # 实例化etree对象
        tree = etree.HTML(response_text)
        # 提取出高清图所在页面地址
        r = tree.xpath('/html/body/div[2]/div[2]/div[3]/ul/li/a/@href')
        print(r)

        for i in r:
            list_lue.append(i)
    return list_lue




if __name__ == '__main__':
    lue()
