import math
import re
import time
from datetime import datetime

import requests
from lxml import etree

# 居里新房：近期开盘和未来半年开盘的数据
# url = "https://sh.julive.com/project/s/n1_n4"
# r = requests.get(url)
# htmlContent = r.text
# tree = etree.HTML(htmlContent)
# # 所以需要前转为字符串查看当前补齐后的html结构
# result = etree.tostring(tree).decode("utf-8")
# 获取列表href
from mysql import tmpUrlsJL, session, future_room, connection

# url_list = ["https://cd.julive.com/project/s/n1_n4", "https://gz.julive.com/project/s/n1_n4"
#     , "https://sz.julive.com/project/s/n1_n4", "https://xa.julive.com/project/s/n1_n4",
#             "https://cq.julive.com/project/s/n1_n4"
#     , "https://hz.julive.com/project/s/n1_n4", "https://nj.julive.com/project/s/n1_n4",
#             "https://qd.julive.com/project/s/n1_n4"
#     , "https://sy.julive.com/project/s/n1_n4", "https://tj.julive.com/project/s/n1_n4",
#             "https://wh.julive.com/project/s/n1_n4","https://nb.julive.com/project/s/n1_n4","https://jx.julive.com/project/s/n1_n4"]

def add_href():
    url_list = ["https://hf.julive.com/project/s/n1_n4","https://jn.julive.com/project/s/n1_n4"
                ,"https://zz.julive.com/project/s/n1_n4","https://cs.julive.com/project/s/n1_n4","https://gy.julive.com/project/s/n1_n4"
                ,"https://km.julive.com/project/s/n1_n4"]
    for o_url in url_list:
        r = requests.get(o_url)
        htmlContent = r.text
        tree = etree.HTML(htmlContent)
        count = int(tree.xpath("/html/body/div[1]/div[4]/div[4]/div[1]/div[1]/p/em")[0].text)
        page = math.ceil(count / 15)
        page_list(page, o_url)



# 获取每一页列表
def page_list(page,o_url):

    for i in range(1,page+1):
        p_url = o_url + "-z" + str(i)
        print("开始爬取第"+str(i)+"页")
        time.sleep(3)
        r = requests.get(p_url)
        htmlContent = r.text
        tree = etree.HTML(htmlContent)
        lists = tree.xpath("/html/body/div[1]/div[4]/div[4]/div[2]/div/div")
        for list in lists:
            s = list.xpath("div/div[2]/div[1]/span/a/@href")
            href = str(list.xpath("div/div[2]/div[1]/span/a/@href")[0])
            urls = tmpUrlsJL(url=href)
            session.add(urls)
            session.commit()
            session.close()
        print("结束爬取第" + str(i) + "页")
        print("休息5秒")
        time.sleep(5)

def begin_detail():
    urls = session.query(tmpUrlsJL).all()
    session.close()
    info_list = []
    i = 1
    for url in urls:
        if i >116:
            r = requests.get(url.url)
            time.sleep(5)
            htmlContent = r.text
            tree = etree.HTML(htmlContent)
            print("开始爬取第" + str(i) + "条")
            time_start = time.time()
            name = tree.xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div[2]/h1")[0].text
            tags = tree.xpath("/html/body/div[1]/div[3]/div[2]/div/div[1]/div[2]/p[1]/span[1]")
            address = tree.xpath("/html/body/div[1]/div[3]/div[3]/div[2]/div[1]/ul[2]/li[2]/p/span/a")[0].text
            opening_date = tree.xpath("/html/body/div[1]/div[3]/div[3]/div[2]/div[1]/ul[2]/li[4]/p[1]/span")
            if len(opening_date):
                opening_date = tree.xpath("/html/body/div[1]/div[3]/div[3]/div[2]/div[1]/ul[2]/li[4]/p[1]/span")[0].text.strip()
            else:
                opening_date = ""
            if len(opening_date) != 0:
                if opening_date[4] != "年":
                    if len(opening_date) == 7:
                        opening_date = datetime.strptime(opening_date, '%Y-%m').date()
                    elif len(opening_date) == 10:
                        if is_valid_date(opening_date) == True:
                            opening_date = datetime.strptime(opening_date, '%Y-%m-%d').date()
                        else:
                            opening_date = None
                else:
                    opening_date = None
            else:
                opening_date = None
            tag_list = []
            for tag in tags:
                tag_list.append(tag.text)
            strtag = ",".join(tag_list)
            print("爬取完成第" + str(i) + "条")
            s_info = {}
            s_info["name"] = name
            s_info["tags"] = strtag
            s_info["address"] = address
            s_info["opening_date"] = opening_date
            s_info["city"] = city_name(url.url)
            s_info["url"] = url.url
            info_list.append(s_info)
            print("开始第" + str(i) + "次存储")
            ins = future_room.insert()
            result = connection.execute(ins, info_list)
            time_end = time.time()
            print("完成第" + str(i) + "次存储")
            print('用时：', time_end - time_start)
            info_list = []
            if i % 30 == 0:
                print("休息一下")
                time.sleep(5)
        i = i + 1
#city_list = {"ju":"北京","cd":"成都","gz":"广州","sz":"深圳","xa":"西安","cq":"重庆","hz":"杭州","nj":"南京",
# "qd":"青岛","sy":"沈阳","tj":"天津","wh":"武汉""nb": "宁波", "sx": "绍兴", "jx": "嘉兴", "wz": "温州",
# "huzhou": "湖州", "zhoushan": "舟山", "quzhou": "衢州",
#                  "jh": "金华", "lishui": "丽水", "yw": "义乌"}
def city_name(url):
    city_list = {"sjz":"石家庄","hf":"合肥","jn":"济南","zz":"郑州","cs":"长沙","gy":"贵阳","km":"昆明"}
    l = re.split('[/ .]', url)
    city = l[2]
    return city_list[city]

def is_valid_date(str):
  '''判断是否是一个有效的日期字符串'''
  try:
    datetime.strptime(str, "%Y-%m-%d")
    return True
  except:
    return False
if __name__=='__main__':
    begin_detail()

