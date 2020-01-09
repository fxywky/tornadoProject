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
    def filter(cls, *args, **kwargs):
        tableName = cls.__name__
        # print(args[0], args[1], len(args))
        # print(kwargs)
        # id,name,age
        # 无条件
        sql = "select "
        if '*' not in args:
            for searchField in args:
                sql += searchField + ','
            sql = sql[:-1] + ' ' + 'from ' + tableName + ' where'
            # print(sql)
        else:
            sql += '* ' + 'from ' + tableName + ' where'

        if len(kwargs) != 0:
            for field in kwargs:
                if isinstance(kwargs[field], str):
                    sql += ' ' + field + '=' + '"' + kwargs[field] + '" and'
                else:
                    sql += ' ' + field + '=' + str(kwargs[field]) + ' and'
            sql = sql[:-4]
        print(sql)

        db = FanMysql()
        return db.getFilter(sql, tableName, args)

    @classmethod
    def delete(cls, **kwargs):
        tableName = cls.__name__
        print(kwargs)
        if len(kwargs) == 0:
            sql = 'delete from ' + tableName
            db = FanMysql()
            count = db.delete(sql)
            # 删除, 返回的是删除的是个数
            return count
        else:
            sql = 'delete from ' + tableName + ' where'
            for field in kwargs:
                if isinstance(kwargs[field], str):
                    sql += ' ' + field + '=' + '"' + kwargs[field] + '" and'
                else:
                    sql += ' ' + field + '=' + str(kwargs[field]) + ' and'
            sql = sql[:-4]
            print(sql)
            db = FanMysql()
            count = db.delete(sql)
            return count



