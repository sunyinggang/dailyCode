import json
import math
from lxml import etree
import requests

# 搜索
url = "http://data.ggzy.gov.cn/yjcx/index/search"
searchData = {"keyword": "清洁", "page": "1"}
headers = {"content-type": "application/json;charset=utf-8"}
r = requests.post(url, data=json.dumps(searchData), headers=headers)
content = json.loads(r.content)
total = content['total']
page = math.ceil(int(total)/10)

# 主体详情（get)
uniscid = "91370105351753004F"
detail_url = "http://data.ggzy.gov.cn/yjcx/index/show/uniscid/" + uniscid
r2 = requests.get(detail_url)
content2 = json.loads(r2.content)

# 成交项目
bind_list_url = "http://data.ggzy.gov.cn/yjcx/index/bid_list"
listData = {"uniscid": "91370105351753004F", "page": 1, "tos": ""}
r3 = requests.post(bind_list_url, data=json.dumps(listData), headers=headers)
content3 = json.loads(r3.content)

# 项目详情
bind_show_url = "http://data.ggzy.gov.cn/yjcx/index/bid_show"
showData = {"id": "00370a5367899e4b4a9ea3c67196ca9572b2"}
r4 = requests.post(bind_show_url, data=json.dumps(showData), headers=headers)
content4 = json.loads(r4.content)
# 注意这里返回的html不完整，只是部分标签
htmlContent = content4['data']['content']
# etree.HTML将字符串转为html对象时自动补齐缺失的标签，但是和原网页标签可能不同
tree = etree.HTML(htmlContent)
# 所以需要前转为字符串查看当前补齐后的html结构
result = etree.tostring(tree)
print(result.decode("utf-8"))

table = tree.xpath('/html/body/table')
td0 = tree.xpath('/html/body/table/tr//td[1]/b')
td1 = tree.xpath('/html/body/table/tr//td[2]')
print(content)