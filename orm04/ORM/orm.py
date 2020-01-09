#coding=utf-8
from .fanMysql import FanMysql


class ORM():
    def save(self):
        # insert into torStus (name,age) values('asd', 22)
        # 返回的是继承这个类的类名
        tableName = self.__class__.__name__
        fieldsStr = valuesStr = '('
        for field in self.__dict__:
            # (name,age,
            fieldsStr += (field + ',')
            if isinstance(self.__dict__[field], str):
                valuesStr += ("'" + self.__dict__[field] + "',")
            else:
                valuesStr += (str(self.__dict__[field]) + ",")
        fieldsStr = fieldsStr[:len(fieldsStr)-1] + ")"
        valuesStr = valuesStr[:len(valuesStr)-1] + ")"
        sql = "insert into " + tableName + " " + fieldsStr + " values" + valuesStr
        print(sql)
        db = FanMysql()

        db.insert(sql)

    @classmethod
    def all(cls):
        # select * from torStus
        tableName = cls.__name__
        sql = 'select * from ' + tableName
        db = FanMysql()
        print(sql)
        # print(tryAWord)
        return db.getAllObj(sql, tableName)

    @classmethod
    def filter(cls):
        pass

    def delete(self):
        pass
