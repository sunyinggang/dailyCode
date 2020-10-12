import requests
from lxml import etree

url = "https://lf.fang.ke.com/loupan/nho0/"
r = requests.get(url)
htmlContent = r.text
tree = etree.HTML(htmlContent)
# 所以需要前转为字符串查看当前补齐后的html结构
result = etree.tostring(tree).decode("utf-8")
lists = tree.xpath("/html/body/div[6]/ul[2]//li/div")
print(result)
hotels = []
hotel = {}
for list in lists:
    hotel['title'] = list.xpath("div[1]/a/text()")
    hotel['href'] = str(list.xpath("div[1]/a/@href")[0])
    tag_lists = list.xpath("div[1]/span")
    hotel['tag'] = []
    for tag_list in tag_lists:
        hotel['tag'].append(tag_list.text)
    hotel['address'] = str(list.xpath("a[1]/@title")[0])
    hotels.append(hotel)
