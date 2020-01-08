#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import os
from views import index
import config


class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            # (r'/', index.httpHandler),

            # request对象
            ('/requestObject', index.RequestObject),

            # 渲染，传东西
            (r'/xuanran', index.XuanRanHandler),

            # 传函数
            (r'/chuanhanshu', index.ChuanHanshu),

            # 转义
            ('/zhuanyi', index.ZhuanYiHandler),

            # 继承
            (r'/jicheng', index.JiChenHandler),







            # 静态文件
            (r'/(.*)$', tornado.web.StaticFileHandler, {'path': os.path.join(config.settings['static_path'], 'html'),
                                                        'default_filename': 'index.html'})
        ]
        super(Application, self).__init__(handler, **config.settings)
