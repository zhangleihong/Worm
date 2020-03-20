
import requests
from lxml import etree
import json
from pprint import pprint

# 1.1访问英雄列表页
response = requests.get(
    url="https://pvp.qq.com/web201605/js/herolist.json",
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
)
#response.encoding = response.apparent_encoding
json_string = response.text
#print(type(response.text))
heros = json.loads(json_string)
items = []
for hero in heros:
    item = {}
    item["hero_name"] = hero["cname"]
    item["skill_list"] = []

    print(hero)


    detail_url = "https://pvp.qq.com/web201605/herodetail/{}.shtml".format(hero["ename"])
    detail_response = requests.get(
        url=detail_url,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }
    )
    html = detail_response.content.decode('gbk')
    detail_eroot = etree.HTML(html)
    skills_list_divs = detail_eroot.xpath('//div[@class="show-list"]')
    for skill_div in skills_list_divs:
        skill = {}
        skill_name = skill_div.xpath('./p[@class="skill-name"]/b/text()')
        if len(skill_name)==0:
            continue
        else:
            skill["skill_name"] = skill_name[0]
        skill_desc = skill_div.xpath('./p[@class="skill-desc"]/text()')
        if len(skill_desc) == 0:
            continue
        else:
            skill["skill_desc"] = skill_desc[0]
        item["skill_list"].append(skill)
    items.append(item)

with open("王者技能英雄列表.json",'w',encoding='utf-8') as f:
    json.dump(items,f,ensure_ascii=False,indent=2)

#print(html)
# 1.2从页面中提取英雄得详情链接
# eroot = etree.HTML(html)
# href = eroot.xpath('//ul[@class="herolist clearfix"]/li/a/@href')
# print(href)