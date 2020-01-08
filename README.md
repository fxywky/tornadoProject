# tornadoProject
编写顺序是按照后面的数字进行记录的

访问静态文件，这个路由写在最后面
r'/(.*)$', tornado.web.StaticFileHandler, {'path': os.path.join(config.settings['static_path'], 'html'),
                                                        'default_filename': 'index.html'})
