from pysocialsim.base.object import Object
from threading import Semaphore
import bisect

class PriorityQueue(Object):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self):
        self.__queue = []
        
    def enqueue(self, item, priority):
        sem = Semaphore()
        sem.acquire()
        bisect.insort(self.__queue, (priority, item))
        sem.release()
        
    def dequeue(self):
        sem = Semaphore()
        sem.acquire()
        item = self.__queue.pop(0)[1]
        sem.release()
        return item
        
    def size(self):
        sem = Semaphore()
        sem.acquire()
        size = len(self.__queue)
        sem.release()
        return size
    
    def getFirst(self):
        sem = Semaphore()
        sem.acquire()
        first = self.__queue[0]
        sem.release()
        return first
    
    def getLast(self):
        sem = Semaphore()
        sem.acquire()
        last = self.__queue[len(self.__queue) - 1]
        sem.release()
        return last