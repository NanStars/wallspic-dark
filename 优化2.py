import requests
import os
from lxml import etree
import time
import urllib3
from tqdm import tqdm

urllib3.disable_warnings()


def each_page(home_page, last_page):
    list_main_html = []
    for i in range(int(home_page), 1 + int(last_page)):
        if i > 1:
            url = f'https://wallpaperscraft.com/catalog/art/page{i}'
        else:
            url = 'https://wallpaperscraft.com/catalog/art'
        list_main_html.append(url)
    return list_main_html


def zong(url):
    cookie = '__gads=ID=cbc8b229f437bf14-22ed7dee3dda009d:T=1677557737:RT=1677557737:S=ALNI_MbLz4A_lyuE_h1EOn7gZ' \
             '-zAElaG9g; ' \
             '__gpi=UID=00000bce0a6f8ac0:T=1677557737:RT=1677642242:S=ALNI_MbUHhZoqhNp10M3hIjIcjbD93bKzg '
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
              'Coolie': cookie}
    i = 0
    while i < 3:
        try:
            list_second_url = []
            for o in url:
                html = requests.get(o, headers=header, timeout=30)
                html.encoding = 'utf-8'
                main_html_1 = html.text
                time.sleep(2)
                Second_page_html = etree.HTML(main_html_1)
                Second_page_url = Second_page_html.xpath(
                    '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/ul/li/a/@href')
                for i in Second_page_url:
                    Full_link_to_the_second_page = 'https://wallpaperscraft.com' + ''.join(i)
                    list_second_url.append(Full_link_to_the_second_page)
            # print(list_second_url)
            return list_second_url
        except requests.exceptions.RequestException:
            i += 1


def Get_the_third_page_url(url):
    cookie = '__gads=ID=cbc8b229f437bf14-22ed7dee3dda009d:T=1677557737:RT=1677557737:S=ALNI_MbLz4A_lyuE_h1EOn7gZ' \
             '-zAElaG9g; ' \
             '__gpi=UID=00000bce0a6f8ac0:T=1677557737:RT=1677642242:S=ALNI_MbUHhZoqhNp10M3hIjIcjbD93bKzg '
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
              'Coolie': cookie}
    i = 0
    while i < 3:
        try:
            list_third_url = []
            for o in url:
                html = requests.get(o, headers=header, timeout=30)
                html.encoding = 'utf-8'
                Third_html = html.text
                time.sleep(2)
                Third_page_html = etree.HTML(Third_html)
                Third_page_url = Third_page_html.xpath(
                    '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div/div[2]/div/div[1]/span[2]/a/@href')
                for i in Third_page_url:
                    Full_link_to_the_third_page = 'https://wallpaperscraft.com' + ''.join(i)
                    list_third_url.append(Full_link_to_the_third_page)
            # print(list_third_url)
            print("一共", len(list_third_url), 'url')
            return list_third_url
        except requests.exceptions.RequestException:
            i += 1


def Get_download_link(url, wenjian):
    if not os.path.exists('./' + wenjian + '/'):
        os.mkdir('./' + wenjian + '/')
    cookie = '__gads=ID=cbc8b229f437bf14-22ed7dee3dda009d:T=1677557737:RT=1677557737:S=ALNI_MbLz4A_lyuE_h1EOn7gZ' \
             '-zAElaG9g; ' \
             '__gpi=UID=00000bce0a6f8ac0:T=1677557737:RT=1677642242:S=ALNI_MbUHhZoqhNp10M3hIjIcjbD93bKzg '
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
              'Coolie': cookie}
    for o in url:
        html = requests.get(o, headers=header, timeout=30)
        html.encoding = 'utf-8'
        Download_page = html.text
        time.sleep(2)
        Download_page_html = etree.HTML(Download_page)
        Download_page_url = ''.join(
            Download_page_html.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/a/@href'))
        print('--------------------------------')
        print(Download_page_url)
        print('--------------------------------')
        Get_name = ''.join(Download_page_html.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/h1/text()')).strip()
        session = requests.Session()
        resp = session.get(url=Download_page_url, stream=True, timeout=30, verify=False, headers=header)
        total = int(resp.headers.get('content-length', 0))
        img_path = './' + wenjian + '/' + Get_name + '.jpg'
        with open(img_path, 'wb') as f, tqdm(
                desc=Get_name,
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)
            print(Get_name + '.jpg下载完毕')
            print('--------------------------------')
    print("全部下载完毕！")


if __name__ == '__main__':
    wenjian = input("请命名文件夹：")
    shouye = input("请输入爬取的第一页：")
    weiye = input("请输入爬取的最后一页：")
    print("正在获取url请稍等~~~~")
    a = each_page(int(shouye), int(weiye))
    b = zong(a)
    c = Get_the_third_page_url(b)
    Get_download_link(c, wenjian)
    exit = input('请输出退出：')
    if exit == '退出':
        print('退出中')
        time.sleep(2)

