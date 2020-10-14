# 地产搭档网站爬虫测试
import json
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from mysql import tmpUrls, session, traditional_office, connection

browser = webdriver.Chrome()

def add_href(i):
    url = "https://www.dichandadang.com/q?city=shanghai&type=traditional_office&page=" + i
    try:
        browser.get(url)
        articles = browser.find_elements_by_xpath(
            "//article[@class='Property col-lg-4 col-md-4 col-sm-4 col-xs-12 unhovered']/div/div/div/a")
        for article in articles:
            url = tmpUrls(url=article.get_attribute('href'))
            session.add(url)
    except TimeoutException:
        add_href(i)

# 先爬取所有url -> 存到一张表
def begin_url():
    url = "https://www.dichandadang.com/q?city=shanghai&type=traditional_office"
    browser.get(url)
    page_num = browser.find_element_by_xpath(
        "//div[@class='hidden-xs pagination-md']/ul/li[@class='pager-last']").text
    for i in range(0, int(page_num)):
        page = str(i)
        print("开始爬取第" + page + "页")
        add_href(page)
        session.commit()
        print("已存储第" + page + "页")
        time.sleep(1)

    browser.close()
    session.close()
    print("结束")



kv = {'大楼名称':'name', '城市':'city', '区域':'area', '地址':'address', '竣工时间':'completion_time',
      '楼层数':'floor_number','层高':'floor_height','业主':'office_owner',
      '物业管理公司':'property_company','客梯数量':'peoelv_number','货梯数量':'freelv_number'}

# 遍历所有url，通过url爬取并存储详情信息
def begin_detail():
    urls = session.query(tmpUrls).all()
    session.close()
    headers = {'Connection': 'close'}
    info_list = []
    i = 1
    for url in urls:
        r = requests.get(url.url, headers=headers)
        tree = etree.HTML(r.text)
        print("开始爬取第" + str(i) + "条")
        time_start = time.time()
        infos = tree.xpath("//*[@id='property-block-info']/article/div[2]/div/div[@class='col-sm-3 col-xs-6 ']")
        print("爬取完成第" + str(i) + "条")
        s_info = {}
        for info in infos:
            result = etree.tostring(info).decode("utf-8")
            key = info.xpath("h5/strong")[0].text
            value = str(info.xpath("normalize-space(p)"))
            col = kv.get(key)
            if col != None:
                s_info[col] = value
        info_list.append(s_info)
        print("开始第" + str(i) + "次存储")
        ins = traditional_office.insert()
        result = connection.execute(ins, info_list)
        time_end = time.time()
        print("完成第" + str(i) + "次存储")
        print('用时：', time_end - time_start)
        info_list = []
        i = i + 1
        if i % 30 == 0:
            print("休息一下")
            time.sleep(3)



