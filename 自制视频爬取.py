import requests
import os
from lxml import etree

response = requests.get(
    # 设置请求地址
    url="http://stu.ityxb.com/preview/detail/24a9b488aa194725877ef199c7246032",
    # 设置请求头
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
)
response.encoding = response.apparent_encoding
html = response.text
#print(html)
#王丽颖json1
#url = "http://encrypted.boxuegu.com/bxg/userUpload/8a12b8c9-899f-c7d3-b8b0-4ede3a941334.mp4"
#王丽颖json2
#html = "http://stu.ityxb.com/preview/detail/24a9b488aa194725877ef199c7246032"
detail_eroot = etree.HTML(html)
src = detail_eroot.xpath('//video/@src')
print(src)
#网络图片的爬取
#王者荣耀爬虫视频
#url = "https://new-bxgstorge.boxuegu.com/smooc/P02/019.mp4"
'''
root = "D://"
path = root + src.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(src)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件保存成功")
except:
    print("爬取失败")

'''