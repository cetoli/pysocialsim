from pysocialsim.simulator.simulation.abstract_simulation import AbstractSimulation
from pysocialsim.base.decorator.return_type import return_type
from types import NoneType
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.i_simulator import ISimulator
from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork
from pysocialsim.base.decorator.public import public
from threading import Thread
from sets import ImmutableSet
from pysocialsim.simulator.simulation.stochastic.i_stochastic_model import IStochasticModel
import time

class AbstractStochasticSimulation(AbstractSimulation):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, simulator, network):
        AbstractSimulation.initialize(self, simulator, network)
        self.__stochasticModels = []
    
    @public
    def addStochasticModel(self, stochasticModel):
#        if stochasticModel in self.__stochasticModels:
#            raise StandardError()
        self.__stochasticModels.append(stochasticModel)
        return self.__stochasticModels[self.__stochasticModels.index(stochasticModel)]
    
    @public
    def removeStochasticModel(self, stochasticModel):
        return self.__stochasticModels.pop(self.__stochasticModels.index(stochasticModel))
    
    @public
    def countStochasticModels(self):
        return len(self.__stochasticModels)
    
    @public
    def execute(self):
        AbstractSimulation.execute(self)
        engine = AbstractStochasticSimulation.SimulationEngine(self)
        engine.start()
        
    @public
    def getStochasticModels(self):
        return ImmutableSet(self.__stochasticModels)
    
    class SimulationEngine(Thread):
        
        def __init__(self, simulation):
            Thread.__init__(self)
            self.__simulation = simulation
            
            
        def run(self):
            
                    for i in range(1, self.__simulation.getSimulationTime() + 1):
                        print i
                        self.__simulation.setSimulationCurrentTime(i)
                        for model in self.__simulation.getStochasticModels():
                            self.__simulation.setGeneratedEvents(model.generateEvents(self.__simulation) + self.__simulation.getGeneratedEvents())
                            time.sleep(0.02)