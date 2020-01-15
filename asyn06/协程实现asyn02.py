#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import threading

gen = None

def longIO():
    def run():
        print('开始耗时操作')
        time.sleep(5)
        try:
            global gen
            gen.send('fanxiaoye')  # 线程结束，然后send数据
        except StopIteration as e:
            pass
    threading.Thread(target=run).start()

def genCoroutine(func):
    def wrapper(*args, **kwargs):
        global gen
        gen = func(*args, **kwargs)
        next(gen)
    return wrapper

@genCoroutine
def reqA():
    print('AAAAAAAAAAAAAAAA开始')
    data = yield longIO()
    print('收到longIO的相应数据：', data)
    print('AAAAAAAAAAAAAAAA结束')


def reqB():
    print('BBBBBBBBBBBBBB开始')
    time.sleep(2)
    print('BBBBBBBBBBBBBBB结束')


def main():
    # global gen
    # gen = reqA()  # 生成一个生成器
    # next(gen)
    # 相比于01，把这三行写成了装饰器
    reqA()

    reqB()


if __name__ == '__main__':
    main()

