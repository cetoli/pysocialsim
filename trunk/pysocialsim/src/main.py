from pysocialsim.network.topology.unstructured_topology import UnstructuredTopology
from pysocialsim.simulator.simulation.default_simulation import DefaultSimulation
from pysocialsim.simulator.default_simulator import DefaultSimulator
from pysocialsim.network.network_builder_director import NetworkBuilderDirector
from pysocialsim.network.pure_network_builder import PureNetworkBuilder
from pysocialsim.simulator.dispatcher.default_dispatcher import DefaultDispatcher
from pysocialsim.network.peer.event.connection_event_handler import ConnectionEventHandler
from pysocialsim.network.peer.event.disconnection_event_handler import DisconnectionEventHandler
from pysocialsim.network.peer.event.send_event_handler import SendEventHandler
from pysocialsim.network.peer.event.receive_event_handler import ReceiveEventHandler
from pysocialsim.network.protocol.gnutella_protocol import GnutellaProtocol
from pysocialsim.network.peer.event.file_advertisement_event_handler import FileAdvertisementEventHandler
from pysocialsim.network.peer.event.content_necessity_event_handler import ContentNecessityEventHandler

if __name__ == '__main__':
    topology = UnstructuredTopology()
    
    builder = PureNetworkBuilder()
    
    director = NetworkBuilderDirector(builder)
    director.build(topology, GnutellaProtocol(), peers=100, min_permanence=60, max_permanence=1200, min_absence=10, max_absence=120)
    
    network = builder.getNetwork()
    network.setEvolutionRate(10)

    simulation = DefaultSimulation(network)
    simulation.setTTL(3)
    simulation.setSimulationTime(3600)
    
    simulation.setPeerConnectionRate(10)
    simulator = DefaultSimulator(simulation)
    simulator.setNumberOfFiles(5)
    
    dispatcher = DefaultDispatcher(simulator)
    dispatcher.registerEventHandler(ConnectionEventHandler(simulation))
    dispatcher.registerEventHandler(DisconnectionEventHandler(simulation))
    dispatcher.registerEventHandler(SendEventHandler(simulation))
    dispatcher.registerEventHandler(ReceiveEventHandler(simulation))
    dispatcher.registerEventHandler(FileAdvertisementEventHandler(simulation))
    dispatcher.registerEventHandler(ContentNecessityEventHandler(simulation))
    
    simulator.configure()
    simulator.execute()
    
    #time.sleep(5)
    
    #topology.show()
    #simulator.stop()