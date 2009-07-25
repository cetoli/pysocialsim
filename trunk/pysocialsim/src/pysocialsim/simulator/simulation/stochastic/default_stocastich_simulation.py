from pysocialsim.simulator.simulation.stochastic.abstract_stochastic_simulation import AbstractStochasticSimulation

class DefaultStochasticSimulation(AbstractStochasticSimulation):
    
    def __init__(self, simulator, network):
        self.initialize(simulator, network)