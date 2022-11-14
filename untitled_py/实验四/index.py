import urllib.request
import re
import json

def getMsgAll(page,score):
    url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100014352549&score={score}&sortType=5&pageSize=10&page={page}'
    headers = {
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(request).read().decode('gbk')
    print(content)
    msg = re.findall('(?<=\()(.*?)(?=\);)',content)
    msg = json.loads(msg)
    comments = msg['comments']
    for comment in comments:
        print("评论：",str(comment["content"]))

i = 1
print("全部评论：score = 0>>>>>》》>>>>>>>>>>>>>>>>>>>>>>>>>>>")
while (i<=5):
    getMsgAll(i,0)
    i = i+1
i = 0
print("好：score = 3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

while (i<=5):
    getMsgAll(i,3)
    i = i+1

i = 0
print("追：score = 5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


while (i<=5):
    getMsgAll(i,5)
    i = i+1
i = 0

print("中：score = 2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

while (i<=2):
    getMsgAll(i,2)
    i = i+1

print("差：score = 1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

while (i<=2):
    getMsgAll(i,1)
    i = i+1
