from pysocialsim.simulator.abstract_simulator import AbstractSimulator

class DefaultSimulator(AbstractSimulator):
    
    def __init__(self, simulation):
        self.initialize(simulation)
        
    