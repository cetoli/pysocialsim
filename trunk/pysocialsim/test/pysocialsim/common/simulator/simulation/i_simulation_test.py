"""
Defines the module with the unit test for ISimulation interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/08/2009
"""
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pysocialsim.common.simulator.i_simulator import ISimulator
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.simulator.event.i_simulation_event_generator import ISimulationEventGenerator
import pymockobject

import unittest

class ISimulationTest(unittest.TestCase):
    
    def testTryCreateInterfaceInstance(self):
        self.assertRaises(NotImplementedError, ISimulation)
        
    def testTryInvokeExecute(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().execute)
        
    def testTryInvokeGetSimulationTime(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().getSimulationTime)
        
    def testTryInvokeGetCurrentSimulation(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().getCurrentSimulationTime)
    
    def testTryInvokeSetCurrentSimulation(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().setCurrentSimulationTime, 2000)
    
    def testTryInvokeUnregisterSimulationEvent(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().unregisterSimulationEvent, "CONNECT")
    
    def testTryInvokeRegisterSimulationEvent(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().registerSimulationEvent, pymockobject.create(ISimulationEvent))
    
    def testTryInvokeCountSimulationEvents(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().countSimulationEvents, "CONNECT")
        
    def testTryInvokesSetSimulator(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().setSimulator, pymockobject.create(ISimulator))
    
    def testTryInvokeGetSimulator(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().getSimulator)
        
    def testTryInvokeCountSimulationEventQueues(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().countSimulationEventQueues)
        
    def testTryInvokeConfigure(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().configure)
        
    def testTryInvokeStop(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().stop)
        
    def testTryInvokeSetPeerToPeerNetwork(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().setPeerToPeerNetwork, pymockobject.create(IPeerToPeerNetwork))
    
    def testTryInvokeGetPeerToPeerNetwork(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().getPeerToPeerNetwork)
    
    def testTryInvokeSetSimulationTime(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().setSimulationTime, 10)
    
    def testTryInvokeAddSimulationEventGenerator(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().addSimulationEventGenerator, pymockobject.create(ISimulationEventGenerator))
    
    def testTryInvokeRemoveSimulationEventGenerator(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().removeSimulationEventGenerator, pymockobject.create(ISimulationEventGenerator))
        
    def testTryInvokeGetSimulationEventGenerators(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().getSimulationEventGenerators)
    
    def testTryInvokeCountSimulationEventGenerators(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().countSimulationEventGenerators)
        
    def testTryInvokeGetSimulationEvent(self):
        self.assertRaises(NotImplementedError, self.SimulationForTest().getSimulationEvent, "TEST")
    
    
    class SimulationForTest(ISimulation):
        
        def __init__(self):
            pass