#！/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import threading


def longIO(callbackData):
    def run(cb):
        print('开始执行耗时操作')
        time.sleep(5)
        print('结束执行耗时操作')
        cb('fanxiaoye')
    threading.Thread(target=run, args=(callbackData,)).start()

def callback(data):
    print('开始执行回调函数')
    print('接收到longIO的相应data= ', data)
    print('结束执行回调函数')

def reqA():
    print('reqA开始工作')
    longIO(callback)
    print('reqA结束工作')


def reqB():
    print('reqB开始工作')
    time.sleep(2)
    print('reqB结束工作')

def main():
    reqA()
    reqB()

if __name__ == '__main__':
    main()
