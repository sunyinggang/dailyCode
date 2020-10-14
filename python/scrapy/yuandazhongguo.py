import requests
from lxml import etree

# 远大中国
from mysql import tmpUrls, session, sign_building, connection


# 先爬取所有url -> 存到一张表
def add_href():
    p_url = "http://www.yuandacn.com/index.php/zh/projectcn/cn.html"
    r = requests.get(p_url)
    htmlContent = r.text
    tree = etree.HTML(htmlContent)
    lists = tree.xpath("/html/body/div/div[4]/div/div[1]/div[2]/div[1]/div")
    for list in lists:
        href = str(list.xpath("div/div/div[2]/h3/a/@href")[0])
        url = "http://www.yuandacn.com"+href
        urls = tmpUrls(url=url)
        session.add(urls)
        session.commit()
        session.close()

kv = {'工程名称':'name', '工程地址':'address', '建筑高度':'height', '幕墙类型':'wall_type', '幕墙面积':'wall_area'}


# 遍历所有url，通过url爬取并存储详情信息
def begin_detail():
    urls = session.query(tmpUrls).all()
    session.close()
    headers = {'Connection': 'close'}
    # urls = ['http://www.yuandacn.com/index.php/zh/projects-cn/87-domestic/hainan/205-sanya-beauty-crown-hotel.html','http://www.yuandacn.com/index.php/zh/projects-cn/66-domestic/beijing/204-beijing-new-poly-plaza.html']
    info_list = []
    for url in urls:
        r = requests.get(url.url, headers=headers)
        tree = etree.HTML(r.text)
        detail = tree.xpath("/html/body/div[@class='t3-wrapper']/div[4]/div/div[1]/div/article/section//p")
        s_info = {}
        for d in detail:
            l = d.xpath("text()")
            if len(l) != 0:
                if l[0].find("工程名称：") != -1:
                    for i in l:
                        kvi = i.split("：")
                        col = kv.get(kvi[0])
                        if col != None:
                            s_info[col] = kvi[1]
        info_list.append(s_info)
        ins = sign_building.insert()
        result = connection.execute(ins, info_list)
        info_list = []


if __name__=='__main__':
    begin_detail()
