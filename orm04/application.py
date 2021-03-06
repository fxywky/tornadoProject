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

            (r'/stus', index.StusHandler),





            # 静态文件
            (r'/(.*)$', tornado.web.StaticFileHandler, {'path': os.path.join(config.settings['static_path'], 'html'),
                                                        'default_filename': 'index.html'})
        ]
        super(Application, self).__init__(handler, **config.settings)
