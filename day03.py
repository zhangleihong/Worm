import requests
import re
import bs4
from bs4 import BeautifulSoup
'''
match = re.match(r'PY.*N','PYANBNCNDN')
if match:
    print(match.group(0))

match = re.search(r'PY.*?N', 'PYANBNCNDN')
if match:
    print(match.group(0))
regex = re.compile('PY.*?N')
match = regex.search('PYANBNCNDN')
if match:
    print(match.group(0))
'''

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt,html):
    print()
def printGoodsList(ilt):
    print()
def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    #https://s.taobao.com/search?initiative_id=staobaoz_20200307&q=%E4%B9%A6%E5%8C%85
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
main()