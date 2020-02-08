#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
BASE_DIRS = os.path.dirname(__file__)


options = {
    'port':9999,
}

mysql = {
    'host': '127.0.0.1',
    'user': 'root',
    'passwd': 'fanxiaoye',
    'dbName': 'torbase'
}


settings = {
    'static_path': os.path.join(BASE_DIRS, 'static'),
    'template_path': os.path.join(BASE_DIRS, 'templates'),
    'debug': False,
    'cookie_secret': 'SKVCH7tMSiu9E9WaBdYGrue336aJ3UliogP7lrIBRUY=',
    'xsrf_cookies': True,
    'login_url': '/login'
}
