# tornadoProject
编写顺序是按照后面的数字进行记录的

访问静态文件，这个路由写在最后面
```
(r'/(.*)$', tornado.web.StaticFileHandler, {'path': os.path.join(config.settings['static_path'],'html'),'default_filename':'index.html'})
```

# ORM
models.py中定义模型类，和Django中的类似。

创建的模型类继承于ORM类，例如torStus。

ORM类最好定义在一个脚本文件中orm.py中

ORM类中有save()方法，all()类方法，filter()类方法等等

①save()方法用于将创建的对象保存到数据库中，self.____class____.__name__返回的是继承ORM类的类名torStus。self.__dict__返回时的是继承ORM的类初始化传来的参数，以字典的形式{'name':'fan', 'age':24} <br>

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
```
"select COLUMN_NAME from information_schema.COLUMNS where table_name ='%s' and table_schema = '%s'" % (tableName, self.dbName)
#获取字段名
```

# xsrf和用户验证【重点是逻辑】 
### xsrf
在首页（静态页面）的Handler里，继承StaticFileHandler，__init__方法中调用父类的初始化方法后，加一句self.xsrf_token <br>

```
    def _ init_(self, *args, **kwargs):
        super(SFHandler, self).__init__(*args, **kwargs)
        self.xsrf_token
```

### 用户验证【重点是逻辑】
当有的页面需要logined才能查看时，比如个人主页等，需要login验证。不论我们从哪一网址进入login页面，当logined之后，再重定向至该页面。<br><br>

需要验证的页面，可以用get_current_user()方法，若返回None，即验证失败则需要重定向至配置中login_url所制定的路由，若验证通过，则走@tornado.web.authenticated装饰器装饰的方法，即进入个人主页。
```
    def get_current_user(self):
        # /home
        flag = self.get_argument('flag', None)
        return flag
```

#### 验证失败
重定向至配置中login_url所制定的路由时，url中会多加 ？next=/...，即指明从哪个页面转来的，可以通过：
```
next0 = self.get_query_argument('next', '/')   # 获取next的值，即登陆成功后要转向的页面的url
url = 'login?next=' + next0
```
先通过get方法，将url传给前端页面要提交表单的action属性，这样再通过post方式，将表单数据和url传给post方法，这时验证通过与否可以重定向至转来的页面（成功），或是再次登录（失败）
