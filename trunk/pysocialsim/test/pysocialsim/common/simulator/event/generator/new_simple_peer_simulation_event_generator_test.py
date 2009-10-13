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
from pysocialsim.common.simulator.event.generator.new_super_peer_simulation_event_generator import NewSuperPeerSimulationEventGenerator
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
import pymockobject

import unittest

class NewSuperPeerSimulationEventGeneratorTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(NewSuperPeerSimulationEventGenerator(2.0, 9600, 9))
        generator = NewSimplePeerSimulationEventGenerator(2.0, 9600, 9)
        self.assertFalse(generator.getSimulation())
    
    def testGenerateSimulationEvents(self):
        simulation = pymockobject.create(ISimulation)
        simulation.getPeerToPeerNetwork.will(ReturnValue(pymockobject.create(IPeerToPeerNetwork)))
        simulator = pymockobject.create(ISimulator)
        scheduler = Scheduler(pymockobject.create(ISimulator))
        simulator.getScheduler.will(ReturnValue(scheduler))
        
        simulation.getSimulator.will(ReturnValue(simulator))
        simulation.getSimulationTime.will(ReturnValue(86400))
        
        generator = NewSuperPeerSimulationEventGenerator(2.0, 9600, 9)
        self.assertEquals(simulation, generator.setSimulation(simulation))
        self.assertEquals(9, generator.generateSimulationEvents())
        
        generator = NewSuperPeerSimulationEventGenerator(2.0, 9600, 90)
        self.assertEquals(simulation, generator.setSimulation(simulation))
        self.assertEquals(10, generator.generateSimulationEvents())
