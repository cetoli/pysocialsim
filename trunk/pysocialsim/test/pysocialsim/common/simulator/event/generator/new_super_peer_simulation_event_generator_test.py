"""
Defines the module with the unit test of NewSimplePeerSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 16/09/2009
"""
from pysocialsim.common.simulator.event.generator.new_simple_peer_simulation_event_generator import NewSimplePeerSimulationEventGenerator
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.i_simulator import ISimulator
from pymockobject.events import ReturnValue
from pysocialsim.common.simulator.scheduler import Scheduler
import pymockobject

import unittest

class NewSimplePeerSimulationEventGeneratorTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(NewSimplePeerSimulationEventGenerator(5.5, 900, 10))
        generator = NewSimplePeerSimulationEventGenerator(5.5, 900, 10)
        self.assertFalse(generator.getSimulation())
    
    def testGenerateSimulationEvents(self):
        simulation = pymockobject.create(ISimulation)
        simulator = pymockobject.create(ISimulator)
        scheduler = Scheduler(pymockobject.create(ISimulator))
        simulator.getScheduler.will(ReturnValue(scheduler))
        
        simulation.getSimulator.will(ReturnValue(simulator))
        simulation.getSimulationTime.will(ReturnValue(86400))
        
        generator = NewSimplePeerSimulationEventGenerator(5.5, 900, 96)
        self.assertEquals(simulation, generator.setSimulation(simulation))
        self.assertEquals(96, generator.generateSimulationEvents())
        
        generator = NewSimplePeerSimulationEventGenerator(5.5, 900, 1000)
        self.assertEquals(simulation, generator.setSimulation(simulation))
        self.assertEquals(601, generator.generateSimulationEvents())