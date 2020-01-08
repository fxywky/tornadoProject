#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config

# tornado.options.options.define('port', default=8000, type=int)
# tornado.options.options.define('list', default=None, type=str, multiple=True)


class httpHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('fanxiaoye❤wangkaiyue')


if __name__ == '__main__':
    # tornado.options.parse_command_line()
    # tornado.options.parse_config_file('config')
    # print(tornado.options.options.list)
    # print(tornado.options.options.port)

    app = tornado.web.Application([
        (r'/', httpHandler)
    ])

    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options['port'])
    httpServer.start(1)

    tornado.ioloop.IOLoop.current().start()







