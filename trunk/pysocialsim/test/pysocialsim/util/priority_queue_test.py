from pysocialsim.util.priority_queue import PriorityQueue
from pymockobject.events import ReturnValue
from pysocialsim.simulator.event.i_event import IEvent
import pymockobject
import unittest

class PriorityQueueTest(unittest.TestCase):
    
    def setUp(self):
        self.__queue = PriorityQueue()
    
    def test_enqueue_events(self):
        event1 = pymockobject.create(IEvent)
        event1.getPriority.will(ReturnValue(1))
        
        event2 = pymockobject.create(IEvent)
        event2.getPriority.will(ReturnValue(2))
        
        event3 = pymockobject.create(IEvent)
        event3.getPriority.will(ReturnValue(3))
        
        self.assertEquals(event3, self.__queue.enqueue(event3, event3.getPriority()))
        self.assertEquals(1, self.__queue.size())
        self.assertEquals(event3, self.__queue.getFirst())
        self.assertEquals(event3, self.__queue.getLast())
        
        self.assertEquals(event2, self.__queue.enqueue(event2, event2.getPriority()))
        self.assertEquals(2, self.__queue.size())
        self.assertEquals(event2, self.__queue.getFirst())
        self.assertEquals(event3, self.__queue.getLast())
        
        self.assertEquals(event1, self.__queue.enqueue(event1, event1.getPriority()))
        self.assertEquals(3, self.__queue.size())
        self.assertEquals(event1, self.__queue.getFirst())
        self.assertEquals(event3, self.__queue.getLast())
        
        self.assertRaises(TypeError, self.__queue.enqueue, None, 1)
        self.assertEquals(3, self.__queue.size())
        self.assertRaises(TypeError, self.__queue.enqueue, event1, None)
        self.assertEquals(3, self.__queue.size())
        self.assertRaises(TypeError, self.__queue.enqueue, None, None)
        self.assertEquals(3, self.__queue.size())
        
    def test_dequeue_events(self):
        event1 = pymockobject.create(IEvent)
        event1.getPriority.will(ReturnValue(1))
        
        event2 = pymockobject.create(IEvent)
        event2.getPriority.will(ReturnValue(2))
        
        event3 = pymockobject.create(IEvent)
        event3.getPriority.will(ReturnValue(3))
        
        self.assertEquals(event3, self.__queue.enqueue(event3, event3.getPriority()))
        self.assertEquals(1, self.__queue.size())
        self.assertEquals(event3, self.__queue.getFirst())
        self.assertEquals(event3, self.__queue.getLast())
        
        self.assertEquals(event2, self.__queue.enqueue(event2, event2.getPriority()))
        self.assertEquals(2, self.__queue.size())
        self.assertEquals(event2, self.__queue.getFirst())
        self.assertEquals(event3, self.__queue.getLast())
        
        self.assertEquals(event1, self.__queue.enqueue(event1, event1.getPriority()))
        self.assertEquals(3, self.__queue.size())
        self.assertEquals(event1, self.__queue.getFirst())
        self.assertEquals(event3, self.__queue.getLast())
        
        self.assertEquals(event1, self.__queue.dequeue())
        self.assertEquals(2, self.__queue.size())
        
        self.assertEquals(event2, self.__queue.dequeue())
        self.assertEquals(1, self.__queue.size())
        
        self.assertEquals(event3, self.__queue.dequeue())
        self.assertEquals(0, self.__queue.size())
        
        self.assertFalse(self.__queue.dequeue())