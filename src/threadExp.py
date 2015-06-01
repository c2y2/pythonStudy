#!/usr/bin/env python
# encoding: utf-8

from sys import stdout
import threading
import time
from __builtin__ import str


class myThread(threading.Thread):
    def __init__(self,thread_name):
        threading.Thread.__init__(self,name=thread_name)
    def run(self):
        for i in range(100):
            print "%s 第 %s 个!"%(self.getName(),str(i))
            time.sleep(5)
            
if __name__ == '__main__':
    thread1 = myThread("myThreadname")
    thread1.start();
    running = threading.currentThread()
    time.sleep(5)
    thread1.join();
    for i in range(5):
        stdout.write(str(i)+'\t')