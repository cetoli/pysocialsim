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
import time

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
        self.__ttl = 0
        self.__simulationTime = 0
        self.__currentSimulationTime = 0
        self.__peerConnectionRate = 0
        
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
        if self.__events.size() == 50:
            self.simulate()
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
    
    @public
    def setTTL(self, ttl):
        self.__ttl = ttl
        
    @public
    def getTTL(self):
        return self.__ttl
    
    @public
    def setSimulationTime(self, simulationTime):
        self.__simulationTime = simulationTime
    
    @public
    def getSimulationTime(self):
        return self.__simulationTime
    
    @public
    def getCurrentSimulationTime(self):
        return self.__currentSimulationTime
    
    @public
    def setCurrentSimulationTime(self, currentSimulationTime):
        self.__currentSimulationTime = currentSimulationTime
    
    @public    
    def setPeerConnectionRate(self, peerConnectionRate):
        self.__peerConnectionRate = peerConnectionRate
    
    @public
    def getPeerConnectionRate(self):
        return self.__peerConnectionRate
    
    @public
    def getPeerConnectionFrequency(self):
        return self.__simulationTime / self.__peerConnectionRate
    
    class EventGenerationThread(Thread):
        
        def __init__(self, simulation):
            Thread.__init__(self)
            self.__simulation = simulation
            
        def run(self):
            for i in range(1, self.__simulation.getSimulationTime()):
                self.__simulation.setCurrentSimulationTime(i)
                self.__simulation.getNetwork().generateEvents(self.__simulation)
                print i
                
            
    class SimulationThread(Thread):
        
        def __init__(self, simulation, simulator):
            Thread.__init__(self)
            self.__simulation = simulation
            self.__simulator = simulator
            
        def run(self):
            while self.__simulation.getCurrentSimulationTime() < self.__simulation.getSimulationTime():
                if self.__simulation.countEvents() == 50:
                    for i in range(0, 50):
                        event = self.__simulation.unregisterEvent()
                        if not event:
                            break
                        self.__simulator.handleEvent(event)
