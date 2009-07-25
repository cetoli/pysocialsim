from pysocialsim.simulator.simulation.i_simulation import ISimulation
from pysocialsim.base.interface import Interface

class IStochasticSimulation(ISimulation):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def addStochasticModel(self, stochasticModel):
        raise NotImplementedError()
    
    def removeStochasticModel(self, stochasticModel):
        raise NotImplementedError()
    
    def countStochasticModels(self):
        raise NotImplementedError()
    
    def getStochasticModels(self):
        raise NotImplementedError()