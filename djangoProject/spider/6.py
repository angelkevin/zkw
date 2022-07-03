import requests
import re
import csv
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36'}

f = open('data.csv',mode='w',newline='')
csvwrite = csv.writer(f)
for i in range(0,250,25):
    url = f'https://movie.douban.com/top250?start={i}&filter='

    response = requests.get(url, headers=headers)

    page = response.text
    response.close()
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                     r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>', re.S)

    obj.finditer(page)
    for i in obj.finditer(page):
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        print(dic)
        csvwrite.writerow(dic.values())
f.close()

