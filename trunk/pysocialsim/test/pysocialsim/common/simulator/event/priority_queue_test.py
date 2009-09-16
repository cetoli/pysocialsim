"""
Defines the module with the unit test of PriorityQueue class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/08/2009
"""
from pysocialsim.common.simulator.event.priority_queue import PriorityQueue
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent
from random import randint

import unittest

class PriorityQueueTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(PriorityQueue())
        
    def testEnqueueEvents(self):
        queue = PriorityQueue()
        
        event1 = self.SimulationEventForTest(randint(0, 1000), 2)
        event2 = self.SimulationEventForTest(randint(0, 1000), 1)
        event3 = self.SimulationEventForTest(randint(0, 1000), 3)
        
        self.assertEquals(event1, queue.enqueue(event1, event1.getPriority()))
        self.assertEquals(1, queue.size())
        self.assertEquals(event2, queue.enqueue(event2, event2.getPriority()))
        self.assertEquals(2, queue.size())
        self.assertEquals(event3, queue.enqueue(event3, event3.getPriority()))
        self.assertEquals(3, queue.size())
        
        self.assertEquals(event2, queue.getFirst())
        self.assertEquals(event3, queue.getLast())
        
        self.assertFalse(queue.enqueue(event1, event1.getPriority()))
        self.assertFalse(queue.enqueue(event2, event2.getPriority()))
        self.assertFalse(queue.enqueue(event3, event3.getPriority()))
        
    def testDequeueEvents(self):
        queue = PriorityQueue()
        
        event1 = self.SimulationEventForTest(randint(0, 1000), 2)
        event2 = self.SimulationEventForTest(randint(0, 1000), 1)
        event3 = self.SimulationEventForTest(randint(0, 1000), 3)
        
        self.assertEquals(event1, queue.enqueue(event1, event1.getPriority()))
        self.assertEquals(1, queue.size())
        self.assertEquals(event2, queue.enqueue(event2, event2.getPriority()))
        self.assertEquals(2, queue.size())
        self.assertEquals(event3, queue.enqueue(event3, event3.getPriority()))
        self.assertEquals(3, queue.size())
        
        self.assertEquals(event2, queue.getFirst())
        self.assertEquals(event3, queue.getLast())
        
        self.assertEquals(event2, queue.dequeue())
        self.assertEquals(event1, queue.dequeue())
        self.assertEquals(event3, queue.dequeue())
        
        self.assertFalse(queue.dequeue())
        self.assertFalse(queue.getFirst())
        self.assertFalse(queue.getLast())
        
    def testClearPriority(self):
        queue = PriorityQueue()
        
        event1 = self.SimulationEventForTest(randint(0, 1000), 2)
        event2 = self.SimulationEventForTest(randint(0, 1000), 1)
        event3 = self.SimulationEventForTest(randint(0, 1000), 3)
        
        self.assertEquals(event1, queue.enqueue(event1, event1.getPriority()))
        self.assertEquals(1, queue.size())
        self.assertEquals(event2, queue.enqueue(event2, event2.getPriority()))
        self.assertEquals(2, queue.size())
        self.assertEquals(event3, queue.enqueue(event3, event3.getPriority()))
        self.assertEquals(3, queue.size())
        
        queue.clear()
        self.assertEquals(0, queue.size())
        
        
    class SimulationEventForTest(AbstractSimulationEvent):
        
        def __init__(self, peerId, priority):
            AbstractSimulationEvent.initialize(self, "TEST", peerId, priority)
        
