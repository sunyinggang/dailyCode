# 地产搭档网站爬虫测试
import json
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# def add_href(i):
#     url = "https://www.dichandadang.com/q?city=shanghai&type=traditional_office&page=" + i
#     try:
#         browser.get(url)
#         articles = browser.find_elements_by_xpath(
#             "//article[@class='Property col-lg-4 col-md-4 col-sm-4 col-xs-12 unhovered']/div/div/div/a")
#         for article in articles:
#             href.append(article.get_attribute('href'))
#     except TimeoutException:
#         add_href(i)

# href = []
# url = "https://www.dichandadang.com/q?city=shanghai&type=traditional_office"
# browser = webdriver.Chrome()
# browser.get(url)
# page_num = browser.find_element_by_xpath(
#         "//div[@class='hidden-xs pagination-md']/ul/li[@class='pager-last']").text
# for i in range(0,int(page_num)):
#     print(i)
#     add_href(str(i))
# browser.close()
# print(href)

href = ['https://www.dichandadang.com/office-leasing/shanghai/pudong/shanghai-tower', 'https://www.dichandadang.com/office-leasing/shanghai/pudong/jin-mao-tower']

for url in href:
    r = requests.get(url)
    tree = etree.HTML(r.text)
    infos = tree.xpath("//*[@id='property-block-info']/article/div[2]/div/div[@class='col-sm-3 col-xs-6 ']")
    for info in infos:
        key = info.xpath("h5/strong")[0].text
        value = str(info.xpath("normalize-space(p)"))
        print(key)
        print(value)


