"""
Defines the module with the implementation of AbstractSimulation class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/08/2009
"""
from threading import Thread, Semaphore
from pysocialsim.simulator.simulation.i_simulation import ISimulation
from pysocialsim.simulator.event.priority_queue import PriorityQueue
from pysocialsim.error.register_simulation_event_error import RegisterSimulationEventError
from pysocialsim.error.unregister_simulation_event_error import UnregisterSimulationEventError
import time

class AbstractSimulation(ISimulation):
    """
    Define the basic implementation of ISimulation
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 27/08/2009
    """
    
    def __init__(self):
        raise NotImplementedError()

    def initialize(self):
        """
        Initializes the object.
        @rtype: NoneType
        """
        self.__simulator = None
        self.__simulationTime = 0
        self.__currentSimulationTime = 0
        self.__queues = {}
        self.__peerToPeerNetwork = None
        self.__simulationEventGenerators = []
        self.__simplePeersByTime = {}
        self.__superPeersByTime = {}
        self.__version = 0
   
    
    def addSimulationEventGenerator(self, simulationEventGenerator):
        if simulationEventGenerator in self.__simulationEventGenerators:
            return None
        self.__simulationEventGenerators.append(simulationEventGenerator)
        simulationEventGenerator.setSimulation(self)
        return self.__simulationEventGenerators[self.__simulationEventGenerators.index(simulationEventGenerator)]
    
    
    def registerSimplePeersByTime(self, time, simplePeers):
        self.__simplePeersByTime[time] = simplePeers
        
    
    def getSimplePeersByTime(self, time):
        return self.__simplePeersByTime[time]
    
    
    def registerSuperPeersByTime(self, time, superPeers):
        self.__superPeersByTime[time] = superPeers
        
    
    def getSuperPeersByTime(self, time):
        return self.__superPeersByTime[time]
    
    
    def removeSimulationEventGenerator(self, simulationEventGenerator):
        if not simulationEventGenerator in self.__simulationEventGenerators:
            return None
        self.__simulationEventGenerators.remove(simulationEventGenerator)
        return simulationEventGenerator

    
    def getSimulationEventGenerators(self):
        return self.__simulationEventGenerators

    
    def countSimulationEventGenerators(self):
        return len(self.__simulationEventGenerators)
    
        
    def configure(self):
        handlers = self.__simulator.getSimulationEventHandlers()
        for hndlr in handlers:
            self.__queues[hndlr.getHandle()] = PriorityQueue()
        generatedEvents = 0
        for generator in self.__simulationEventGenerators:
            generatedEvents += generator.generateSimulationEvents()
        return generatedEvents
    
        
    def getPeerToPeerNetwork(self):
        return self.__peerToPeerNetwork
    
    
    def getSimulationEvent(self, handle):
        return self.__queues[handle].getFirst()

    
    def setPeerToPeerNetwork(self, peerToPeerNetwork):
        self.__peerToPeerNetwork = peerToPeerNetwork
        self.__peerToPeerNetwork.setSimulation(self)
        return self.__peerToPeerNetwork
    
        
    def getSimulationTime(self):
        return self.__simulationTime
    
    
    def getEnqueuedTime(self, eventHandle):
        event = self.__queues[eventHandle].getFirst()
        return event.getPriority()

    
    def setSimulationTime(self, simulationTime):
        self.__simulationTime = simulationTime
        return self.__simulationTime
    
    
    def getCurrentSimulationTime(self):
        semaphore = Semaphore()
        semaphore.acquire()
        time = self.__currentSimulationTime
        semaphore.release()
        return time

    
    def setCurrentSimulationTime(self, currentSimulationTime):
        semaphore = Semaphore()
        semaphore.acquire()
        self.__currentSimulationTime = currentSimulationTime
        self.__simulator.notifyEventHandlingThreads()
        semaphore.release()
        return currentSimulationTime
    
    
    def getSimulator(self):
        return self.__simulator
    
    
    def setSimulator(self, simulator):
        self.__simulator = simulator
        return self.__simulator
    
    
    def execute(self):
        self.SimulationEngine(self).start()
    
    
    def stop(self):
        self.__simulationTime = 0
    
    
    def countSimulationEventQueues(self):
        return len(self.__queues)

    
    def countSimulationEvents(self, handle):
        return self.__queues[handle].size()

    
    def registerSimulationEvent(self, simulationEvent):
        if not self.__queues.has_key(simulationEvent.getHandle()):
            raise RegisterSimulationEventError(simulationEvent.getHandle()+" is invalid handle")
        return self.__queues[simulationEvent.getHandle()].enqueue(simulationEvent, simulationEvent.getPriority())

    
    def unregisterSimulationEvent(self, handle):
        if not self.__queues.has_key(handle):
            raise UnregisterSimulationEventError(handle + "was not registered by simulator.")
        return self.__queues[handle].dequeue()
    
    
    def increaseVersion(self):
        self.__version += 1
    
    
    def getVersion(self):
        return self.__version
    
        
    class SimulationEngine(Thread):
        
        def __init__(self, simulation):
            Thread.__init__(self)
            self.__simulation = simulation
            
            
        def run(self):
            if self.__simulation.getSimulationTime() > 0:
                for i in range(1, self.__simulation.getSimulationTime() + 1):
                    
                    self.__simulation.setCurrentSimulationTime(i)
                    if i % 1000 == 0:
                        self.__simulation.increaseVersion()
                        time.sleep(60)

                    if self.__simulation.getSimulationTime() == 0:
                        return 
                    print i
                    time.sleep(0.06)