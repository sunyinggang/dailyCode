from lxml import etree

import requests
# 房天下
url = "https://newhouse.fang.com/house/saledate/202009.html"
r = requests.get(url)
htmlContent = r.text
tree = etree.HTML(htmlContent)
# 所以需要前转为字符串查看当前补齐后的html结构
result = etree.tostring(tree)
lists = tree.xpath('//*[@id="kplist"]/ul//li/div/div[2]')
hotels = []
hotel = {}

for list in lists:
    hotel['title'] = list.xpath('normalize-space(div[1]/div[1]/a[1]/text())')
    hotel['href'] = str(list.xpath('div[1]/div[1]/a[1]/@href')[0])
    hotel['address'] = str(list.xpath('div[3]/div[1]/a[1]/@title')[0])
    hotel['tag'] = list.xpath('div[4]//a/text()')
    hotel['start_time'] = str(list.xpath('div[5]/@title')[0])
    hotels.append(hotel)