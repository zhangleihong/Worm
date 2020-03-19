import requests
import re
import bs4
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
#print(demo)
'''
#标签树的下行遍历
soup = BeautifulSoup(demo,"html.parser")
#print(soup.head.title.contents)
print(len(soup.body))
for child in soup.body.children:
    print(child)
'''
'''
#标签树的上行遍历
soup = BeautifulSoup(demo,"html.parser")
#print(soup.head.title.contents)
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
'''
'''
#标签树的平行遍历:发生在同一个父节点
soup = BeautifulSoup(demo,"html.parser")
for sibling in soup.a.next_siblings:
    print(sibling)
for sibling in soup.a.previous_siblings:
    print(sibling)
'''
'''
#基于bs4库的html编码美化
soup = BeautifulSoup(demo,"html.parser")
print(soup)
print(soup.head.prettify())
'''
'''
#html信息提取的一般方法
for link in soup.find_all('a'):
    print(link.get('href'))
'''
'''
#基于bs4库的html查找方法
#.find_all(name,attrs,recursive,string,**kwargs)
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

print(soup(re.compile('b')))
'''

#中国大学排名定向爬取
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            #print(tds[3].string)

            ulist.append([tds[0].string,tds[1].string,tds[3].string])


def printUnivList(ulist,num):
    tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:{3}^10}"
    print(tplt.format("排名","学校名称","综合得分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
main()

