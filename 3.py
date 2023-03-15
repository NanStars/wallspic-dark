# www.duitang.com
# 20200603 by WX:huguo00289

# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
import urllib.parse
import requests, time, os, json


def ua():
    ua = UserAgent()
    headers = {'User-Agent': ua.random,
               'Cookie': 'sessionid=ef6912ba-38d9-4b6e-a3d9-8d6526805f07; js=1; Hm_lvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1590492733,1591182385; Hm_lpvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1591182414'}
    # headers = {'User-Agent': ua.random}
    return headers


def get_imgs(i, keyword):
    kd = urllib.parse.quote(keyword)
    #https://www.duitang.com/napi/blog/list/by_search/?include_fields=like_count%2Csender%2Calbum%2Cmsg%2Creply_count%2Ctop_comments&kw=%E5%A3%81%E7%BA%B8&start=38&_=1677132654699
    url = f'https://www.duitang.com/napi/blog/list/by_search/?include_fields=like_count%2Csender%2Calbum%2Cmsg%2Creply_count%2Ctop_comments&kw={kd}&start={1*i}&_=1677132654699'
    #url = f"https://www.duitang.com/napi/blog/list/by_search/?kw={kd}&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start={24 * i}&_=159118241418{i}"
    html = requests.get(url, headers=ua(), timeout=8).content.decode('utf-8')
    time.sleep(1)
    datas = json.loads(html)
    object_lists = datas['data']['object_list']
    print(len(object_lists))
    for object_list in object_lists:
        print(object_list)
        img_url = object_list['album']['covers'][0]
        img_name = '%s%s' % (object_list['album']['id'], os.path.splitext(img_url)[1])
        print(img_url, img_name)
        down_img(img_url, img_name, keyword)


def down_img(img_url, img_name, keyword):
    os.makedirs(f'{keyword}/', exist_ok=True)  # 创建目录
    r = requests.get(img_url, headers=ua(), timeout=5)
    with open(f'{keyword}/{img_name}', 'wb') as f:
        f.write(r.content)
    print(f'>>>保存{img_name}图片成功！')


def main(keyword):
    for i in range(1, 10):
        print(f'>>>正在爬取第{i}页图片内容')
        get_imgs(i, keyword)

    print('采集图片完毕！')


if __name__ == '__main__':
    main("壁纸")
