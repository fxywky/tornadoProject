#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
from views import index
import config


class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            (r'/', index.httpHandler),
            (r'/chuanCan', index.canShuHandler, {'word1': 'fanxiaoye', 'word2': 'wangkaiyue'}),

            # 反向解析需要name，在页面中的链接中利用reverse_url对name进行解析
            tornado.web.url(r'/FXJX', index.fanxiangHandler, {'word3': 'fanfan', 'word4': 'xiaoyueyue'}, name='fanxiangjiexi'),

            # 正则匹配uri
            (r'/wangkaiyue/(\w+)/(\w+)/(\w+)', index.wangkaiyueHandler),

            # get请求方式
            (r'/getFangShi', index.GetFangShiHandler),

            # post请求方式
            (r'/postFangShi', index.PostFangshiHandler),

            # request对象
            ('/requestObject', index.RequestObject),

            # upfile
            (r'/upfile', index.UpFile),

            # json
            (r'/json1', index.JsonData),

            # 重定向
            (r'/redirect', index.RedirectHandler),

            # 错误处理
            (r'/error', index.ErrorHandler),

            # 执行顺序查看
            (r'/sequence', index.sequenceHandler),
        ]
        super(Application, self).__init__(handler, **config.settings)
