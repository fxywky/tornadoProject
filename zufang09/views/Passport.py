#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging
from .BaseHandler import BaseHandler
import hashlib
from utils.session import *
import config

class RegisterHandler(BaseHandler):
    """注册"""
    def post(self):
        # sms_code_
        mobile = self.json_args.get('mobile')
        smsCode = self.json_args.get('phonecode')
        password = self.json_args.get('password')
        if not all([mobile, smsCode, password]):
            return self.write({'errcode': 1, "errmsg": '参数错误'})
        realCode = self.redis.get('sms_code_' + mobile)
        realCode = str(realCode, 'utf-8')
        # print('realCode= ', realCode)
        # print('smsCode= ', smsCode)
        if realCode != str(smsCode):
            return self.write({'errcode': 2, 'errmsg': '验证码无效'})
        password = hashlib.sha256((config.passwdHashKey + password).encode('utf-8')).hexdigest()
        try:
            # 返回的是主键ｉｄ值
            res = self.db.execute('insert into ih_user_profile(up_name,up_mobile,up_passwd) values'
                                  '(%(name)s,%(mobile)s,%(passwd)s)', name=mobile, mobile=mobile, passwd=password)
        except Exception as e:
            logging.error(e)
            return self.write({'errcode': 3, 'errmsg': '手机号已注册'})
        try:
            self.session = Session(self)
            self.session.data['user_id'] = res
            self.session.data['name'] = mobile
            self.session.data['mobile'] = mobile
            self.session.save()   # 存入redis，并存cookie
            print('保存成功')
        except Exception as e:
            print('session 没有存入redis')
            logging.error(e)
        self.write({'errcode': 0, 'errmsg': 'OK'})


class LoginHandler(BaseHandler):
    def post(self):
        mobile = self.json_args.get('mobile')
        password = self.json_args.get('password')
        if not all([mobile, password]):
            return self.write({'errcode': 1, 'errmsg': '参数错误'})
        res = self.db.get('select up_user_id,up_name,up_passwd from ih_user_profile where up_mobile=%(mobile)s', mobile=mobile)
        password = hashlib.sha256((config.passwdHashKey + password).encode()).hexdigest()
        print("res['up_passwd']= ", res['up_passwd'])
        print("password=", password)
        if res and res['up_passwd'] == password:
            try:
                self.session = Session(self)
                self.session.data['user_id'] = res['up_user_id']
                self.session.data['name'] = res['up_name']
                self.session.data['mobile'] = mobile
                self.session.save()
            except Exception as e:
                logging.error(e)
            return self.write({'errcode': 0, 'errmsg': 'OK'})
        else:
            return self.write({'errcode': 2, 'errmsg': '手机号或密码错误！'})


class CheckLoginHandler(BaseHandler):
    def get(self):
        if self.get_current_user():
            self.write({'errcode': 0, 'errmsg': 'true', 'data': {'name': self.session.data.get('name')}})
        else:
            self.write({'errcode': 1, 'errmsg': 'false'})



class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        # self.db
        # self.redis
        # logging.debug('debug msg')
        # logging.info('debug msg')
        # logging.warning('debug msg')
        # logging.error('debug msg')
        # print('print msg')
        self.write('hello world')

