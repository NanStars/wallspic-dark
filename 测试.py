import requests
import os
from lxml import etree
import time

'''
a_list = ['a', 'b', 'mpilgrim', 'z', 'example']

for i, v in enumerate(a_list):
    print('列表的第', i, '个元素是：', v)
b = input('id:')
print(a_list[int(b)])
'''


def Request_header():
    cookie = '__gads=ID=cbc8b229f437bf14-22ed7dee3dda009d:T=1677557737:RT=1677557737:S=ALNI_MbLz4A_lyuE_h1EOn7gZ' \
             '-zAElaG9g; ' \
             '__gpi=UID=00000bce0a6f8ac0:T=1677557737:RT=1677642242:S=ALNI_MbUHhZoqhNp10M3hIjIcjbD93bKzg '
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
              'Coolie': cookie}
    return header


def main_html(url, header):
    i = 0
    while i < 3:
        try:
            r = requests.get(url, headers=header, timeout=30)
            r.encoding = 'utf-8'
            main_html_1 = r.text
            return main_html_1
        except requests.exceptions.RequestException:
            i += 1


# 需要爬取几页主页函数
def each_page(home_page, last_page):
    list_main_html = []
    for i in range(int(home_page), 1 + int(last_page)):
        if i > 1:
            url = f'https://wallpaperscraft.com/catalog/art/page{i}'
        else:
            url = 'https://wallpaperscraft.com/catalog/art'
        list_main_html.append(url)
    return list_main_html


# 获取第二页url函数
def Get_the_second_page_connection(header):
    list_second_url = []
    for o in each_page(1, 2):
        html = main_html(o, header)
        time.sleep(2)
        Second_page_html = etree.HTML(html)
        Second_page_url = Second_page_html.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/ul/li/a/@href')
        for i in Second_page_url:
            Full_link_to_the_second_page = 'https://wallpaperscraft.com' + ''.join(i)
            # print(Full_link_to_the_second_page)
            list_second_url.append(Full_link_to_the_second_page)
    return list_second_url


# 获取第三页url函数
def Get_the_third_page_url(header):
    list_third_url = []
    for u in Get_the_second_page_connection(header):
        Third_html = main_html(u, header)
        time.sleep(2)
        Third_page_html = etree.HTML(Third_html)
        Third_page_url = Third_page_html.xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div/div[2]/div/div[1]/span[2]/a/@href')
        for i in Third_page_url:
            Full_link_to_the_third_page = 'https://wallpaperscraft.com' + ''.join(i)
            list_third_url.append(Full_link_to_the_third_page)
            # print('第三次url：', Full_link_to_the_third_page)
    return list_third_url


def Get_name(header):
    list_name = []
    for i in Get_the_third_page_url(header):
        Get_name_html = main_html(i, header)
        time.sleep(2)
        Get_name_html_page = etree.HTML(Get_name_html)
        Get_name_html_text = ''.join(
            Get_name_html_page.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/h1/text()')).strip()
        list_name.append(Get_name_html_text)
    print(list_name)
    return list_name


def Get_download_link(header):
    list_download_url = []
    for i in Get_the_third_page_url(header):
        Download_page = main_html(i, header)
        time.sleep(2)
        Download_page_html = etree.HTML(Download_page)
        Download_page_url = ''.join(
            Download_page_html.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/a/@href'))
        list_download_url.append(Download_page_url)
        print(Download_page_url)
    return list_download_url


def Download_pictures(header):
    if not os.path.exists('./测试/'):
        os.mkdir('./测试/')
    for i in Get_download_link(header):
        print(i)
        img = requests.get(i, headers=header, timeout=50).content
        time.sleep(2)
        for o in Get_name(header):
            img_path = './测试/' + o + '.jpg'
            with open(img_path, 'wb') as f:
                f.write(img)
            print(o + '.jpg下载完毕')


def main():
    Download_pictures(Request_header())


if __name__ == '__main__':
    main()
