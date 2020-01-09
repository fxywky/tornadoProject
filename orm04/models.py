#coding=utf-8

from ORM.orm import ORM

class torStus(ORM):
    def __init__(self, name, age):
        self.name = name
        self.age = age