#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import tornado.web
import tornado.ioloop
import tornado.httpserver
from application import Application
import config

if __name__ == '__main__':
    app = Application()

    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options['port'])
    httpServer.start(1)

    tornado.ioloop.IOLoop.current().start()



