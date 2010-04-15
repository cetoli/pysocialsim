"""
Defines the module with the implementation of PriorityQueue class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/08/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.base.decorators import public
from threading import Semaphore
from pysocialsim.common.util.rotines import requires, pre_condition, returns
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from bisect import insort

class PriorityQueue(Object):
    """
    Implements a synchronized priority queue of simulation event.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 27/08/2009
    """

    def initialize(self):
        self.__queue = []
    
    @public
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
        requires(item, ISimulationEvent)
        requires(priority, int)
        
        pre_condition(item, lambda x: x <> None)
        pre_condition(priority, lambda x: x >= 0)
        
        sem = Semaphore()
        sem.acquire()
#        for event in self.__queue:
#            if event[1] == item:
#                return None
        self.__queue.append(item)
        #insort(self.__queue, (priority, item))
        sem.release()
        return returns(item, ISimulationEvent)
        
    @public
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
        item = self.__queue.pop(0)
        sem.release()
        return returns(item, ISimulationEvent)
    
    @public
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
        return returns(size, int)
    
    @public
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
        first = self.__queue[0]
        sem.release()
        return returns(first, ISimulationEvent)
    
    @public
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
        last = self.__queue[len(self.__queue) - 1]
        sem.release()
        return returns(last, ISimulationEvent)
    
    @public
    def clear(self):
        """
        Clean the queue of simulation events.
        @rtype: NoneType
        """
        del self.__queue
        self.__queue = []