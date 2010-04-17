"""
Defines the module with the implementation of PriorityQueue class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/08/2009
"""
from threading import Semaphore
from bisect import insort
class PriorityQueue(object):
    """
    Implements a synchronized priority queue of simulation event.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 27/08/2009
    """

    def __init__(self):
        self.initialize()

    def initialize(self):
        self.__queue = []
    
    
    def enqueue(self, item, priority):
        """
        Enqueues a simulation event.
        @param item: an ISimulationEvent
        @type item: ISimulationEvent
        @param priority: a int
        @type priority: int
        @return: an ISimulationEvent
        @rtype: ISimulationEvent
        """
        sem = Semaphore()
        sem.acquire()
#        for event in self.__queue:
#            if event[1] == item:
#                return None
        
        insort(self.__queue, (priority, item))
        sem.release()
        return item
        
    
    def dequeue(self):
        """
        Dequeues a simulation event.
        @return: an ISimulationEvent
        @rtype: ISimulationEvent
        """
        sem = Semaphore()
        sem.acquire()
        if len(self.__queue) == 0:
            sem.release()
            return None
        item = self.__queue.pop(0)[1]
        sem.release()
        return item
    
    
    def size(self):
        """
        Returns the size of queue.
        @return: an int
        @rtype: int
        """
        sem = Semaphore()
        sem.acquire()
        size = len(self.__queue)
        sem.release()
        return size
    
    
    def getFirst(self):
        """
        Gets the first simulation event of queue.
        @return: an ISimulationEvent
        @rtype: ISimulationEvent
        """
        sem = Semaphore()
        sem.acquire()
        if len(self.__queue) == 0:
            sem.release()
            return
        first = self.__queue[0][1]
        sem.release()
        return first
    
    
    def getLast(self):
        """
        Gets the first simulation event of queue.
        @return: an ISimulationEvent
        @rtype: ISimulationEvent
        """
        sem = Semaphore()
        sem.acquire()
        if len(self.__queue) == 0:
            sem.release()
            return
        last = self.__queue[len(self.__queue) - 1][1]
        sem.release()
        return last
    
    
    def clear(self):
        """
        Clean the queue of simulation events.
        @rtype: NoneType
        """
        del self.__queue
        self.__queue = []