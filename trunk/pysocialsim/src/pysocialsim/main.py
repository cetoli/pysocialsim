from pysocialsim.simulator.default_simulator import DefaultSimulator
from pysocialsim.p2p.topology.default_p2p_topology import DefaultP2PTopology
from pysocialsim.p2p.network.default_p2p_network_builder import DefaultP2PNetworkBuilder
from pysocialsim.p2p.network.p2p_network_builder_director import P2PNetworkBuilderDirector
from pysocialsim.simulator.dispatcher.peer_connection_event_handler import PeerConnectionEventHandler
from pysocialsim.simulator.dispatcher.peer_disconnection_event_handler import PeerDisconnectionEventHandler
from pysocialsim.simulator.dispatcher.content_sharing_event_handler import ContentSharingEventHandler
from pysocialsim.simulator.simulation.stochastic.peer_connection_process_model import PeerConnectionProcessModel
from pysocialsim.simulator.simulation.stochastic.content_sharing_process_model import ContentSharingProcessModel
from pysocialsim.simulator.simulation.stochastic.peer_interest_process_model import PeerInterestProcessModel
from pysocialsim.simulator.dispatcher.interest_specification_event_handler import InterestSpecificationEventHandler

if __name__ == '__main__':
    builder = DefaultP2PNetworkBuilder()
    director = P2PNetworkBuilderDirector(builder)
    director.build("network.yaml", DefaultP2PTopology())
    network = builder.getP2PNetwork()
    simulator = DefaultSimulator()
    
    simulation = simulator.createStochasticSimulation(network)
    simulator.registerEventHandler(PeerConnectionEventHandler(simulation))
    simulator.registerEventHandler(PeerDisconnectionEventHandler(simulation))
    simulator.registerEventHandler(ContentSharingEventHandler(simulation))
    simulator.registerEventHandler(InterestSpecificationEventHandler(simulation))
    
    simulation.setSimulationTime(2592000)
    
    model = PeerConnectionProcessModel(1, 846)
    simulation.addStochasticModel(model)
    
    model = ContentSharingProcessModel(1, 30000, 3600)
    simulation.addStochasticModel(model)
    
    model = PeerInterestProcessModel(1, 60000, 1900)
    simulation.addStochasticModel(model)
    
    simulation.execute()