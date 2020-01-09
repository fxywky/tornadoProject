#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
BASE_DIRS = os.path.dirname(__file__)


options = {
    'port':9993,
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
    'debug': False
}
