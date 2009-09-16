"""
Defines the module with the unit test of AbstractSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 30/08/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.error.invalid_value_error import InvalidValueError
import pymockobject

import unittest

class AbstractSimulationEventGeneratorTest(unittest.TestCase):
    
    def testTryCreateAbstractClassInstance(self):
        self.assertRaises(NotImplementedError, AbstractSimulationEventGenerator)
        
    def testTryInvokeGenerateSimulationEvent(self):
        self.assertRaises(NotImplementedError, self.SimulationEventGeneratorForTest().generateSimulationEvents)
        
    def testSetAndGetSimulation(self):
        simulation = pymockobject.create(ISimulation)
        generator = self.SimulationEventGeneratorForTest()
        self.assertEquals(simulation, generator.setSimulation(simulation))
        self.assertEquals(simulation, generator.getSimulation())
        
        self.assertRaises(TypeError, generator.setSimulation, "")
        self.assertRaises(TypeError, generator.setSimulation, 1)
        self.assertRaises(TypeError, generator.setSimulation, 0.8)
        self.assertRaises(TypeError, generator.setSimulation, True)
        self.assertRaises(TypeError, generator.setSimulation, False)
        
        self.assertRaises(InvalidValueError, generator.setSimulation, None)
        
    class SimulationEventGeneratorForTest(AbstractSimulationEventGenerator):
        
        def __init__(self):
            pass
    