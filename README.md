# tornadoProject
编写顺序是按照后面的数字进行记录的

访问静态文件，这个路由写在最后面
r'/(.*)$', tornado.web.StaticFileHandler, {'path': os.path.join(config.settings['static_path'], 'html'),
                                                        'default_filename': 'index.html'})

models.py中定义模型类，和Django中的类似。
创建的模型类继承于ORM类，例如torStus。
ORM类最好定义在一个脚本文件中orm.py中
ORM类中有save()方法，all()类方法，filter()类方法等等

①save()方法用于将创建的对象保存到数据库中，self.__class__.__name__返回的是继承ORM类的类名torStus。self.__dict__返回时的是继承ORM的类初始化传来的参数，以字典的形式{'name':'fan', 'age':24}

