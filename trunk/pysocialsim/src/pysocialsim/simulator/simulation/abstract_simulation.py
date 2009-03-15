from pysocialsim.base.object import Object
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.network.network import Network
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.simulator import Simulator
from pysocialsim.util.priority_queue import PriorityQueue
from pysocialsim.simulator.simulation.event.event import Event
from types import NoneType
from threading import Thread

class AbstractSimulation(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None.__class__)
    @require("network", Network)
    def initialize(self, network):
        self.__network = network
        self.__network.setSimulation(self)
        self.__simulator = None
        self.__events = PriorityQueue()
        self.__numberOfFiles = 0
        
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
    
    @public
    @return_type(NoneType)
    def generateEvents(self):
        AbstractSimulation.EventGenerationThread(self).start()
    
    @public
    @return_type(NoneType)
    def simulate(self):
        AbstractSimulation.SimulationThread(self, self.__simulator).start()
    
    @public
    @return_type(NoneType)        
    def stop(self):
        self.__network.stop()
        
    @public
    def setNumberOfFiles(self, files):
        self.__numberOfFiles = files
        return self.__numberOfFiles
    
    @public
    def getNumberOfFiles(self):
        return self.__numberOfFiles
    
    @public
    def generateFiles(self):
        raise NotImplementedError()
    
    class EventGenerationThread(Thread):
        
        def __init__(self, simulation):
            Thread.__init__(self)
            self.__simulation = simulation
            
        def run(self):
            while True:
                self.__simulation.getNetwork().generateEvents(self.__simulation)
            
    class SimulationThread(Thread):
        
        def __init__(self, simulation, simulator):
            Thread.__init__(self)
            self.__simulation = simulation
            self.__simulator = simulator
            
        def run(self):
            while True:
                if self.__simulation.countEvents() > 0:
                    for id in range(self.__simulation.countEvents()):
                        event = self.__simulation.unregisterEvent()
                        self.__simulator.handleEvent(event)