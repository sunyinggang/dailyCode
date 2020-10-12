import requests
from lxml import etree

# 居里新房：近期开盘和未来半年开盘的数据
url = "https://sh.julive.com/project/s/n1_n4"
r = requests.get(url)
htmlContent = r.text
tree = etree.HTML(htmlContent)
# 所以需要前转为字符串查看当前补齐后的html结构
result = etree.tostring(tree).decode("utf-8")
lists = tree.xpath("/html/body/div[1]/div[4]/div[4]/div[2]/div/div")
hotels = []
hotel = {}

for list in lists:
    hotel['title'] = str(list.xpath("div/div[2]/div[1]/span/a/text()")[0])
    hotel['href'] = str(list.xpath("div/div[2]/div[1]/span/a/@href")[0])
    hotel['tag_list'] = str(list.xpath("div/div[2]/div[1]/a[1]/text()")[0])
    hotel['address'] = str(list.xpath("div/div[2]/div[2]/div[1]/p[1]/a/text()")[0])
    hotels.append(hotel)
