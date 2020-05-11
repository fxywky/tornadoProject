# coding=utf-8
import uuid
import logging
import config
import json

class Session(object):
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.session_id = str(self.request_handler.get_secure_cookie('session_id'), 'utf-8')
        print('self.session_id= ', self.session_id)
        data = {}
        # 用户第一次访问，生成一个session_id, 全局唯一
        if not self.session_id:
            self.session_id = uuid.uuid4().hex
            self.data = {}
        else:
            # 拿到了session_id ,去redis中取数据
            try:
                data = self.request_handler.redis.get('sess_%s' % self.session_id)
            except Exception as e:
              logging.error(e)
              self.data = {}
            if not data:
                self.data = {}
            else:
                self.data = json.loads(data)

    def save(self):
        json_data = json.dumps(self.data)
        try:
            self.request_handler.redis.setex('sess_%s' % self.session_id, config.session_expires, json_data)
        except Exception as e:
            logging.error(e)
            raise Exception('save session failed Eric')
        else:
            self.request_handler.set_secure_cookie('session_id', self.session_id)

    def clear(self):
        self.request_handler.clear_cookie('session_id')
        try:
            self.request_handler.redis.delete('sess_%s' % self.session_id)
        except Exception as e:
            logging.error(e)
