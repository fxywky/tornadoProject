#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web
import config
import os
from models import torStus

class StusHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 插入
        # stu = torStus('fanfan', 88)
        # stu.save()
        #
        # self.write('ok')

        # 读取所有信息
        # stus = torStus.all()
        #
        # self.render('students.html', stus=stus)

        # 删除,写的是条件，不写就全删 返回的是删除的是个数
        count = torStus.delete(age=34)
        self.write(str(count))

        # 查询 前面是显示的字段，后面是查询的条件
        # stus = torStus.filter('name', 'age', '*', age=34)
        # self.render('students.html', stus=stus)

