import urllib.request
import re
import json

from pymysql import Connection
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)
# 选择数据库
conn.select_db("demo")
cursor = conn.cursor()

def list(page):
    url = f'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start={page}&limit=10'
    headers = {
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(request).read()
    msgs = json.loads(content)
    id = 0
    for msg in msgs :
        sql = f"insert into douban(id,title,actors,rating) values('{page}{id}','{msg['title']}','{msg['actors'][0]}','{msg['rating'][0]}')"
        print(sql)
        id = id + 1
        cursor.execute(sql)
        conn.commit()
        # print(msg['actors'][0])
        #                 # print(msg['title'])
        #                 # print(msg['rating'])

# list(0)
i = 0
while(i<=50):
    list(i)
    i = i+10
    print(">>>>>>>>>>>>")

conn.close()