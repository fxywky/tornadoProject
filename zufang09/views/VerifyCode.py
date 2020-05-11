#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import constants
import random
from .BaseHandler import *
from utils.captcha.captcha import *
from utils.response_code import RET

from lib.yuntongxun.SendTemplateSMS import ccp

class ImageCodeHandler(BaseHandler):
    """图片验证码"""
    def get(self, *args, **kwargs):
        preCodeId = self.get_argument('pre')
        curCodeId = self.get_argument('cur')
        if preCodeId:
            try:
                self.redis.delete('ImageCode'+preCodeId)
                # self.redis.delete('')
            except Exception as e:
                pass

        name, text, image = captcha.generate_captcha()
        try:
            self.redis.setex('ImageCode' + curCodeId, constants.IMAGE_CODE_VALIDITY, text)
        except Exception as e:
            self.write('')
        self.set_header('Content-Type', 'image/jpg')
        self.write(image)

class PhoneCodeHandler(BaseHandler):
    def post(self):
        """获取参数
        判断图片验证码
        若成功，发送短信
        不成功，返回错误信息"""
        mobile = self.json_args.get('mobile')
        imageCodeId = self.json_args.get('imageCodeId')
        imageCodeText = self.json_args.get('imageCodeText')
        if not all((mobile, imageCodeId, imageCodeText)):
            return self.write(dict(errcode=RET.PARAMERR, errmsg='参数不完整'))
        # 判断图片验证码
        try:
            realImageCodeText = self.redis.get('ImageCode%s' % imageCodeId)
            realImageCodeText = str(realImageCodeText, 'utf-8')
        except Exception as e:
            return self.write(dict(errcode=RET.DBERR, errmsg='查询出错'))
        if not realImageCodeText:
            return self.write(dict(errcode=RET.NODATA, errmsg='验证码已过期'))
        if realImageCodeText.lower() != imageCodeText.lower():
            return self.write(dict(errcode=RET.DATAERR, errmsg='验证码错误'))
        # 生成随机验证码
        smsCode = '%04d' % random.randint(0, 9999)
        try:
            self.redis.setex('sms_code_%s' % mobile, constants.SMS_CODE_EXPIRES_SECONDS, smsCode)
        except Exception as e:
            return self.write(dict(errcode=RET.DATAERR, errmsg='验证码错误'))
        # 发送短信
        try:
            ccp.sendTemplateSMS(mobile, [smsCode, constants.SMS_CODE_EXPIRES_SECONDS/60], 1)
        except Exception as e:
            return self.write(dict(errcode=RET.THIRDERR, errmsg='发送失败'))
        self.write(dict(errcode=RET.OK, errmsg='OK'))




