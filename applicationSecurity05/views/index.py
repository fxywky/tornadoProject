#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import os
import config


class httpHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render(os.path.join(config.settings['static_path'], 'html/index.html'))

class PutongCookie(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('fanxiaoye', '960000')
        self.write('cookie')

class GetPutongCookie(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        cookie = self.get_cookie('fanxiaoye', '未登录')
        print(cookie)
        self.write('ok')

class ClearCookie(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.clear_cookie('fanxiaoye')
        self.clear_all_cookies()
        self.write('ok')


class SaveCookie(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_secure_cookie('fan', 'haha')
        self.write('ok')

class GetSaveCookie(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        saveCookie = self.get_secure_cookie('fan')
        print(saveCookie)
        self.write(saveCookie)


# xsrf
class CookieNum(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        count = self.get_cookie('count', None)
        if count == None:
            count = 1
        self.render('fangwenNum.html', count=count)

class PostCookie(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postfile.html')

    def post(self, *args, **kwargs):
        count = self.get_cookie('count', None)
        if not count:
            count = 1
        else:
            count = int(count) + 1
        self.set_cookie('count', str(count))
        self.redirect('/cookienum')


# 打开主页就添加xsrf的cookie
class SFHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(SFHandler, self).__init__(*args, **kwargs)
        self.xsrf_token


# 用户登录验证
class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        next0 = self.get_query_argument('next', '/')
        url = 'login?next=' + next0
        self.render('login.html', url=url)

    def post(self, *args, **kwargs):
        userName = self.get_argument('username')
        passwd = self.get_argument('passwd')

        if userName == '1' and passwd == '1':
            # self.get_argument()
            next0 = self.get_query_argument('next', '/')
            print(next0)
            self.redirect(next0+'?flag=logined')
        else:
            next0 = self.get_query_argument('next', '/')
            print(next0)
            self.redirect('/login?next=' + next0)

class HomeHandler(tornado.web.RequestHandler):
    # 验证用户的方法应该写在该方法中，验证成功返回True
    # 验证失败则重定向至配置中login_url所制定的路由
    def get_current_user(self):
        # /home
        flag = self.get_argument('flag', None)
        return flag

    # get_current_user验证成功就走装饰器的方法
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('home.html')


class CartHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        # /home
        flag = self.get_argument('flag', None)
        return flag

    # get_current_user验证成功就走装饰器的方法
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('home.html')
