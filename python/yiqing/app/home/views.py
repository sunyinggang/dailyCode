import math

from flask import jsonify, request
from . import home
from .. import db
from ..models import traditionalOffice


@home.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ





@home.route("/list", methods=['GET'])
def get_classfication():
    #class_list = request.get_json()
    page = request.args.get('page', 1, type=int)
    total = traditionalOffice.query.count()
    list = traditionalOffice.query.paginate(page=page, per_page=10, error_out=False)
    res = {}
    res['page'] = page
    res['pre_page'] = 10
    res['pages'] = math.ceil(total/10)
    res['total'] = total
    de = []
    for i in list.items:
        de.append(i.to_json())
    res['data'] = de
    return jsonify(res)