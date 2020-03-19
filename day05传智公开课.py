import requests
from lxml import etree
# 网页存到本地
'''
try:
    #kv = {'wd':'Python'}
    kv = {'user_agent': 'Mozilla/5.0'}
    r = requests.get("https://search.bilibili.com/all?keyword=MP3",headers=kv)
    print(r.status_code)
    print(r.request.url)
    r.raise_for_status()   #输出错误信息
    r.encoding = r.apparent_encoding
    print(len(r.text))
    with open('01-获取响应内容.html','w',encoding='utf-8') as f:
       f.write(r.text)
except:
    print("爬取失败")
'''

# xpath语法学习
'''
# html = ''''''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>语法学习</title>
</head>
<body>
    <bookstore>
        <book category="COOKING">
          <title lang="en">Everyday Italian</title>
          <author>Giada De Laurentiis</author>
          <year>2005</year>
          <price>30.00</price>
        </book>
        <book category="CHILDREN">
          <title lang="en">Harry Potter</title>
          <author>J K. Rowling</author>
          <year>2005</year>
          <price>29.99</price>
        </book>
        <book category="WEB">
          <title lang="en">Learning XML</title>
          <author>Erik T. Ray</author>
          <year>2003</year>
          <price>39.95</price>
        </book>
    </bookstore>
</body>
</html>



eroot = etree.HTML(html)
print(eroot.xpath('//book[@category="WEB"]/price/text()'))
'''

# XPath提取练习
response = requests.get(
    url="http://www.itcast.cn/channel/teacher.shtml",
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
)
#response.raise_for_status()
response.encoding = response.apparent_encoding
# 3. 处理响应
# 使用 XPath 对传智播客教师列表数据进行提取
eroot = etree.HTML(response.text)

# 利用 XPath 对网页内容进行提取
# 1> 提取包含老师信息的 DIV => //div[@class="li_txt"]
div_list = eroot.xpath('//div[@class="li_txt"]')

# 2> 从DIV 大标签内容中获取具体内容
for div in div_list:
    item = {}
    # 获取老师名称
    item["name"] = div.xpath('./h3/text()')[0]
    # 获取老师级别
    item["level"] = div.xpath('./h4/text()')[0]
    # 获取老师详细内容
    item["desc"] = div.xpath('./p/text()')[0]
    print(item)

