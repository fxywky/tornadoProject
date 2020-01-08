#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import tornado.web
import tornado.ioloop
import tornado.httpserver

class httpHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello1 world')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', httpHandler)
    ])

    # 相比于server.py，换了这两行，更加直观的看到创建服务器
    httpServer = tornado.httpserver.HTTPServer(app)

    httpServer.listen(8000)

    tornado.ioloop.IOLoop.current().start()


