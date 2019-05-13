# encoding:utf-8
import configparser
import os


# 读取配置文件
def get_config(section, key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/../conf/config.conf'
    config.read(path)
    return config.get(section, key)
