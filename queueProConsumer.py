#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   queueProConsumer.py
@Time    :   2019/09/23 16:43:38
@Author  :   baoy.bao 
@Version :   1.0
@Contact :   zeroleavebaoy@163.com
@License :   (C)Copyright 2019-2021
@Desc    :   None
'''

import threading
from queue import Queue
import time


queue = Queue()


class Producer(threading.Thread):
    def run(self):
        count = 0
        global queue
        while True:
            for i in range(100):
                if queue.qsize() > 1000:
                    pass
                else:
                    count = count + 1
                    msg = '生产产品' + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            for i in range(3):
                if queue.qsize() < 100:
                    pass
                else:
                    msg = self.name + '消费了' + queue.get() + '\n'
                    print(msg)
            time.sleep(1)
            

def test():
    for i in range(500):
        queue.put('初始产品' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(2):
        c = Consumer()
        c.start()


if __name__ == "__main__":
    test()
    pass