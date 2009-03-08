from pysocialsim.network.topology.unstructured_topology import UnstructuredTopology
from pysocialsim.simulator.simulation.default_simulation import DefaultSimulation
from pysocialsim.simulator.default_simulator import DefaultSimulator
from pysocialsim.network.network_builder_director import NetworkBuilderDirector
from pysocialsim.network.pure_network_builder import PureNetworkBuilder

if __name__ == '__main__':
    topology = UnstructuredTopology()
    builder = PureNetworkBuilder()
    director = NetworkBuilderDirector(builder)
    director.build(topology, peers=1000, min_permanence=21600, max_permanence=31104000, min_absence=3600, max_absence=2592000)
    network = builder.getNetwork()
    simulation = DefaultSimulation(network)
    simulator = DefaultSimulator(simulation)
    
    simulator.configure()
    simulator.execute()
    
    #simulator.stop()