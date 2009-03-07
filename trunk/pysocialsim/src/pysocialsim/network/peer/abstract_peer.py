from pysocialsim.base.object import Object
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.base.decorator.require import require
from pysocialsim.network.network import Network
from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.simulation.event.event_generator import EventGenerator
from pysocialsim.simulator.simulation.simulation import Simulation
from types import NoneType

class AbstractPeer(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None.__class__)
    @require("id", int)
    @require("network", Network)
    @require("type", int)
    @require("permanence", int)
    @require("absence", int)
    def initialize(self, id, network, type, permanence, absence):
        self.__id = id
        self.__network = network
        self.__eventGenerators = []
        self.__isConnected = False
        self.__type = type
        self.__permanence = permanence
        self.__absence = absence
        #print self.__permanence/10000000.0, self.__absence/100000000.0
    
    @public
    @return_type(int)
    def getId(self):
        return self.__id
    
    @public
    @return_type(Network)
    def getNetwork(self):
        return self.__network
    
    @public
    @return_type(EventGenerator)
    @require("generator", EventGenerator)
    def addEventGenerator(self, generator):
        self.__eventGenerators.append(generator)
        return self.__eventGenerators[len(self.__eventGenerators) - 1]
    
    @public
    @return_type(EventGenerator)
    @require("generator", EventGenerator)
    def removeEventGenerator(self, generator):
        index = self.__eventGenerators.index(generator)
        return self.__eventGenerators.pop(index)
    
    @public
    @return_type(int)
    def countEventGenerators(self):
        return len(self.__eventGenerators)
    
    @public
    @return_type(int)
    @require("simulation", Simulation)
    def generateEvents(self, simulation):
        aux = 0
        for generator in self.__eventGenerators:
            aux += generator.generateEvents(simulation)
            
        return aux
    
    @public
    @return_type(bool)
    def isConnected(self):
        return self.__isConnected
    
    @public
    @return_type(NoneType)
    def connect(self):
        network = self.getNetwork()
        topology = network.getTopology()
        topology.connect(self)
        self.__isConnected = True
    
    @public
    @return_type(NoneType)
    def disconnect(self):
        network = self.getNetwork()
        topology = network.getTopology()
        topology.disconnect(self)
        self.__isConnected = False
    
    @public
    @return_type(int)
    def getType(self):
        return self.__type
    
    @public
    @return_type(int)
    def getPermanenceTime(self):
        return self.__permanence
    
    @public
    @return_type(int)
    def getAbsenceTime(self):
        return self.__absence