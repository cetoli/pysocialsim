"""
Defines the module with unit test for ISimulator interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.common.simulator.i_simulator import ISimulator
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pysocialsim.common.simulator.event.i_simulation_event_handler import ISimulationEventHandler
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
import pymockobject

import unittest

class ISimulatorTest(unittest.TestCase):
    
    def testTryInstantiateISimulatorInterface(self):
        self.assertRaises(NotImplementedError, ISimulator)
        
    def testTryInvokeHandleSimulationEvent(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().handleSimulationEvent, pymockobject.create(ISimulationEvent))
    
    def testTryInvokeRegisterSimulationEventHandler(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().registerSimulationEventHandler, pymockobject.create(ISimulationEventHandler))
    
    def testTryInvokeUnregisterSimulationEventHandler(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().unregisterSimulationEventHandler, "Teste")
    
    def testTryInvokeCountSimulationEventHandlers(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().countSimulationEventHandlers)
    
    def testTryInvokeGetSimulationEventHandlers(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().getSimulationEventHandlers)
        
    def testTryInvokeStart(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().start)
        
    def testTryInvokeStop(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().stop)
        
    def testTrySetSimulation(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().setSimulation, pymockobject.create(ISimulation))
        
    def testTryGetSimulation(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().getSimulation)
    
    def testTryInvokeGetScheduler(self):
        self.assertRaises(NotImplementedError, self.SimulatorForTest().getScheduler)    
        
    class SimulatorForTest(ISimulator):
        
        def __init__(self):
            pass