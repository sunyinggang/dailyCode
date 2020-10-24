import math
import re
import time
from datetime import datetime

import requests
from lxml import etree


# 先爬取所有url -> 存到一张表
from mysql import tmpUrls, session, future_room, connection


# 获取每一页列表
def page_list(page,o_url):

    for i in range(1,page+1):
        p_url = o_url + "/loupan/nho0pg" + str(i)
        print("开始爬取第"+str(i)+"页")
        time.sleep(5)
        r = requests.get(p_url)
        htmlContent = r.text
        tree = etree.HTML(htmlContent)
        lists = tree.xpath("/html/body/div[6]/ul[2]//li/div")
        for list in lists:
            href = str(list.xpath("div[1]/a/@href")[0])
            url = o_url + href
            urls = tmpUrls(url=url)
            session.add(urls)
            session.commit()
            session.close()
        print("结束爬取第" + str(i) + "页")
        print("休息5秒")
        time.sleep(5)

# url_list = ["https://hz.fang.ke.com","https://nj.fang.ke.com","https://qd.fang.ke.com","https://sy.fang.ke.com"
#                 ,"https://tj.fang.ke.com","https://wh.fang.ke.com","https://nb.fang.ke.com","https://sx.fang.ke.com","https://jx.fang.ke.com","https://wz.fang.ke.com"
#                 ,"https://huzhou.fang.ke.com","https://zhoushan.fang.ke.com","https://quzhou.fang.ke.com","https://jh.fang.ke.com"
#                 ,"https://lishui.fang.ke.com","https://yw.fang.ke.com"]

# 获取列表href
def add_href():
    url_list = ["https://sjz.fang.ke.com","https://ty.fang.ke.com","https://hhht.fang.ke.com","https://cc.fang.ke.com"
                ,"https://hrb.fang.ke.com","https://hf.fang.ke.com","https://fz.fang.ke.com","https://nc.fang.ke.com"
                ,"https://jn.fang.ke.com","https://zz.fang.ke.com","https://cs.fang.ke.com","https://nn.fang.ke.com"
                ,"https://hk.fang.ke.com","https://gy.fang.ke.com","https://km.fang.ke.com","https://lasa.fang.ke.com"
                ,"https://lz.fang.ke.com","https://xining.fang.ke.com","https://yinchuan.fang.ke.com","https://wlmq.fang.ke.com"]
    for o_url in url_list:
        print("开始城市"+o_url)
        p_url = o_url + "/loupan/nho0/"
        r = requests.get(p_url)
        htmlContent = r.text
        tree = etree.HTML(htmlContent)
        count = int(tree.xpath("/html/body/div[6]/div[2]/span[2]")[0].text)
        page = math.ceil(count / 10)
        page_list(page, o_url)
        print("结束城市" + o_url)


#
def begin_detail():
    urls = session.query(tmpUrls).all()
    session.close()
    info_list = []
    i = 1
    for url in urls:
        if i >77:
            r = requests.get(url.url)
            time.sleep(8)
            htmlContent = r.text
            tree = etree.HTML(htmlContent)
            print("开始爬取第" + str(i) + "条")
            time_start = time.time()
            s = tree.xpath("/html/body/div[2]/div[2]/div[1]/div[1]/h2")
            name = tree.xpath("/html/body/div[2]/div[2]/div[1]/div[1]/h2")[0].text
            tags = tree.xpath("/html/body/div[2]/div[2]/div[1]/div[1]/div//span")
            address = tree.xpath("/html/body/div[2]/div[3]/div[2]/div/div[3]/ul/li[1]/span[2]")[0].text
            opening_date = tree.xpath("/html/body/div[2]/div[3]/div[2]/div/div[3]/ul/li[2]/div/span[2]")
            if len(opening_date):
                opening_date = tree.xpath("/html/body/div[2]/div[3]/div[2]/div/div[3]/ul/li[2]/div/span[2]")[0].text
            else:
                opening_date = ""

            if len(opening_date) == 7:
                opening_date = datetime.strptime(opening_date, '%Y.%m').date()
            elif len(opening_date) == 0:
                opening_date = None
            else:
                opening_date = datetime.strptime(opening_date, '%Y.%m.%d').date()
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
            if i % 10 == 0:
                print("休息一下")
                time.sleep(5)
        i = i + 1

#city_list = {"sh":"上海","bj":"北京","cd":"成都","gz":"广州","sz":"深圳","xa":"西安","cq":"重庆","hz":"杭州",
# "nj":"南京","qd":"青岛","sy":"沈阳","tj":"天津","wh":"武汉",
# "nb":"宁波","sx":"绍兴","jx":"嘉兴","wz":"温州","huzhou":"湖州","zhoushan":"舟山",
#"quzhou":"衢州","jh":"金华","lishui":"丽水","yw":"义乌","sjz":"石家庄","ty":"太原","hhht":"呼和浩特",
# "cc":"长春","hrb":"哈尔滨","hf":"合肥",
# "fz":"福州","nc":"南昌","jn":"济南","zz":"郑州","cs":"长沙","nn":"南宁","hk":"海口"
#,"gy":"贵阳","km":"昆明","lasa":"拉萨","lz":"兰州","xining":"西宁","yinchuan":"银川","wlmq":"乌鲁木齐"}

def city_name(url):
    city_list = {"sjz":"石家庄","ty":"太原","hhht":"呼和浩特","cc":"长春","hrb":"哈尔滨","hf":"合肥",
                 "fz":"福州","nc":"南昌","jn":"济南","zz":"郑州","cs":"长沙","nn":"南宁","hk":"海口"
                 ,"gy":"贵阳","km":"昆明","lasa":"拉萨","lz":"兰州","xining":"西宁","yinchuan":"银川","wlmq":"乌鲁木齐"}
    l = re.split('[/ .]', url)
    city = l[2]
    return city_list[city]


def test():
    # 免费代理ip：http://ip.yqie.com/proxygaoni/
    proxies = {
        "http": "http://123.133.36.26:36017"  # 代理ip
    }
    o_url = "https://cd.fang.ke.com"
    p_url = o_url + "/loupan/nho0/"
    r = requests.get(url=p_url,proxies=proxies)
    htmlContent = r.text
    tree = etree.HTML(htmlContent)
    count = int(tree.xpath("/html/body/div[6]/div[2]/span[2]")[0].text)
    page = math.ceil(count/10)
    print(page)

def test2():
    r = requests.get("https://cd.fang.ke.com/loupan/p_jzyjzyblgjr/")
    htmlContent = r.text
    tree = etree.HTML(htmlContent)
    time_start = time.time()
    name = tree.xpath("/html/body/div[2]/div[2]/div[1]/div[1]/h2")[0].text
    tags = tree.xpath("/html/body/div[2]/div[2]/div[1]/div[1]/div//span")
    address = tree.xpath("/html/body/div[2]/div[3]/div[2]/div/div[3]/ul/li[1]/span[2]")[0].text
    opening_date = tree.xpath("/html/body/div[2]/div[3]/div[2]/div/div[3]/ul/li[2]/div/span[2]")
    if len(opening_date):
        opening_date = tree.xpath("/html/body/div[2]/div[3]/div[2]/div/div[3]/ul/li[2]/div/span[2]")[0].text
    else:
        opening_date = tree.xpath("/html/body/div[2]/div[3]/div[2]/div/div[3]/ul/li[2]/span[2]")[0].text
    k=1
    l=2



if __name__=='__main__':
    add_href()

