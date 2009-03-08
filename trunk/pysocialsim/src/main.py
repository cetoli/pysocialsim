from pysocialsim.network.topology.unstructured_topology import UnstructuredTopology
from pysocialsim.simulator.simulation.default_simulation import DefaultSimulation
from pysocialsim.simulator.default_simulator import DefaultSimulator
from pysocialsim.network.network_builder_director import NetworkBuilderDirector
from pysocialsim.network.pure_network_builder import PureNetworkBuilder
from pysocialsim.simulator.dispatcher.default_dispatcher import DefaultDispatcher
from pysocialsim.network.peer.event.connection_event_handler import ConnectionEventHandler
from pysocialsim.network.peer.event.disconnection_event_handler import DisconnectionEventHandler

if __name__ == '__main__':
    topology = UnstructuredTopology()
    builder = PureNetworkBuilder()
    director = NetworkBuilderDirector(builder)
    director.build(topology, peers=100, min_permanence=21600, max_permanence=31104000, min_absence=3600, max_absence=2592000)
    network = builder.getNetwork()
    simulation = DefaultSimulation(network)
    simulator = DefaultSimulator(simulation)
    dispatcher = DefaultDispatcher(simulator)
    
    dispatcher.registerEventHandler(ConnectionEventHandler(simulation))
    dispatcher.registerEventHandler(DisconnectionEventHandler(simulation))
    
    simulator.configure()
    simulator.execute()
    
    #simulator.stop()