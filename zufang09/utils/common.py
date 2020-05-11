#coding=utf-8
import functools

from utils.response_code import RET

def require_logined(func):
    # 加这个装饰器是保持func原来的函数名
    @functools.wraps(func)
    def wrapper(requestHandlerObj, *args, **kwargs):   # requestHandlerObj就是调用的class
        # 如果不是空的，说明有数据，有ｓｅｓｓｉｏｎｉｄ
        if requestHandlerObj.get_current_user():
            func(requestHandlerObj, *args, **kwargs)
        else:
            a = requestHandlerObj.request.full_url()
            print(a)
            requestHandlerObj.write({'errcode': RET.SESSIONERR, 'errmsg': '用户未登录'})
    return wrapper
