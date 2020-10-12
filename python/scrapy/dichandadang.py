# 地产搭档网站爬虫测试
import json
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from mysql import tmpUrls, session, traditional_office, connection

# def add_href(i):
#     url = "https://www.dichandadang.com/q?city=shanghai&type=traditional_office&page=" + i
#     try:
#         browser.get(url)
#         articles = browser.find_elements_by_xpath(
#             "//article[@class='Property col-lg-4 col-md-4 col-sm-4 col-xs-12 unhovered']/div/div/div/a")
#         for article in articles:
#             url = tmpUrls(url=article.get_attribute('href'))
#             session.add(url)
#     except TimeoutException:
#         add_href(i)
#
# href = []
# url = "https://www.dichandadang.com/q?city=shanghai&type=traditional_office"
# browser = webdriver.Chrome()
# browser.get(url)
# page_num = browser.find_element_by_xpath(
#         "//div[@class='hidden-xs pagination-md']/ul/li[@class='pager-last']").text
# for i in range(0,int(page_num)):
#     page = str(i)
#     print("开始爬取第" + page +"页")
#     add_href(page)
#     session.commit()
#     print("已存储第" + page +"页")
#     time.sleep(1)
#
#
# browser.close()
# session.close()
# print("结束")

kv = {'大楼名称':'name', '城市':'city', '区域':'area', '地址':'address', '竣工时间':'completion_time',
      '楼层数':'floor_number','层高':'floor_height','业主':'owner',
      '物业管理公司':'property_company','客梯数量':'peoelv_number','货梯数量':'freelv_number'}

href = ['https://www.dichandadang.com/office-leasing/shanghai/pudong/shanghai-tower', 'https://www.dichandadang.com/office-leasing/shanghai/pudong/jin-mao-tower','https://www.dichandadang.com/office-leasing/shanghai/pudong/shanghai-sk-tower']


info_list = []
for url in href:
    r = requests.get(url)
    tree = etree.HTML(r.text)
    infos = tree.xpath("//*[@id='property-block-info']/article/div[2]/div/div[@class='col-sm-3 col-xs-6 ']")
    s_info = {}
    for info in infos:
        result = etree.tostring(info).decode("utf-8")
        key = info.xpath("h5/strong")[0].text
        value = str(info.xpath("normalize-space(p)"))
        col = kv.get(key)
        if col != None :
            s_info[col] = value
    info_list.append(s_info)

ins = traditional_office.insert()
result=connection.execute(ins,info_list)


