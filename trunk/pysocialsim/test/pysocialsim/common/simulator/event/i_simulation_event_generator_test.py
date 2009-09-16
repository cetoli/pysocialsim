"""
Defines the module with the unit test of ISimulationEventGenerator interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 29/08/2009
"""
from pysocialsim.common.simulator.event.i_simulation_event_generator import ISimulationEventGenerator
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
import pymockobject

import unittest

class ISimulationEventGeneratorTest(unittest.TestCase):
    
    def testTryCreateInterfaceInstance(self):
        self.assertRaises(NotImplementedError, ISimulationEventGenerator)
        
    def testTryInvokeSetSimulation(self):
        self.assertRaises(NotImplementedError, self.SimulationEventGeneratorForTest().setSimulation, pymockobject.create(ISimulation))
    
    def testTryInvokeGetSimulation(self):
        self.assertRaises(NotImplementedError, self.SimulationEventGeneratorForTest().getSimulation)
        
    def testTryInvokeGenerateSimulationEvents(self):
        self.assertRaises(NotImplementedError, self.SimulationEventGeneratorForTest().generateSimulationEvents)
        
    class SimulationEventGeneratorForTest(ISimulationEventGenerator):
        
        def __init__(self):
            pass