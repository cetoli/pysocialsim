from pysocialsim.simulator.simulation.abstract_simulation import AbstractSimulation

class DefaultSimulation(AbstractSimulation):
    
    def __init__(self, network):
        self.initialize(network)