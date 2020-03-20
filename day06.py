#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
爬取流程
1. 访问官方网站 -> 提取播放视频的详情页面地址
2. 访问视频的详情页面地址 -> 提取真正的视频播放地址
3. 根据视频播放地址下载视频

'''
import requests
from lxml import etree

# 1.1 访问官方网站获取官方网站的 html 内容
'''
模拟浏览器的需要分析的内容
url
    http://yun.itheima.com/
请求方式
    GET
请求头
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
'''
response = requests.get(
    # 设置请求地址
    url="http://yun.itheima.com/",
    # 设置请求头
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
)

html = response.text

# 1.2 从 html 内容中提取视频的详情页地址
eroot = etree.HTML(html)
hrefs = eroot.xpath('//div[@class="main"]/ul/li/a/@href')
for href in hrefs:
    detail_url = "http://yun.itheima.com" + href
    print(detail_url)
    # 2.1 访问详情页地址获取详情页的 HTML 内容
    '''
    请求详情页的分析
    url
        detail_url
    请求方式
        GET
    请求头
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
    '''
    detail_response = requests.get(
        url=detail_url,
        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }
    )
    detail_html = detail_response.text
    #print(detail_html)


    # 2.2 从详情页的 HTML 内容中提取 真正的视频播放地址
    detail_eroot = etree.HTML(detail_html)
    src = detail_eroot.xpath('//div[@class="con"]/ul/li[@class="click on"]/a/@data')

    if len(src) > 0:
        src = src[0]
        print(src)
    #print('--------------------------------------------------------------')
        # 3. 根据视频播放地址下载视频
        root = "D://"
        path = root + '1.mp4'
        with open(path,'wb') as f:
            # f 就是文件写入对象，如果想写入内容就可以调用
            # f.write(内容数据)
            # 使用 requests 进行下载文件
            video_response = requests.get(
                url=src,
                stream=True
            )
            print("正在下载:", src)
            # chunk_size 每下载 512 个字节数据就会回调一次
            for chunk in video_response.iter_content(chunk_size=512):
                 f.write(chunk)
    break
