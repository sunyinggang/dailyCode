# import requests
# from lxml import etree
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
# }
# url = "https://www.jianshu.com/u/3313b20a4e25?order_by=shared_at&page=1"
# r = requests.get(url, headers=headers)
# htmlContent = r.text
# tree = etree.HTML(htmlContent)
# # 所以需要前转为字符串查看当前补齐后的html结构
# lists = tree.xpath('//ul[@class="note-list"]/li')
# for list in lists:
#     print(list)
#     result = etree.tostring(list).decode("utf-8")
#     title = tree.xpath('./div/a/text()')
from datetime import datetime
#
# def is_valid_date(str):
#   '''判断是否是一个有效的日期字符串'''
#   try:
#     datetime.strptime(str, "%Y.%m.%d")
#     return True
#   except:
#     return False

# str = "2020年10月下旬"
# print(str[4] != "年")
# k = datetime.strptime(str, "%Y.%m.%d")
# print(k)
def city_name(url):
    city_list = {"xa":"西安","cq":"重庆","hz":"杭州","nj":"南京","qd":"青岛","sy":"沈阳","tj":"天津","wh":"武汉"}
    city = url[8:10]
    return city_list[city]
s = "https://qd.fang.ke.com/loupan/p_bcbijbd/"
k = city_name(s)
print(k)



