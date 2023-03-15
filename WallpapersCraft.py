"""
//                            _ooOoo_
//                           o8888888o
//                           88" . "88
//                           (| -_- |)
//                            O\ = /O
//                        ____/`---'\____
//                      .   ' \\| |// `.
//                       / \\||| : |||// \
//                     / _||||| -:- |||||- \
//                       | | \\\ - /// | |
//                     | \_| ''\---/'' | |
//                      \ .-\__ `-` ___/-. /
//                   ___`. .' /--.--\ `. . __
//                ."" '< `.___\_<|>_/___.' >'"".
//               | | : `- \`.;`\ _ /`;.`/ - ` : | |
//                 \ \ `-. \_ __\ /__ _/ .-` / /
//         ======`-.____`-.___\_____/___.-`____.-'======
//                            `=---='
//
//         .............................................
//                  佛祖保佑             永无BUG
//          佛曰:
//                  写字楼里写字间，写字间里程序员；
//                  程序人员写程序，又拿程序换酒钱。
//                  酒醒只在网上坐，酒醉还来网下眠；
//                  酒醉酒醒日复日，网上网下年复年。
//                  但愿老死电脑间，不愿鞠躬老板前；
//                  奔驰宝马贵者趣，公交自行程序员。
//                  别人笑我忒疯癫，我笑自己命太贱；
//                  不见满街漂亮妹，哪个归得程序员？
"""

import requests
import os
from lxml import etree


def Request_header():
    cookie = '__gads=ID=cbc8b229f437bf14-22ed7dee3dda009d:T=1677557737:RT=1677557737:S=ALNI_MbLz4A_lyuE_h1EOn7gZ' \
             '-zAElaG9g; ' \
             '__gpi=UID=00000bce0a6f8ac0:T=1677557737:RT=1677642242:S=ALNI_MbUHhZoqhNp10M3hIjIcjbD93bKzg '

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
              'Coolie': cookie}

    return header


def main_html(url, header):
    """
    cookie = '__gads=ID=cbc8b229f437bf14-22ed7dee3dda009d:T=1677557737:RT=1677557737:S=ALNI_MbLz4A_lyuE_h1EOn7gZ' \
             '-zAElaG9g; ' \
             '__gpi=UID=00000bce0a6f8ac0:T=1677557737:RT=1677642242:S=ALNI_MbUHhZoqhNp10M3hIjIcjbD93bKzg '

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
              'Coolie': cookie}
              """
    r = requests.get(url, headers=header, timeout=30)
    r.encoding = 'utf-8'
    main_html_1 = r.text
    return main_html_1


def Get_the_second_page_connection(html):
    Second_page_html = etree.HTML(html)
    Second_page_url = Second_page_html.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/ul/li[1]/a/@href')
    # print(Second_page_url)
    # https://wallpaperscraft.com/wallpaper/artist_waves_colorful_129158
    Full_link_to_the_second_page = 'https://wallpaperscraft.com' + ''.join(Second_page_url)
    print(Full_link_to_the_second_page)
    return Full_link_to_the_second_page


def Get_the_third_page_url(second_page_url, header):
    Third_html = main_html(second_page_url, header)
    Third_page_html = etree.HTML(Third_html)
    Third_page_url = Third_page_html.xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div/div[2]/div/div[1]/span[2]/a/@href')
    # print(Third_page_url)
    Full_link_to_the_third_page = 'https://wallpaperscraft.com' + ''.join(Third_page_url)
    print(Full_link_to_the_third_page)
    return Full_link_to_the_third_page


def Get_download_link(third_url, header):
    Download_page = main_html(third_url, header)
    Download_page_html = etree.HTML(Download_page)
    Download_page_url = ''.join(
        Download_page_html.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/a/@href'))
    print(Download_page_url)
    return Download_page_url


def Download_pictures(Download_url, header):
    if not os.path.exists('./测试/'):
        os.mkdir('./测试/')
    img = requests.get(Download_url, headers=header, timeout=30).content
    img_path = './测试/' + '1.jpg'
    with open(img_path, 'wb') as f:
        f.write(img)
    print('.jpgDownload')

    pass


def main():
    header = Request_header()
    url = 'https://wallpaperscraft.com/catalog/art/page3'
    a = Get_the_second_page_connection(main_html(url, header))
    b = Get_the_third_page_url(a, header)
    c = Get_download_link(b, header)
    Download_pictures(c, header)


if __name__ == '__main__':
    main()
