"""
Defines the module with the unit test of SimplePeerJoiningSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 16/09/2009
"""
from pysocialsim.common.simulator.event.generator.simple_peer_joining_simulation_event_generator import SimplePeerJoiningSimulationEventGenerator
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.i_simulator import ISimulator
from pysocialsim.common.simulator.scheduler import Scheduler
from pymockobject.events import ReturnValue
from pysocialsim.common.simulator.event.generator.simple_peer_leaving_simulation_event_generator import SimplePeerLeavingSimulationEventGenerator
import pymockobject

import unittest

class SimplePeerLeavingSimulationEventGeneratorTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(SimplePeerLeavingSimulationEventGenerator(1.8, 3600.0, 96))
        generator = SimplePeerLeavingSimulationEventGenerator(1.8, 3600.0, 96)
        self.assertFalse(generator.getSimulation())
        
    def testGenerateSimulationEvents(self):
        simulation = pymockobject.create(ISimulation)
        simulator = pymockobject.create(ISimulator)
        scheduler = pymockobject.create(Scheduler)
        scheduler.getTimeForPeer.will(ReturnValue(900))
        simulator.getScheduler.will(ReturnValue(scheduler))
        
        simulation.getSimulator.will(ReturnValue(simulator))
        simulation.getSimulationTime.will(ReturnValue(86400))
        
        generator = SimplePeerLeavingSimulationEventGenerator(1.8, 3600.0, 96)
        self.assertEquals(simulation, generator.setSimulation(simulation))
        self.assertEquals(96, generator.generateSimulationEvents())