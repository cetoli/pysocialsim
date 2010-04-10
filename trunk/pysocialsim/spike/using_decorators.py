from random import uniform
from threading import Thread
import time


class ThreadDoida(Thread):
    
    def __init__(self, s):
        Thread.__init__(self)
        
    def run(self):
        print 111111111111111
        
        
t = ThreadDoida("ddd")
t.start()
time.sleep(1);
t.__init__("sss")
t.start()