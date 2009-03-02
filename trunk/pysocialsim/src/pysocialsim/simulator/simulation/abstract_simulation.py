from pysocialsim.base.object import Object
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.network.network import Network
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.simulator import Simulator
from pysocialsim.util.priority_queue import PriorityQueue
from pysocialsim.simulator.simulation.event.event import Event

class AbstractSimulation(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None.__class__)
    @require("network", Network)
    def initialize(self, network):
        self.__network = network
        self.__simulator = None
        self.__events = PriorityQueue()
        
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
    
    @public
    @return_type(Event)
    @require("event", Event)
    def registerEvent(self, event):
        self.__events.enqueue(event, event.getPriority())
        return event
    
    @public
    @return_type(int)
    def countEvents(self):
        return self.__events.size()
    
    @public
    @return_type(Event)
    def unregisterEvent(self):
        return self.__events.dequeue()