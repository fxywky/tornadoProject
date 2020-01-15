#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import threading

# 我理解的next()就是往下走。当yield的时候，就是卡在那里，next的时候，就会运行yield后面的程序
def genCoroutine(func):
    def wrapper(*args, **kwargs):
        gen0 = func(*args, **kwargs)    # reqA 的生成器
        gen1 = next(gen0)               # longIO的生成器
        def run(g):
            res = next(g)   # 获得返回的数据
            try:
                gen0.send(res)
            except StopIteration as e:
                pass
        threading.Thread(target=run, args=(gen1,)).start()
    return wrapper


def longIO(a):
    print('开始耗时操作')
    time.sleep(5)
    print('结束耗时操作')
    # 返回数据
    a += 1
    yield a


@genCoroutine
def reqA(a):
    print('AAAAAAAAAAAAAAAA开始')
    data = yield longIO(a)
    print('收到longIO的相应数据：', data)
    print('AAAAAAAAAAAAAAAA结束')


def reqB():
    print('BBBBBBBBBBBBBB开始')
    time.sleep(2)
    print('BBBBBBBBBBBBBBB结束')


def main():
    reqA(a=1)
    reqB()


if __name__ == '__main__':
    main()

