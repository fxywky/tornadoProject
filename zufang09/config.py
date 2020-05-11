#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
BASE_DIRS = os.path.dirname(__file__)


options = {
    'port':9999,
}

session_expires = 86400     # session的有效期　秒
passwdHashKey = 'ihome@$^*'

image_url_prefix = 'http://q67g039lo.bkt.clouddn.com/'

mysql_options = {
    'host': '127.0.0.1',
    'user': 'root',
    'passwd': 'fanxiaoye',
    'dbName': 'ihome'
}

redis_options = {
    'host': '127.0.0.1',
    'port': 6379
}

settings = {
    'static_path': os.path.join(BASE_DIRS, 'static'),
    'template_path': os.path.join(BASE_DIRS, 'templates'),
    'debug': False,
    'cookie_secret': 'SKVCH7tMSiu9E9WaBdYGrue336aJ3UliogP7lrIBRUY=',
    'xsrf_cookies': True,
    'login_url': '/login'
}
