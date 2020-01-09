#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import config
import os
from models import torStus

class StusHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # stu = torStus('fanfan', 88)
        # stu.save()
        #
        # self.write('ok')

        stus = torStus.all()

        self.render('students.html', stus=stus)
