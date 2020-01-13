# tornadoProject
编写顺序是按照后面的数字进行记录的

访问静态文件，这个路由写在最后面
r'/(.*)$', tornado.web.StaticFileHandler, {'path': os.path.join(config.settings['static_path'],'html'),'default_filename':'index.html'})


# ORM
models.py中定义模型类，和Django中的类似。

创建的模型类继承于ORM类，例如torStus。

ORM类最好定义在一个脚本文件中orm.py中

ORM类中有save()方法，all()类方法，filter()类方法等等

①save()方法用于将创建的对象保存到数据库中，self.__class__.__name__返回的是继承ORM类的类名torStus。
self.__dict__返回时的是继承ORM的类初始化传来的参数，以字典的形式{'name':'fan', 'age':24} <br>

```
class ORM():
    def save(self):
        insert into torStus (name,age) values('asd', 22)
        返回的是继承这个类的类名<br>
        tableName = self.__class__.__name__
        fieldsStr = valuesStr = '('
        for field in self.__dict__
```

②filter()类方法，通过继承类torStus.filter(...)使用，可以这样理解，因为查询无需创建一个具体的对象<br>
```
@classmethod
    def filter(cls, *args, **kwargs):
        tableName = cls.__name__
        # print(args[0], args[1], len(args))
        # print(kwargs)
        # id,name,age
```

这里的args代表要查询的字段名，kwargs为查询条件<br>

ORM类主要的作用是生成sql语句，然后传给fanMysql.py 中的FanMysql类执行，完成与数据库的交互<br>

FanMysql是单例类，将从数据库查询的数据重组并返回<br>

"select COLUMN_NAME from information_schema.COLUMNS where table_name ='%s' and table_schema = '%s'" % (tableName, self.dbName)
获取字段名<br>
