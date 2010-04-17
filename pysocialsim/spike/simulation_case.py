'''
Created on 17/04/2010

@author: Fabricio
'''
from pysocialsim.simulator.default_simulator import DefaultSimulator
from pysocialsim.simulator.event.handler.begin_simulation_event_handler import BeginSimulationEventHandler
from pysocialsim.simulator.event.handler.new_super_peer_simulation_event_handler import NewSuperPeerSimulationEventHandler
from pysocialsim.simulator.event.handler.new_simple_peer_simulation_event_handler import NewSimplePeerSimulationEventHandler
from pysocialsim.simulator.event.handler.start_opportunity_simulation_event_handler import StartOpportunitySimulationEventHandler
from pysocialsim.simulator.event.handler.end_opportunity_simulation_event_handler import EndOpportunitySimulationEventHandler
from pysocialsim.simulator.event.handler.push_opportunity_simulation_event_handler import PushOpportunitySimulationEventHandler
from pysocialsim.simulator.event.handler.simple_peer_leaving_simulation_event_handler import SimplePeerLeavingSimulationEventHandler
from pysocialsim.simulator.event.handler.simple_peer_joining_simulation_event_handler import SimplePeerJoiningSimulationEventHandler
from pysocialsim.simulator.event.handler.end_simulation_event_handler import EndSimulationEventHandler
from pysocialsim.simulator.simulation.concrete_simulation import ConcreteSimulation
from pysocialsim.simulator.event.generator.begin_simulation_event_generator import BeginSimulationEventGenerator
from pysocialsim.simulator.event.generator.new_super_peer_simulation_event_generator import NewSuperPeerSimulationEventGenerator
from pysocialsim.simulator.event.generator.new_simple_peer_simulation_event_generator import NewSimplePeerSimulationEventGenerator
from Pyro.core import getProxyForURI

if __name__ == '__main__':
    simulator = DefaultSimulator()
    simulator.registerSimulationEventHandler(BeginSimulationEventHandler())
    simulator.registerSimulationEventHandler(NewSuperPeerSimulationEventHandler())
    simulator.registerSimulationEventHandler(NewSimplePeerSimulationEventHandler())
    simulator.registerSimulationEventHandler(StartOpportunitySimulationEventHandler())
    simulator.registerSimulationEventHandler(EndOpportunitySimulationEventHandler())
    simulator.registerSimulationEventHandler(PushOpportunitySimulationEventHandler())
    simulator.registerSimulationEventHandler(SimplePeerLeavingSimulationEventHandler())
    simulator.registerSimulationEventHandler(SimplePeerJoiningSimulationEventHandler())
    #simulator.registerSimulationEventHandler(ShareHardwareSimulationEventHandler())
    simulator.registerSimulationEventHandler(EndSimulationEventHandler())
    
    simulation = ConcreteSimulation()
    simulator.setSimulation(simulation)
    simulation.setSimulationTime(432000)
    
    simulation.addSimulationEventGenerator(BeginSimulationEventGenerator())
simulation.addSimulationEventGenerator(NewSuperPeerSimulationEventGenerator(0.5, 250, 24))
simulation.addSimulationEventGenerator(NewSimplePeerSimulationEventGenerator(0.5, 10, 700))

#simulator.start()

masterNode = getProxyForURI("PYRONAME://network")
    
    