from pysocialsim.base.object import Object
from threading import Semaphore
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.base.decorator.require import require
import bisect

class PriorityQueue(Object):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self):
        self.__queue = []
    
    @public
    def enqueue(self, item, priority):
        sem = Semaphore()
        sem.acquire()
        bisect.insort(self.__queue, (priority, item))
        sem.release()
        
    @public
    def dequeue(self):
        sem = Semaphore()
        sem.acquire()
        item = self.__queue.pop(0)[1]
        sem.release()
        return item
    
    @public
    def size(self):
        sem = Semaphore()
        sem.acquire()
        size = len(self.__queue)
        sem.release()
        return size
    
    @public
    def getFirst(self):
        sem = Semaphore()
        sem.acquire()
        first = self.__queue[0]
        sem.release()
        return first
    
    @public
    def getLast(self):
        sem = Semaphore()
        sem.acquire()
        last = self.__queue[len(self.__queue) - 1]
        sem.release()
        return last