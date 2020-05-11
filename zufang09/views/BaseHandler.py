#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import os
import config
import time
import tornado.gen
import tornado.websocket

from tornado.httpclient import AsyncHTTPClient
import json
from utils.session import *

# 打开主页就添加xsrf的cookie
class SFHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(SFHandler, self).__init__(*args, **kwargs)
        self.xsrf_token

class BaseHandler(tornado.web.RequestHandler):
    """handler基类"""

    # 定义一个成员方法按照属性对待
    @property
    def db(self):
        return self.application.db
    @property
    def redis(self):
        return self.application.redis

    def prepare(self):
        self.xsrf_token
        if self.request.headers.get('Content-Type', '').startswith('application/json'):
            self.json_args = json.loads(self.request.body)   # 字典
        else:
            self.json_args = None

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    def initialize(self):
        pass

    def on_finish(self):
        pass

    def get_current_user(self):   # 谁调用get_current_user，谁就把自己传进去
        self.session = Session(self)
        return self.session.data
