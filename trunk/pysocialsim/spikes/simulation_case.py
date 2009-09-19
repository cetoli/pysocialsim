"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 07/09/2009
"""
from pysocialsim.common.simulator.default_simulator import DefaultSimulator
from pysocialsim.common.simulator.simulation.abstract_simulation import AbstractSimulation
from pysocialsim.common.simulator.event.handler.begin_simulation_event_handler import BeginSimulationEventHandler
from pysocialsim.common.simulator.event.generator.begin_simulation_event_generator import BeginSimulationEventGenerator
from pysocialsim.common.simulator.event.handler.end_simulation_event_handler import EndSimulationEventHandler
from pysocialsim.common.simulator.event.generator.end_simulation_event_generator import EndSimulationEventGenerator
from pysocialsim.common.simulator.event.generator.new_super_peer_simulation_event_generator import NewSuperPeerSimulationEventGenerator
from pysocialsim.common.simulator.event.handler.new_super_peer_simulation_event_handler import NewSuperPeerSimulationEventHandler
from pysocialsim.common.simulator.event.handler.new_simple_peer_simulation_event_handler import NewSimplePeerSimulationEventHandler
from pysocialsim.common.simulator.event.generator.new_simple_peer_simulation_event_generator import NewSimplePeerSimulationEventGenerator
from pysocialsim.common.simulator.event.generator.simple_peer_leaving_simulation_event_generator import SimplePeerLeavingSimulationEventGenerator
from pysocialsim.common.simulator.event.generator.simple_peer_joining_simulation_event_generator import SimplePeerJoiningSimulationEventGenerator

class SimulationSpike(AbstractSimulation):
    
    def __init__(self):
        AbstractSimulation.initialize(self)


simulator = DefaultSimulator()
simulator.registerSimulationEventHandler(BeginSimulationEventHandler())
simulator.registerSimulationEventHandler(NewSuperPeerSimulationEventHandler())
simulator.registerSimulationEventHandler(NewSimplePeerSimulationEventHandler())
simulator.registerSimulationEventHandler(EndSimulationEventHandler())
simulation = SimulationSpike()
simulator.setSimulation(simulation)
simulation.setSimulationTime(86400)
simulation.addSimulationEventGenerator(BeginSimulationEventGenerator())
simulation.addSimulationEventGenerator(NewSuperPeerSimulationEventGenerator(2.0, 9600, 9))
simulation.addSimulationEventGenerator(NewSimplePeerSimulationEventGenerator(5.5, 900, 96))
simulation.addSimulationEventGenerator(SimplePeerLeavingSimulationEventGenerator(3.9867, 13.7007, 96))
simulation.addSimulationEventGenerator(SimplePeerJoiningSimulationEventGenerator(1.8, 3600.0, 96))
simulation.addSimulationEventGenerator(EndSimulationEventGenerator())
#simulation.configure()
simulator.start()