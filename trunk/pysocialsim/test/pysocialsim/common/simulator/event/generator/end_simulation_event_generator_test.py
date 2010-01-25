"""
Defines the module with the unit test BeginSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.simulator.event.generator.end_simulation_event_generator import EndSimulationEventGenerator
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pymockobject.events import ReturnValue
import pymockobject
import unittest

class EndSimulationEventGeneratorTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(EndSimulationEventGenerator())
        generator = EndSimulationEventGenerator()
        self.assertFalse(generator.getSimulation())
    
    def testGenerateSimulationEvents(self):
        generator = EndSimulationEventGenerator()
        simulation = pymockobject.create(ISimulation)
        simulation.getSimulationTime.will(ReturnValue(10))
        self.assertEquals(simulation, generator.setSimulation(simulation))
        self.assertEquals(1, generator.generateSimulationEvents())