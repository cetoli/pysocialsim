from pysocialsim.base.object import Object
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.network.network import Network
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.simulator import Simulator

class AbstractSimulation(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None.__class__)
    @require("network", Network)
    def initialize(self, network):
        self.__network = network
        self.__simulator = None
        
    @public
    @return_type(Network)
    def getNetwork(self):
        return self.__network
    
    @public
    @return_type(Simulator)
    @require("simulator", Simulator)
    def setSimulator(self, simulator):
        self.__simulator = simulator
        return self.__simulator