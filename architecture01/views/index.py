#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import config
import os

class httpHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url('fanxiangjiexi')
        self.write('fanxiaoye❤wangkaiyue<a href="%s">去另一个界面</a>' % (url))


class canShuHandler(tornado.web.RequestHandler):
    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        print(self.word1)
        self.write('fan')


class fanxiangHandler(tornado.web.RequestHandler):
    def initialize(self, word3, word4):   # 参数获取的是application里面的
        self.word3 = word3
        self.word4 = word4

    def get(self, *args, **kwargs):
        self.write('反向解析页面%s' % (self.word3))


class wangkaiyueHandler(tornado.web.RequestHandler):
    def get(self, h1, h2, h3, *args, **kwargs):   # 参数获取的是uri里面的
        print(h1 + '--' + h2 + '--' + h3)
        self.write('wangkaiyue')


# get
class GetFangShiHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument('a', default=100)
        b = self.get_query_argument('b', default=100)
        c = self.get_query_argument('c', default=100)
        self.write('%s, %s, %s' % (a, b, c))


# post
class PostFangshiHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postfile.html')

    def post(self, *args, **kwargs):
        username = self.get_body_argument('username')
        passwd = self.get_body_argument('passwd')
        hobbyList = self.get_body_arguments('hobby')
        print(username, passwd, hobbyList)
        self.write('post请求方式')


class RequestObject(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)


class UpFile(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('upfile.html')

    def post(self, *args, **kwargs):
        a = {"a": 'b'}
        filesDict = self.request.files
        for fileList in filesDict.values():
            for item in fileList:
                fileName = item['filename']
                filePath = os.path.join(config.BASE_DIRS, 'upfile/' + fileName)
                with open(filePath, 'wb') as f:
                    f.write(item['body'])


class JsonData(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        jsonData = {
            'name': 'fanxiaoye',
            'age': 18
        }
        self.set_header('name', 'fanxiaoye')
        self.write(jsonData)


class RedirectHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect(r'/upfile')


class ErrorHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        flag = self.get_query_argument('flag')
        if flag == '0':
            self.send_error(404)   # 然后跳转write_error方法
        self.write('服务器 is OK')

    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            # 应该是返回一个错误的界面redirect
            self.write('服务器内部错误')
        elif status_code == 404:
            self.write('资源不存在')

        self.set_status(status_code)

class sequenceHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print('set_default_headers')
    def initialize(self):
        print('initalize')
    def prepare(self):
        print('prepare')
        self.send_error(500)
    def get(self, *args, **kwargs):
        print('HTTP方法')
    def write_error(self, status_code, **kwargs):
        self.write('服务器错误')
        print('write_error')
    def on_finish(self):
        print('on_finish')
