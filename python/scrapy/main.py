import json
import math
import time
from datetime import datetime

from lxml import etree
import requests

from mysql import connection, future_room, tmp_uniscid, session, bidding_ggzy


# 搜索相关项目：uniscid，keyword=保洁服务/清洁服务
def serch_url():
    url = "http://data.ggzy.gov.cn/yjcx/index/search"
    searchData = {}
    searchData["keyword"] = "保洁服务"
    searchData["page"] = 1
    headers = {"content-type": "application/json;charset=utf-8"}
    r = requests.post(url, data=json.dumps(searchData), headers=headers)
    content = json.loads(r.content)
    total = content['total']
    page = math.ceil(int(total) / 10)
    for i in range(1,page+1):
        print("开始爬取第"+str(i)+"页")
        searchData["page"] = i
        r = requests.post(url, data=json.dumps(searchData), headers=headers)
        content = json.loads(r.content)
        data_list = content["data"]
        info_list = []
        for data in data_list:
            s_info = {}
            s_info['uniscid'] = data['uniscid']
            s_info['entname'] = data['entname']
            info_list.append(s_info)
        ins = tmp_uniscid.insert()
        result = connection.execute(ins, info_list)
        print("爬取完成第" + str(i) + "页")

# 成交项目
def delite_list():
    uniscid_list = session.query(tmp_uniscid).all()
    session.close()
    headers = {"content-type": "application/json;charset=utf-8"}
    i=1
    for u in uniscid_list:
        print("开始爬取第"+str(i)+"条")
        bind_list_url = "http://data.ggzy.gov.cn/yjcx/index/bid_list"
        listData = {"uniscid": u.uniscid, "page": 1, "tos": ""}
        r3 = requests.post(bind_list_url, data=json.dumps(listData), headers=headers)
        content3 = json.loads(r3.content)
        data_list = content3["data"]
        info_list = []
        for data in data_list:
            s_info = {}
            s_info['bidding_people'] = data['tender_org_name']
            s_info['name'] = data['project_name']
            s_info['field'] = data['tos']
            s_info['begin_date'] = datetime.strptime(data['create_time'], '%Y-%m-%d').date()
            s_info['money'] = float(data['bid_price'])
            s_info['company'] = u.entname
            info_list.append(s_info)
        ins = bidding_ggzy.insert()
        result = connection.execute(ins, info_list)
        print("结束爬取第" + str(i) + "条")
        if i % 20 == 0:
            time.sleep(3)
            print("休息一下")
        i=i+1



# 暂时无用
def xiangqing():
    # 项目详情
    bind_show_url = "http://data.ggzy.gov.cn/yjcx/index/bid_show"
    showData = {"id": "00370a5367899e4b4a9ea3c67196ca9572b2"}
    r4 = requests.post(bind_show_url, data=json.dumps(showData), headers=headers)
    content4 = json.loads(r4.content)
    # 注意这里返回的html不完整，只是部分标签
    htmlContent = content4['data']['content']
    # etree.HTML将字符串转为html对象时自动补齐缺失的标签，但是和原网页标签可能不同
    tree = etree.HTML(htmlContent)
    # 所以需要前转为字符串查看当前补齐后的html结构
    result = etree.tostring(tree)
    print(result.decode("utf-8"))

    table = tree.xpath('/html/body/table')
    td0 = tree.xpath('/html/body/table/tr//td[1]/b')
    td1 = tree.xpath('/html/body/table/tr//td[2]')



if __name__=='__main__':
    delite_list()


