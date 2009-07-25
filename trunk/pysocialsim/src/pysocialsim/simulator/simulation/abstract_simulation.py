from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.util.priority_queue import PriorityQueue
from threading import Semaphore

class AbstractSimulation(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, simulator, network):
        self.__simulator = simulator
        self.__network = network
        self.__network.setSimulation(self)
        self.__events = {}
        self.__simulationTime = 0
        self.__generatedEvents = 0
        self.__simulationCurrentTime = 0
        self.__totalContents = 0
    
    @public
    def getP2PNetwork(self):
        return self.__network
    
    @public
    def registerEvent(self, event):
        self.__events[event.getHandle()].enqueue(event, event.getPriority())
        return event
    
    @public
    def unregisterEvent(self, handle):
        return self.__events[handle].dequeue()
    
    @public
    def countEvents(self, handle):
        return self.__events[handle].size()
    
    @public
    def execute(self):
        handlers = self.getSimulator().getEventHandlers()
        for h in handlers:
            self.__events[h.getHandle()] = PriorityQueue()
        self.getSimulator().start(self)
    
    @public
    def stop(self):
        raise NotImplementedError()
    
    @public
    def setSimulationTime(self, simulationTime):
        if isinstance(simulationTime, bool):
            raise TypeError()
        if simulationTime <= 0:
            raise StandardError("Invalid simulation time.")
        
        self.__simulationTime = simulationTime
        return self.__simulationTime
    
    @public
    def getSimulationTime(self):
        return self.__simulationTime
   
    @public
    def setGeneratedEvents(self, number):
        sem = Semaphore()
        sem.acquire()
        self.__generatedEvents = number
        aux = self.__generatedEvents
        sem.release()
        return aux
    
    @public
    def getGeneratedEvents(self):
        sem = Semaphore()
        sem.acquire()
        aux = self.__generatedEvents
        sem.release()
        return aux
    
    def getSimulator(self):
        return self.__simulator
    
    @public
    def setSimulationCurrentTime(self, time):
        sem = Semaphore()
        sem.acquire()
        self.__simulationCurrentTime = time
        sem.release()
        return time
    
    @public
    def getSimulationCurrentTime(self):
        sem = Semaphore()
        sem.acquire()
        aux = self.__simulationCurrentTime
        sem.release()
        return aux

    @public
    def setNumberOfContents(self, contents):
        self.__totalContents = contents
        return self.__totalContents
    
    @public
    def getNumberOfContents(self):
        return self.__totalContents