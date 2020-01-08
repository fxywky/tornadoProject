#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import tornado.web
import tornado.ioloop

# 业务处理类
class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法，可以响应信息
        self.write('hello world')


if __name__ == '__main__':
    # 实例化一个app对象
    # Application是tornado.web框架的核心应用类，是与服务器对应的接口
    # 里面保存了路由映射表
    # listen方法创建一个http服务器的实例，并绑定了端口
    app = tornado.web.Application([
        (r'/', IndexHandler)
    ])
    # 绑定监听端口
    # 注意：此时的服务器并没有开启监听
    app.listen(8000)
    # IOLoop.current()返回当前线程的IOLoop实例
    # IOLoop.start()启动IOLoop实例的I/O循环
    tornado.ioloop.IOLoop.current().start()

