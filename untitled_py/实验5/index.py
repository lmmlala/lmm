from pymysql import Connection
import urllib.request
import re
import json

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)
# 选择数据库
conn.select_db("demo")
cursor = conn.cursor()

def getMsgAll(page,score):
    url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100014352549&score={score}&sortType=5&pageSize=10&page={page}'
    headers = {
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'cookie':"__jdu=1654416444255322193629; shshshfpa=13c8c8dd-1809-bfa1-827d-b6cc9e19d81d-1654416445; shshshfpb=b308pYWc7rawVFT5mLizh7g; pinId=ElbdvDl6pTOnGOi4BqQ65LV9-x-f3wj7; areaId=18; unpl=JF8EAMhnNSttWEIHAUlQEkYVHFsDW1QNSB8CbG9VB1hbTwRWHgFPGkB7XlVdXhRLFx9ubxRUXVNIUQ4bBCsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwWFU5dU1tYDUgTB21kBlRVWkxXDSsDKxUge21WXVQISxczblcEZB8MF1MDGQMeFl1LWlBbWAhMEgZqZAFQX1tIVA0ZBRgaIEptVw; CCC_SE=ADC_uByI5pW+cEyjFh482+NwI2yBsXA5rUNPcqyu/YhLhX3vDoQkIMbwshDJMJQYklM7Gr4TejVyTHof6VxPCc7VUHD5TIgrK9sDlnEqVkCLk9lgjao9D8niBGhBYlP9ZHQ1leaQXAfTEcnfwf7ZNMFgodSxB8sp47tgRSLl5IPhMtBlbuWdXhHYd1SyfYaDElXcs3yvN6Y1hITs3uRLOMoQ60Kt88vchoWBe0oj6AwQKN4VEXICWD2zc04P0UBvtntWPYlcToVbfdG3Wna5oDOgpHEL8P/h/MsPRHhQa2842M8juY+OFtESXlYN8A84wtybH5M+CtRRR04Rvee3bbkGMDaOBVbK/nO7QnTam1JZMZby6P8YfjGQVR12IAk8D1OborrBX/EpAUYxQ8dhnWgcR/Fhz/7GNit7J65dyAJqRbCcHVmQsChJ6dpcJkj5Q0h/NwqLjiz8W+0Folh64TrotfpDXk6Sotx6PT6VIUhxelnDmPTyG4xyBvajpa1Wm8hMTf2HW3muiuCTYFj/2Gf6DETeB6kP1CC7B0o4ueJXmhDT0KwBjUxFZG7wSJvJdCKxJy0ufOJ+dTErAhQTrDLbWltu6aO2ZhIxDnb9+20pwksBcAh/Y0l2l0C1HtnJOagk; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_18b5cc8e4f7f48429029ab425ab42e9a|1667964256588; token=74dc56622f4ee87dca60a386c76eac69,2,926646; __tk=NfG3sIPfrcOdqfNBNATgqIqBqiqCrLaAscunOcuCrAa,2,926646; shshshfp=6665b657c6c0a61395b34783c3be744d; shshshsID=e9af3f12fdccad346f0fa12b3eb0c9a9_2_1667964270998; __jda=122270672.1654416444255322193629.1654416444.1667911641.1667964257.20; __jdb=122270672.2.1654416444255322193629|20.1667964257; __jdc=122270672; ip_cityCode=1495; ipLoc-djd=18-1495-1498-30785; 3AB9D23F7A4B3C9B=WGD3AI3OCCFGWOEMI5YSN2LR3ABBQDOOUIU7TZSZJUGK77XEQDKV76LPOGO44DI33GL6E4663S65FNZQCB2NUZLTQA; jwotest_product=99; JSESSIONID=A3A26B464447CA3DEDC77BBEAD07C899.s1"
    }
    request = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(request).read().decode('gbk')
    msg = re.findall('(?<=\()(.*?)(?=\);)',content)[0]
    msg = json.loads(msg)
    comments = msg['comments']
    id = 0
    for comment in comments:
        sql = f"insert into score{score}(id,msg) values('{page}{id}','{comment['content'][0:20]}')"
        print(sql)
        id = id+1
        cursor.execute(sql)
        conn.commit()

# 插入追评 score = 5
i = 0
while (i<=5):
    getMsgAll(i,5)
    i = i+1
#  好评 score = 3
i=0
while(i<5):
    getMsgAll(i,3)
    i = i+1
#  差评 score = 1
i=0
while(i<5):
    getMsgAll(i,1)
    i = i+1

conn.close()