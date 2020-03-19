import requests
import os
#r = requests.get("http://python123.io/ws")
#print(r.status_code)
#print(r.encoding)
'''
url = "https://item.jd.com/100004770249.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
    #print(r.text)

except:
    print("爬取失败")
'''

print('-----------------------')
'''
#亚马逊爬取失败
url = "https://www.amazon.cn/dp/B0832B8HFJ/ref=lp_665002051_1_5?s=wireless&ie=UTF8&qid=1583390051&sr=1-5"
try:
    kv = {'user_agent': 'Mozilla/5.0'} #模拟浏览器发送请求
    r = requests.get(url,headers=kv)
    #print(r.status_code) 查看状态吗，是否请求成功
    #print(r.request.headers)  获取头部查看user-agent
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬去失败")
'''
'''
#百度搜索360关键词提交
try:
    kv = {'wd':'Python'}
    r = requests.get("https://www.baidu.com/s",params=kv)
    print(r.status_code)
    print(r.request.url)
    r.raise_for_status()   #输出错误信息
    print(len(r.text))
except:
    print("爬取失败")
    
'''


#网络图片的爬取
url = "https://new-bxgstorge.boxuegu.com/smooc/P02/019.mp4"
#"http://202.207.82.51/dest/41b/41b04f41-a106-4e64-86e7-2a0d2052db29.mp4"
root = "D://"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件保存成功")
except:
    print("爬取失败")



'''
#ip归属地查询失败，可能因为自己电脑定位的问题
#url = 'http://www.ip138.com/iplookup.asp?ip='
#url = 'http://m.ip138.com/iplookup.asp?ip=202.204.80.112'
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)

    r.text[-500:]  #返回文本的最后500字节
except:
    print('爬取失败')
'''

