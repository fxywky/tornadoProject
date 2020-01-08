#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import tornado.web
import tornado.ioloop
import tornado.httpserver

class httpHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('wangkaiyue')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', httpHandler)
    ])

    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(8000)
    httpServer.start(2)

    tornado.ioloop.IOLoop.current().start()
