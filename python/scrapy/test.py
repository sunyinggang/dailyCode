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
import time

l = [35,50,66,100]
time_start = time.time()


for i in l:
    print(int(i/50))
time_end = time.time()
print('用时：', time_end - time_start)