#!/usr/bin/env python
# encoding: utf-8
from Queue import Queue  
# import random  
import threading  
import time  
#Producer thread  
  
class Producer(threading.Thread):  
    def __init__(self,t_name,queue):
        threading.Thread.__init__(self, name=t_name);
        self.data=queue
    def run(self):
        for i in range(20):
            self.data.put('haha'.upper()+str(i));
            print time.ctime()+'加入数据haha%d' % (i)
  
#Main thread
def main():  
    queue = Queue()  
    producer = Producer('Pro.', queue)  
    producer.start()  
    producer.join() 
    for i in range(1000):
        print  queue.get()
        print i
    print 'All threads terminate!'  
  
if __name__ == '__main__':  
    main()  


