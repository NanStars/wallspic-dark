import requests
import join
import requests
import os
from lxml import etree


def getHTMLText(url):
    cookie = 'sessionid=551b521f-fe51-4289-b9ca-19a61ad9f02b; Hm_lvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1677033844,1677124877; _fromcat=category; js=1; dt_auth=eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NzcxMzk5MzEsImV4cCI6MTY3Nzc0NDczMSwic3ViIjoi5rWu55Sf5rGd5qKmIiwiaWQiOjI2MzI1ODU1LCJwbGF0Zm9ybSI6IldFQiIsInZlcnNpb24iOjF9.l9DXWHqOGoQA_ubIatCr2dLW9SlRFSZJR0lvJs22wxs; _auth_user_id=26325855; username=%E6%B5%AE%E7%94%9F%E6%B1%9D%E6%A2%A6; Hm_lpvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1677139930'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Cookie': cookie
    }
    try:
        r = requests.get(url, headers=headers, timeout=30)
        # r = requests.get(url, headers=headers,timeout=30,proxies=get_random_ip(ip_list))
        r.raise_for_status()
        r.encoding = 'utf-8'
        text = r.text

        return text
    except:
        return 'xx'


def Get_thumbnail_links(html_text):

    list_lue = []

    # 实例化etree对象
    tree = etree.HTML(html_text)
    # 提取出高清图所在页面地址
    # //*[@id="woo-holder"]/div[1]/div[2]/div[1]/div/div[1]/a
    r = tree.xpath('//div[@class="mbpho"]//a/@href')
    print(list_lue)
    newlist = list(filter(lambda x: x != 'javascript:;', r))
    print(newlist)

    return list_lue


if __name__ == '__main__':
    Get_thumbnail_links(getHTMLText('https://www.duitang.com/category/?cat=wallpaper'))
