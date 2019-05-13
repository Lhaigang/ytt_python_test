# -*- coding: UTF-8 -*-
from app import config
import requests
import json


host = config.get_config('account', 'Host')
account = config.get_config('account', 'account')
password = config.get_config('account', 'password')


# 获取session_id
def get_session():
    url = host + "/index.php?m=api&f=getSessionID&t=json"
    r = requests.get(url, verify=False)
    h_json = json.loads(r.text)
    data = json.loads(h_json['data'])
    # 全局变量
    global session_id
    session_id = data['sessionID']


# 登录
def login():
    get_session()
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    values = {
        'account': account,
        'password': password,
    }
    url = host + "/index.php?m=user&f=login&t=json&zentaosid=" + session_id
    requests.post(url, data=values, headers=headers)


# 获取产品id
def get_product_id(product_name):
    url = host + "/index.php?m=product&f=index&locate=no&t=json&zentaosid=" + session_id
    r = requests.get(url, verify=False)
    h_json = json.loads(r.text)
    data = json.loads(h_json['data'])
    products = data['products']

    for item in products:
        if products[item] == product_name:
            return item


# 获取产品编号
def get_project_id(product_id, project_name):
    url = host + "/index.php?m=product&f=ajaxGetProjects&t=json&productID="+product_id+"&branch=0&zentaosid=" + session_id
    r = requests.get(url, verify=False)
    h_json = json.loads(r.text)

    for item in h_json:
        if h_json[item] == project_name:
            return item


# 获取模块编号
def get_module_id(product_id, module_name):
    url = host + "/index.php?m=tree&f=ajaxGetOptionMenu&t=json&productID="+product_id+"&viewtype=bug&branch=0&rootModuleID=0&returnType=json" + "&zentaosid=" + session_id
    r = requests.get(url, verify=False)
    h_json = json.loads(r.text)
    for item in h_json:
        if h_json[item] == module_name:
            return item


def post_bug_report(p_data):
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    values = {
        'product': int(p_data['product_id']),
        'project': 0,
        'module': int(p_data['module_id']),
        'assignedTo': p_data['assignedTo'],
        'type': p_data['type'],
        'steps': p_data['steps'],
        'openedBuild[]': p_data['openedBuild'],
        'pri': p_data['pri'],
        'title': p_data['title'],
        'task': p_data['task'],
        'story': p_data['story'],
        'severity': p_data['severity'],
        'os': p_data['os'],
        'browser': p_data['browser'],
        'color': p_data['color'],
        'deadline': p_data['deadline'],
        'mailto[]': p_data['mailto'],
    }
    url = host + "/index.php?m=bug&f=create&productID="+p_data['product_id']+"&branch=0&moduleID=0&zentaosid=" + session_id
    requests.post(url, data=values, headers=headers)


login()


