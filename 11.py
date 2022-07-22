import requests
from bs4 import BeautifulSoup
from fontTools import encodings
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re

headers = {
    'authority': 'www.ebay.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

url = 'https://www.ebay.com/'
driver = webdriver.PhantomJS()
driver.get(url)
driver.find_element_by_xpath('//*[@id="gh-ac"]').send_keys('tools') #搜索的东西
driver.find_element_by_xpath('//*[@id="gh-btn"]').click()
url1 = driver.current_url
url_new = url1 + '&_stpos=2128&_fcid=15'
url_list = [
    url_new+'&_pgn=1',
    url_new + '&_pgn=2',
]
print(url_new)
all_list = []
for i in url_list[0]:
    driver.get(i)
    driver.add_cookie(driver.get_cookies()[0])
    driver.get(i)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    html = driver.execute_script('return document.documentElement.outerHTML')
    # print(html)
    r = 'class="s-item__link" href="(.*?)">'
    ret = re.findall(r, html)
    all_list = all_list + ret
# num = 0
for i in all_list:
    #     # res = requests.get(i,headers=headers)
    #     # print(res)
    #     # if res == '<Response [404]>':
    #     #     num = num+1
    print(i)
