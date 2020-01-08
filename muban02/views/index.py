#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import config
import os

class httpHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url('fanxiangjiexi')
        self.write('fanxiaoye❤wangkaiyue<a href="%s">去另一个界面</a>' % (url))


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


class XuanRanHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        temp = 100
        dic = {
            'name': 'fanfan',
            'age': '24'
        }
        flag = 1

        list1 = [0,1,2,3,4,5]
        self.render('home.html', num=temp, dic=dic, flag=flag, list1=list1)


class ChuanHanshu(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        def fan(n1, n2):
            return n1 + n2
        self.render('chuanhanshu.html', f=fan)


class ZhuanYiHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        str = '<h1>fanxiaoye</h1>'
        self.render('jicheng.html', str=str)


class JiChenHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('jicheng.html', title='jicheng')
