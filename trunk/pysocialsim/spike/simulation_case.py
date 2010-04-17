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
from pysocialsim.p2p.network.peer_to_peer_network import PeerToPeerNetwork

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
    network = PeerToPeerNetwork()
    network.setSimulation(simulation)
    network.setConnectionsBetweenSuperPeers(6)
    network.setConnectionsBetweenSuperPeerAndSimplePeers(30)
    network.setConnectionsBetweenSimplePeerAndSuperPeers(1)
    
    network.setLinkAvailability(50.0)
    
    network.setSuperPeerLink(1000000000)
    network.setSimplePeerLink(1000000)
    
    network.registerSizeOfMemory(4294967296)
    network.registerSizeOfMemory(3221225472)
    network.registerSizeOfMemory(2147483648)
    network.registerSizeOfMemory(1073741824)
    
    network.setMemoryAvailability(70.0)
    
    network.registerSizeOfDisk(343597383680)
    network.registerSizeOfDisk(268435456000)
    network.registerSizeOfDisk(171798691840)
    network.registerSizeOfDisk(128849018880)
    
    network.setDiskAvailability(70.0)
    
    network.registerProcessorClock(5000000000)
    network.registerProcessorClock(4000000000)
    network.registerProcessorClock(3000000000)
    network.registerProcessorClock(2000000000)
    
    network.setDiskAvailability(90.0)
    
    simulator.setSimulation(simulation)
    simulation.setSimulationTime(432000)
    
    simulation.addSimulationEventGenerator(BeginSimulationEventGenerator())
    simulation.addSimulationEventGenerator(NewSuperPeerSimulationEventGenerator(0.5, 250, 24))
    simulation.addSimulationEventGenerator(NewSimplePeerSimulationEventGenerator(0.5, 10, 700))
    
    simulator.start()

#masterNode = getProxyForURI("PYRONAME://network")
    
    