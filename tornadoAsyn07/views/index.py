#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import os
import config
import time
import tornado.gen

from tornado.httpclient import AsyncHTTPClient
import json

# 打开主页就添加xsrf的cookie
class SFHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(SFHandler, self).__init__(*args, **kwargs)
        self.xsrf_token


class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('home')

# 回调函数异步
class StudentHandler(tornado.web.RequestHandler):
    def on_response(self, response):
        if response.error:
            self.send_error(500)
        else:
            # 转成字符串
            data = json.loads(response.body)
            self.write(data)
        self.finish()  # 手动关闭通信的通道

    @tornado.web.asynchronous   # 不关闭通信的通道
    def get(self, *args, **kwargs):
        url = 'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'
        # 创建一个客户端
        client = AsyncHTTPClient()
        client.fetch(url, callback=self.on_response)


# 协程异步
class StudentHandler1(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = 'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            self.write(json.loads(res.body))


# 将获取数据的方法抽离出来
class StudentHandler2(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        ret = yield self.getData()
        self.write(ret)

    @tornado.gen.coroutine
    def getData(self):
        url = 'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            ret = {'ret': 0}
        else:
            ret = json.loads(res.body)
        raise tornado.gen.Return(ret)

# 协程并行
class BingXingHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = [
            'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00',
            'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00',
            'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00',
            'http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00'
        ]

        resA, resB = yield [self.getData(url[0]), self.getData(url[1])]
        dicCD = yield dict(resC=self.getData(url[2]), resD=self.getData(url[3]))

        self.selfWrite(resA, url[0])
        self.selfWrite(resB, url[1])
        self.selfWrite(dicCD['resC'], url[2])
        self.selfWrite(dicCD.get('resD', ''), url[3])

    @tornado.gen.coroutine
    def getData(self, url):
        client = tornado.httpclient.AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            ret = {'ret': 0}
        else:
            ret = json.loads(res.body)
            print(ret)
        raise tornado.gen.Return(ret)

    def selfWrite(self, res, url):
        self.write(url)
        self.write('<:br/>')
        self.write(res)
        self.write('<br/>')
        self.write('<br/>')


