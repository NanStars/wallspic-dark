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
from tqdm import tqdm

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.75 Mobile Safari/537.36 '
}


# 实现爬取前10页略缩图片地址，并存放在列表中
def lue(shouye, weiye):
    list_lue = []
    for i in range(int(shouye), 1 + int(weiye)):
        if i > 1:
            url = f'http://www.netbian.com/shouji/index_{i}.htm'  # http://www.netbian.com/shouji/dongman/index_2.htm
        else:
            url = 'http://www.netbian.com/shouji/index.htm'
        response_text = requests.get(url, headers=headers, timeout=15).text

        # 实例化etree对象
        tree = etree.HTML(response_text)
        # 提取出高清图所在页面地址
        r = tree.xpath('/html/body/div[2]/div[2]/div[3]/ul/li/a/@href')
        for i in r:
            list_lue.append(i)
    return list_lue


# 获取高清图下载地址及名称
def gao(b, weijian_name):
    if not os.path.exists('./' + weijian_name + '/'):
        os.mkdir('./' + weijian_name + '/')
    for i in b:
        url = "http://www.netbian.com/" + ''.join(i)  # 高清图所在页面地址
        response = requests.get(url=url, headers=headers, timeout=15)
        response.encoding = 'gbk'  # 解决中文乱码
        response_text = response.text
        tree = etree.HTML(response_text)
        # 第二图片页面地址
        img_src = 'http://www.netbian.com/' + ''.join(tree.xpath('/html/body/div[2]/div[2]/div[3]/div/p/a/@href'))
        print(img_src)

        response2 = requests.get(url=img_src, headers=headers, timeout=15)
        response2.encoding = 'gbk'  # 解决中文乱码
        response_text2 = response2.text
        tree2 = etree.HTML(response_text2)
        # 最终图片地址
        img_src2 = ''.join(tree2.xpath('/html/body/div[2]/div[2]/table/tr/td/a/@href'))
        # 图片名
        img_name = ''.join(tree2.xpath('/html/body/div[2]/div[2]/table/tr/td/a/@title'))
        resp = requests.get(img_src2, stream=True)
        total = int(resp.headers.get('content-length', 0))
        # 获取图片二进制数据
        img_path = './' + weijian_name + '/' + img_name + '.jpg'
        with open(img_path, 'wb') as f, tqdm(
                desc=img_name,
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)
            print(img_name + '.jpg下载完毕')
    print("手机图片全部下载完毕！")


def main():
    print(' _____ _                  _   _                     _  ')
    print('|_   _| |__   ___    ___ | |_| |__   ___ _ __   ___| |__   ___  _ __ ___ ')
    print("  | | | '_ \ / _ \  / _ \| __| '_ \ / _ \ '__| / __| '_ \ / _ \| '__/ _ \ ")
    print('  | | | | | |  __/ | (_) | |_| | | |  __/ |    \__ \ | | | (_) | | |  __/ ')
    print('  |_| |_| |_|\___|  \___/ \__|_| |_|\___|_|    |___/_| |_|\___/|_|  \___| ')
    print('  Author: Thinking about the wind')
    print('彼岸桌面壁纸下载工具'.center(35, '-'))
    shouye = input('请输入爬取的始页：')
    weiye = input('请输入爬取的尾页：')
    b = lue(shouye, weiye)
    wenjian_name = input("输入文件分类:")
    gao(b, wenjian_name)


if __name__ == '__main__':
    main()
    a = input("请输入退出：")
    if a == a:
        print("程序退出")
