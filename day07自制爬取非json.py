
import requests
import requests as requests
from lxml import etree
import json
from pprint import pprint

# 1.1访问英雄列表页
response = requests.get(
    url="https://pvp.qq.com/web201605/herolist.shtml",
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
)
#response.encoding = response.apparent_encoding
html = response.content.decode('gbk')
#print(html)
# 1.2从页面中提取英雄得详情链接
eroot = etree.HTML(html)
hrefs = eroot.xpath('//ul[@class="herolist clearfix"]/li/a/@href')
#可以获取网页列表
#print(hrefs)
items = []
for href in hrefs:
    item = {}
    item["skill_list"] = []
    detail_url = "https://pvp.qq.com/web201605/"+href
    detail_response = requests.get(
        url=detail_url,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }
    )
    html2 = detail_response.content.decode('gbk')
    detail_eroot = etree.HTML(html2)
    item["hero_name"] = detail_eroot.xpath('//div[@class="cover"]/h2[@class="cover-name"]/text()')
    print(item["hero_name"])
    skills_list_divs = detail_eroot.xpath('//div[@class="show-list"]')
    for skill_div in skills_list_divs:
        skill = {}
        skill_name = skill_div.xpath('./p[@class = "skill-name"]/b/text()')
        if len(skill_name) == 0:
            continue
        else:
            print(skill_name)
            skill["skill_name"] = skill_name[0]
            print(skill_name[0])
        skill_desc = skill_div.xpath('./p[@class = "skill-desc"]/text()')
        if len(skill_desc) == 0:
            continue
        else:
            skill["skill_desc"] = skill_desc[0]
        item["skill_list"].append(skill)
    items.append(item)
with open("英雄技能列表.json",'w',encoding='utf-8') as f:
    json.dump(items,f,ensure_ascii=False,indent=2)


