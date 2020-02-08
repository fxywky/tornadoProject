#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import os
from views import index
import config

class Application(tornado.web.Application):
    def __init__(self):
        handler = [

            (r'/home', index.HomeHandler),
            # 回调函数实现异步
            (r'/student', index.StudentHandler),
            # 协程实现异步
            (r'/stuedent1', index.StudentHandler1),
            (r'/student2', index.StudentHandler2),
            # 协程并行
            (r'/bingxing', index.BingXingHandler),

            (r'/(.*)$', index.SFHandler, {'path': os.path.join(config.settings['static_path'], 'html'),
                                                       'default_filename': 'index.html'}),

                   ]
        super(Application, self).__init__(handler, **config.settings)
