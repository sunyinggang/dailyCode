import json
import math
from lxml import etree
import requests
from selenium import webdriver

browser = webdriver.Chrome()
url = "https://vendor.wanda.cn/AnnouncementList.aspx"
searchData = {"Title":"清洁","CategoryID":"*","rowIndex":"1","PageSize":"15","__1osInfo":"Windows"}
browser.post(url,searchData)
# 搜索


headers = {"content-type": "application/json;charset=utf-8"}
r = requests.post(url, data=json.dumps(searchData), headers=headers)
l =1
k =2