import json
import math
from lxml import etree
import requests

# 搜索
url = "http://bp.cfldcn.com/index!index.do"
searchData = {"categoryCode": "zbgg","webArticleName": "保洁服务","signUpType": "","signUpEnd": "","isSignUpEnd":"" ,"input": "搜索","start": "0","limit": "500"}
headers = {"content-type": "application/json;charset=utf-8"}
r = requests.post(url, data=json.dumps(searchData), headers=headers)
l =1
k =2