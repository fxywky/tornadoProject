#coding=utf-8
import logging

from .BaseHandler import BaseHandler
from utils.common import require_logined
from config import image_url_prefix
from utils.response_code import RET
from utils.image_storage import storage

class ProfileHandler(BaseHandler):
    @require_logined
    def get(self):
        userId = self.session.data['user_id']
        try:
            ret = self.db.get('select up_name,up_mobile,up_avatar from ih_user_profile where up_user_id=%s' % userId)
        except Exception as e:
            logging.error(e)
            return self.write({'errcode': 4101, 'errmsg': 'no data'})
        if ret['up_avatar']:
            imgUrl = image_url_prefix + ret['up_avatar']
        else:
            imgUrl = None
        self.write({'errcode': 0, 'errmsg': 'OK', 'data':{'user_id': userId, 'name': ret['up_name'], 'mobile': ret['up_mobile'], 'avatar': imgUrl}})


class AvatarHandler(BaseHandler):
    @require_logined
    def post(self):
        """头像"""
        # 获取user_id
        userId = self.session.data['user_id']
        try:
            avatar = self.request.files['avatarfan'][0]['body']
        except Exception as e:
            logging.error(e)
            return self.write({'errcode': RET.PARAMERR, 'errmsg': '参数错误'})
        try:
            imgName = storage(avatar)
        except Exception as e:
            logging.error(e)
            imgName = None
        if not imgName:
            return self.write({'errcode': RET.PARAMERR, 'errmsg': '参数错误'})
        try:
            ret = self.db.execute('update ih_user_profile set up_avatar=%s where up_user_id=%s', imgName, userId)
        except Exception as e:
            logging.error(e)
            return self.write({'errcode': RET.DBERR, 'errmsg': 'upload failed'})
        imgUrl = image_url_prefix + imgName
        self.write({'errcode': RET.OK, 'errmsg': 'OK', 'url': imgUrl})

class AuthHandler(BaseHandler):
    """实名认证"""
    @require_logined
    def get(self):
        userId = self.session.data['user_id']
        try:
            ret = self.db.get("select up_real_name,up_id_card from ih_user_profile where up_user_id=%s", userId)
        except Exception as e:
            logging.error(e)
            return self.write({'errcode': RET.DBERR, 'errmsg': 'get data failed'})
        logging.debug(ret)
        if not ret:
            return self.write({'errcode': RET.NODATA, 'errmsg': 'no data'})
        self.write({'errcode': RET.OK, 'errmsg': 'OK', 'data': {'real_name': ret.get('up_real_name', ''), 'id_card': ret.get('up_id_card', '')}})

    @require_logined
    def post(self):
        userId = self.session.data['user_id']
        realName = self.json_args.get('real_name')
        idCard = self.json_args.get('id_card')
        print('realName= ', realName)
        print('idCard= ', idCard)
        if realName in (None, '') or idCard in (None, ''):
            return self.write({'errcode': RET.PARAMERR, 'errmsg': 'para erro'})
        # 判断身份证号格式
        try:
            self.db.execute_rowcount("update ih_user_profile set up_real_name=%s,up_id_card=%s where up_user_id=%s",
                                     realName, idCard, userId)
        except Exception as e:
            logging.error(e)
            return self.write({"errcode": RET.DBERR, "errmsg": "update failed"})
        self.write({"errcode": RET.OK, "errmsg": "OK"})
