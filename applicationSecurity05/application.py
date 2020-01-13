#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import os
from views import index
import config

class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            # (r'/$', index.httpHandler),

            # 普通cookie
            (r'/pcookie', index.PutongCookie),
            # 获取普通cookie
            (r'/getpcookie', index.GetPutongCookie),
            # 清除cookie,只是值设置为空，清除操作由浏览器完成
            (r'/clearcookie', index.ClearCookie),

            # 安全cookie
            (r'/savecookie', index.SaveCookie),
            # 获取安全cookie
            (r'/getsavecookie', index.GetSaveCookie),

            # xrsf
            (r'/cookienum', index.CookieNum),
            (r'/postCookie', index.PostCookie),

            # 用户登录验证
            (r'/login', index.LoginHandler),
            (r'/home', index.HomeHandler),
            (r'/cart', index.CartHandler),

            (r'/(.*)$', index.SFHandler, {'path': os.path.join(config.settings['static_path'], 'html'),
                                                       'default_filename': 'index.html'}),

                   ]
        super(Application, self).__init__(handler, **config.settings)
