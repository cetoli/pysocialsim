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
from pysocialsim.common.simulator.event.generator.simple_peer_leaving_simulation_event_generator import SimplePeerLeavingSimulationEventGenerator
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
from pysocialsim.common.simulator.event.generator.simple_peer_joining_simulation_event_generator import SimplePeerJoiningSimulationEventGenerator
from pysocialsim.common.simulator.event.handler.simple_peer_joining_simulation_event_handler import SimplePeerJoiningSimulationEventHandler

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
simulator.registerSimulationEventHandler(EndSimulationEventHandler())
simulation = SimulationSpike()
network = PeerToPeerNetwork(simulation)

network.setConnectionsBetweenSuperPeers(6)
network.setConnectionsBetweenSuperPeerAndSimplePeers(30)
network.setConnectionsBetweenSimplePeerAndSuperPeers(1)

network.setLinkAvailability(50.0)

network.setSuperPeerLink(1000000000)

protocol = GnutellaSuperPeerProtocol()
protocol.setPingHops(6)
protocol.setPongHops(6)

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
simulation.setSimulationTime(2592000)

simulation.addSimulationEventGenerator(BeginSimulationEventGenerator())
simulation.addSimulationEventGenerator(NewSuperPeerSimulationEventGenerator(5.5, 3000, 10))
simulation.addSimulationEventGenerator(NewSimplePeerSimulationEventGenerator(5.5, 500, 100))
simulation.addSimulationEventGenerator(SimplePeerLeavingSimulationEventGenerator(1.5618, 6.0013, 100))
simulation.addSimulationEventGenerator(StartOpportunitySimulationventGenerator(0.5, 600, 300))

simulation.addSimulationEventGenerator(SimplePeerJoiningSimulationEventGenerator(1.8, 900.0, 100))
simulation.addSimulationEventGenerator(SimplePeerLeavingSimulationEventGenerator(1.5618, 6.0013, 100))

simulation.addSimulationEventGenerator(EndSimulationEventGenerator())

simulator.start()
