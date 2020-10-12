import requests
from lxml import etree

# 远大中国
url = "http://www.yuandacn.com/index.php/zh/projectcn/cn.html"
r = requests.get(url)
htmlContent = r.text
tree = etree.HTML(htmlContent)
# 所以需要前转为字符串查看当前补齐后的html结构
result = etree.tostring(tree).decode("utf-8")
lists = tree.xpath("/html/body/div[2]/div[4]/div/div[1]/div[2]/div[1]/div")
hotels = []
hotel = {}

for list in lists:
    hotel['title'] = str(list.xpath("div/div[2]/div[1]/span/a/text()")[0])
    hotel['href'] = str(list.xpath("div/div[2]/div[1]/span/a/@href")[0])
    hotel['tag_list'] = str(list.xpath("div/div[2]/div[1]/a[1]/text()")[0])
    hotel['address'] = str(list.xpath("div/div[2]/div[2]/div[1]/p[1]/a/text()")[0])
    hotels.append(hotel)
