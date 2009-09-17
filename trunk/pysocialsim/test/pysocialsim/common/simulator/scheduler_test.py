"""
Defines the module with the unit test for Scheduler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/09/2009
"""
from pysocialsim.common.simulator.scheduler import Scheduler
from pysocialsim.common.simulator.i_simulator import ISimulator
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.error.invalid_value_error import InvalidValueError
import pymockobject

import unittest

class SchedulerTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        simulator = pymockobject.create(ISimulator)
        self.assertTrue(Scheduler(simulator))
        
        scheduler = Scheduler(simulator)
        self.assertEquals(simulator, scheduler.getSimulator())
        
        self.assertRaises(InvalidValueError, scheduler.countTimesForPeer, IPeerToPeerNetwork.SUPER_PEER, 0)
        self.assertRaises(InvalidValueError, scheduler.countTimesForPeer, IPeerToPeerNetwork.SIMPLE_PEER, 0)
        self.assertRaises(InvalidValueError, scheduler.getTimeForPeer, IPeerToPeerNetwork.SUPER_PEER, 0)
        self.assertRaises(InvalidValueError, scheduler.getTimesForPeer, IPeerToPeerNetwork.SUPER_PEER, 0)
        self.assertRaises(InvalidValueError, scheduler.getTimeForPeer, IPeerToPeerNetwork.SIMPLE_PEER, 0)
        self.assertRaises(InvalidValueError, scheduler.getTimesForPeer, IPeerToPeerNetwork.SIMPLE_PEER, 0)
        
        self.assertRaises(TypeError, Scheduler, "")
        self.assertRaises(TypeError, Scheduler, 1)
        self.assertRaises(TypeError, Scheduler, 0.66)
        self.assertRaises(TypeError, Scheduler, True)
        self.assertRaises(TypeError, Scheduler, False)
        
        self.assertRaises(InvalidValueError, Scheduler, None)
    
    def testRegisterTimeForPeer(self):
        scheduler = Scheduler(pymockobject.create(ISimulator))
        
        self.assertEquals(9600, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1, 9600))
        self.assertEquals(1, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertEquals(9600, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        
        self.assertEquals(10000, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1, 10000))
        self.assertEquals(2, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertEquals(10000, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        
        self.assertEquals(50000, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1, 50000))
        self.assertEquals(3, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertEquals(50000, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        
        self.assertEquals(9600, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2, 9600))
        self.assertEquals(1, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertEquals(9600, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        
        self.assertEquals(10000, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2, 10000))
        self.assertEquals(2, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertEquals(10000, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        
        self.assertEquals(50000, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2, 50000))
        self.assertEquals(3, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertEquals(50000, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        
        self.assertEquals(900, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1, 900))
        self.assertEquals(1, scheduler.countTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertEquals(900, scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        
        self.assertEquals(1800, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1, 1800))
        self.assertEquals(2, scheduler.countTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertEquals(1800, scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        
        self.assertEquals(2700, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1, 2700))
        self.assertEquals(3, scheduler.countTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertEquals(2700, scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        
        self.assertRaises(InvalidValueError, scheduler.registerTimeForPeer, 2, 1, 1)
        self.assertRaises(InvalidValueError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SIMPLE_PEER, 0, 1)
        self.assertRaises(InvalidValueError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SIMPLE_PEER, 1, 0)
        
        self.assertRaises(InvalidValueError, scheduler.registerTimeForPeer, None, 1, 1)
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, "", 1, 1)
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, 0.07, 1, 1)
        
        self.assertRaises(InvalidValueError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SIMPLE_PEER, None, 1)
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SIMPLE_PEER, "", 1)
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SIMPLE_PEER, 0.6, 1)
        
        self.assertRaises(InvalidValueError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SIMPLE_PEER, 1, None)
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SIMPLE_PEER, 1, "")
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SIMPLE_PEER, 1, 0.888)
        
        self.assertRaises(InvalidValueError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SUPER_PEER, None, 1)
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SUPER_PEER, "", 1)
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SUPER_PEER, 0.6, 1)
        
        self.assertRaises(InvalidValueError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SUPER_PEER, 1, None)
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SUPER_PEER, 1, "")
        self.assertRaises(TypeError, scheduler.registerTimeForPeer, IPeerToPeerNetwork.SUPER_PEER, 1, 0.888)
        
    def testUnregisterTimeForPeer(self):
        scheduler = Scheduler(pymockobject.create(ISimulator))
        
        self.assertEquals(9600, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1, 9600))
        self.assertEquals(1, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertEquals(9600, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        
        self.assertEquals(10000, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1, 10000))
        self.assertEquals(2, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertEquals(10000, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        
        self.assertEquals(50000, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1, 50000))
        self.assertEquals(3, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertEquals(50000, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 1))
        
        self.assertEquals(9600, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2, 9600))
        self.assertEquals(1, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertEquals(9600, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        
        self.assertEquals(10000, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2, 10000))
        self.assertEquals(2, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertEquals(10000, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        
        self.assertEquals(50000, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2, 50000))
        self.assertEquals(3, scheduler.countTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertEquals(50000, scheduler.getTimeForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SUPER_PEER, 2))
        
        self.assertEquals(900, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1, 900))
        self.assertEquals(1, scheduler.countTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertEquals(900, scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        
        self.assertEquals(1800, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1, 1800))
        self.assertEquals(2, scheduler.countTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertEquals(1800, scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        
        self.assertEquals(2700, scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1, 2700))
        self.assertEquals(3, scheduler.countTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertEquals(2700, scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        self.assertTrue(scheduler.getTimesForPeer(IPeerToPeerNetwork.SIMPLE_PEER, 1))
        