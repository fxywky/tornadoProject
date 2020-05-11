#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
# import torndb
import torndb_for_python3
import redis
import MySQLdb
import os
from views import BaseHandler, Passport, VerifyCode, Profile, House, Order
import config

class Application(tornado.web.Application):
    def __init__(self):
        self.db = torndb_for_python3.Connection(
            host=config.mysql_options['host'],
            database=config.mysql_options['dbName'],
            user=config.mysql_options['user'],
            password=config.mysql_options['passwd']
        )
        self.redis = redis.StrictRedis(
            host=config.redis_options['host'],
            port=config.redis_options['port']
        )
        handler = [
            (r'/api/imagecode', VerifyCode.ImageCodeHandler),
            (r'/api/smscode', VerifyCode.PhoneCodeHandler),
            (r'^/api/register$', Passport.RegisterHandler),
            (r'^/api/login$', Passport.LoginHandler),
            (r'^/api/check_login$', Passport.CheckLoginHandler),
            (r'^/api/profile$', Profile.ProfileHandler),
            (r'^/api/profile/avatar$', Profile.AvatarHandler),
            # (r'^/api/profile/name$', Profile.NameHandler),
            (r'^/api/profile/auth$', Profile.AuthHandler),
            (r'^/api/house/area$', House.AreaInfoHandler),
            (r'^/api/house/my$', House.MyHousesHandler),
            (r'^/api/house/info', House.HouseInfoHandler),
            (r'^/api/house/index', House.IndexHandler),
            (r'^/api/house/list2', House.HouseListRedisHandler),
            (r'^/api/house/image', House.HouseImageHandler),
            (r'^/api/order$', Order.OrderHandler),  # 下单
            (r'^/api/order/my$', Order.MyOrdersHandler),  # 我的订单，作为房客和房东同时适用
            (r'^/api/order/accept$', Order.AcceptOrderHandler),  # 接单
            (r'^/api/order/reject$', Order.RejectOrderHandler),  # 拒单
            (r'^/api/order/comment$', Order.OrderCommentHandler),
            (r'/(.*)', BaseHandler.SFHandler, {'path': os.path.join(config.settings['static_path'], 'html'),
                                                       'default_filename': 'index.html'}),

                   ]
        super(Application, self).__init__(handler, **config.settings)
