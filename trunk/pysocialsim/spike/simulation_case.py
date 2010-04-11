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
from pysocialsim.common.simulator.event.generator.new_simple_peer_simulation_event_generator import NewSimplePeerSimulationEventGenerator
from pysocialsim.common.p2p.network.peer_to_peer_network import PeerToPeerNetwork
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.protocol.gnutella.gnutella_super_peer_protocol import GnutellaSuperPeerProtocol
from pysocialsim.common.p2p.topology.peer_to_peer_topology import PeerToPeerTopology
from pysocialsim.common.p2p.protocol.gnutella.gnutella_simple_peer_protocol import GnutellaSimplePeerProtocol
from pysocialsim.common.simulator.event.handler.start_opportunity_simulation_event_handler import StartOpportunitySimulationEventHandler
from pysocialsim.common.simulator.event.generator.start_opportunity_simulation_event_generator import StartOpportunitySimulationventGenerator
from pysocialsim.common.simulator.event.handler.end_opportunity_simulation_event_handler import EndOpportunitySimulationEventHandler
from pysocialsim.common.simulator.event.handler.push_opportunity_simulation_event_handler import PushOpportunitySimulationEventHandler
from pysocialsim.common.simulator.event.handler.new_simple_peer_simulation_event_handler import NewSimplePeerSimulationEventHandler
from pysocialsim.common.simulator.event.handler.simple_peer_leaving_simulation_event_handler import SimplePeerLeavingSimulationEventHandler
from pysocialsim.common.simulator.event.handler.simple_peer_joining_simulation_event_handler import SimplePeerJoiningSimulationEventHandler
from pysocialsim.common.p2p.peer.event.share_hardware_simulation_event_handler import ShareHardwareSimulationEventHandler
from pysocialsim.common.simulator.event.generator.simple_peer_leaving_simulation_event_generator import SimplePeerLeavingSimulationEventGenerator
from pysocialsim.common.simulator.event.generator.simple_peer_joining_simulation_event_generator import SimplePeerJoiningSimulationEventGenerator

class SimulationSpike(AbstractSimulation):
    
    def __init__(self):
        AbstractSimulation.initialize(self)


simulator = DefaultSimulator()
simulator.registerSimulationEventHandler(BeginSimulationEventHandler())
simulator.registerSimulationEventHandler(NewSuperPeerSimulationEventHandler())
simulator.registerSimulationEventHandler(NewSimplePeerSimulationEventHandler())
simulator.registerSimulationEventHandler(StartOpportunitySimulationEventHandler())
simulator.registerSimulationEventHandler(EndOpportunitySimulationEventHandler())
simulator.registerSimulationEventHandler(PushOpportunitySimulationEventHandler())
simulator.registerSimulationEventHandler(SimplePeerLeavingSimulationEventHandler())
simulator.registerSimulationEventHandler(SimplePeerJoiningSimulationEventHandler())
simulator.registerSimulationEventHandler(ShareHardwareSimulationEventHandler())
simulator.registerSimulationEventHandler(EndSimulationEventHandler())
simulation = SimulationSpike()

network = PeerToPeerNetwork(simulation)

network.setConnectionsBetweenSuperPeers(32)
network.setConnectionsBetweenSuperPeerAndSimplePeers(30)
network.setConnectionsBetweenSimplePeerAndSuperPeers(3)

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


protocol = GnutellaSuperPeerProtocol()
protocol.setPingHops(6)
protocol.setPongHops(6)
protocol.setPushHops(6)

topology = PeerToPeerTopology()
topology.setPeerToPeerNetwork(network)

protocol.setPeerToPeerTopology(topology)
network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SUPER_PEER, protocol)

protocol = GnutellaSimplePeerProtocol()
protocol.setPingHops(6)
protocol.setPongHops(6)
protocol.setPushHops(6)
protocol.setPeerToPeerTopology(topology)
network.registerPeerToPeerProtocol(IPeerToPeerNetwork.SIMPLE_PEER, protocol)


simulation.setPeerToPeerNetwork(network)
simulator.setSimulation(simulation)
simulation.setSimulationTime(432000)

simulation.addSimulationEventGenerator(BeginSimulationEventGenerator())
simulation.addSimulationEventGenerator(NewSuperPeerSimulationEventGenerator(5.5, 900, 100))
simulation.addSimulationEventGenerator(NewSimplePeerSimulationEventGenerator(5.5, 600, 1000))
simulation.addSimulationEventGenerator(SimplePeerLeavingSimulationEventGenerator(0.6566, 4.0763, 1000))
simulation.addSimulationEventGenerator(StartOpportunitySimulationventGenerator(0.5, 900, 1))
#for i in range(simulation.getSimulationTime()/10000):
#    simulation.addSimulationEventGenerator(SimplePeerJoiningSimulationEventGenerator(0.2, 1.0, 1000))
#    simulation.addSimulationEventGenerator(SimplePeerLeavingSimulationEventGenerator(0.6566, 4.0763, 1000))

simulation.addSimulationEventGenerator(EndSimulationEventGenerator())

simulator.start()
