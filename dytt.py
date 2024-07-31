import re

import requests

head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
# 电影天堂
href0="https://www.dy2018.com"
# headers=head
response=requests.get(href0,verify=False)
response.encoding='gb2312'
content = response.text
# print(content)
child_href_list=[]

obj0 = re.compile("2023必看热片.*?<ul>(?P<ul>.*?)<ul>",re.S)
obj1=re.compile("<li><a href='(?P<href>.*?)'",re.S)

result0=obj0.finditer(content)
for i in result0:
    ul=i.group('ul')
    result1=obj1.finditer(ul)
    for j in result1:
        child_href=href0+j.group('href')
        child_href_list.append(child_href)

for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding='gb2312'
