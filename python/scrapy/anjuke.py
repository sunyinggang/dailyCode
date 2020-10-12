import requests
from lxml import etree

# 未来半年开盘的楼盘  -> 有反派，访问呢几次就ip被锁，需要代理ip池
url = "https://lf.fang.anjuke.com/loupan/all/o4/"
r = requests.get(url)
htmlContent = r.text
tree = etree.HTML(htmlContent)
# 所以需要前转为字符串查看当前补齐后的html结构
result = etree.tostring(tree).decode("utf-8")
lists = tree.xpath("/html/body/div[2]/div[2]/div[1]/div[4]/div")
hotels = []
hotel = {}

for list in lists:
    l = list.xpath("div[1]/a[1]")
    print(l)