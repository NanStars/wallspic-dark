import requests
import os
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}


# 实现爬取前10页略缩图片地址，并存放在列表中
def lue():
    list_lue = []

    url = 'https://www.duitang.com/blogs/tag/?name=%E6%A8%AA%E5%B1%8F%E5%A3%81%E7%BA%B8'
    response_text = requests.get(url, headers=headers, timeout=15).text

    # 实例化etree对象
    tree = etree.HTML(response_text)
    # 提取出高清图所在页面地址
    r = tree.xpath('/html/body/div[2]/div[2]/div[3]/ul/li/a/@href')
    for i in r:
        list_lue.append(i)
    return list_lue


# 获取高清图下载地址及名称
def gao(b):
    if not os.path.exists('./手机壁纸女生/'):
        os.mkdir('./手机壁纸女生/')
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
        # 获取图片二进制数据
        img_content = requests.get(img_src2, headers=headers, timeout=10).content
        img_path = './手机壁纸女生/' + img_name + '.jpg'
        with open(img_path, 'wb') as f:
            f.write(img_content)
        print(img_name + '.jpg下载完毕')
    print("手机图片全部下载完毕！")


def main():
    b = lue()
    gao(b)


if __name__ == '__main__':
    main()
