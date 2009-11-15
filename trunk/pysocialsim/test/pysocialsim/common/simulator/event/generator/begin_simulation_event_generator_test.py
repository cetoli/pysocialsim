"""
Defines the module with the unit test BeginSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.simulator.event.generator.begin_simulation_event_generator import BeginSimulationEventGenerator
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
import pymockobject

import unittest

class BeginSimulationEventGeneratorTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(BeginSimulationEventGenerator())
        generator = BeginSimulationEventGenerator()
        self.assertFalse(generator.getSimulation())
    
    def testGenerateSimulationEvents(self):
        generator = BeginSimulationEventGenerator()
        simulation = pymockobject.create(ISimulation)
        self.assertEquals(simulation, generator.setSimulation(simulation))
        self.assertEquals(1, generator.generateSimulationEvents())