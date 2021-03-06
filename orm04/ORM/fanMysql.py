#coding=utf-8

import pymysql
import config


def singleton(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


@singleton
class FanMysql():
    host = config.mysql['host']
    user = config.mysql['user']
    passwd = config.mysql['passwd']
    dbName = config.mysql['dbName']

    def connect(self):
        self.db = pymysql.connect(self.host, self.user,
                                  self.passwd, self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def getOne(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print('查询失败')
        return res

    def getAll(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print('查询失败')
        return res

    def getAllObj(self, sql, tableName, *args):
        resList = []
        fieldsList = []
        if (len(args) > 0):
            for item in args:
                fieldsList.append(item)
        else:
            fieldSql = "select COLUMN_NAME from " \
                       "information_schema.COLUMNS where table_name" \
                       " ='%s' and table_schema = '%s'" % \
                       (tableName, self.dbName)
            fields = self.getAll(fieldSql)
            for item in fields:
                fieldsList.append(item[0])

        # 执行查询数据sql
        res = self.getAll(sql)
        for item in res:
            obj = {}
            count = 0
            for x in item:
                obj[fieldsList[count]] = x
                count += 1
            resList.append(obj)
        print(resList)
        return resList

    def getFilter(self, sql, tableName, searchField):
        resList = []
        fieldsList = []
        fieldSql = "select COLUMN_NAME from " \
                   "information_schema.COLUMNS where table_name" \
                   " ='%s' and table_schema = '%s'" % \
                   (tableName, self.dbName)
        fields = self.getAll(fieldSql)
        print('fields=', fields)

        if '*' in searchField:
            for item in fields:
                fieldsList.append(item[0])
            print('fieldsList= ', fieldsList)
        else:
            for item in searchField:
                for field in fields:
                    if item in field:
                        fieldsList.append(item)
            print('fieldsList= ', fieldsList)

        # 执行查询数据sql
        res = self.getAll(sql)
        print(res)
        for item in res:
            obj = {}
            count = 0
            for x in item:
                obj[fieldsList[count]] = x
                count += 1
            resList.append(obj)
        print(resList)
        return resList



    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.connect()
            # 删除, 返回的是删除的是个数
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print('事务提交失败')
            self.db.rollback()
        return count