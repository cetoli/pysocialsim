"""
Defines the module with the implementation of AbstractSimulation class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/08/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.base.decorators import public
from pysocialsim.common.simulator.event.priority_queue import PriorityQueue
from pysocialsim.common.simulator.i_simulator import ISimulator
from pysocialsim.common.util.rotines import requires, returns, pre_condition
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pysocialsim.common.error.register_simulation_event_error import RegisterSimulationEventError
from pysocialsim.common.error.unregister_simulation_event_error import UnregisterSimulationEventError
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.simulator.event.i_simulation_event_generator import ISimulationEventGenerator
from threading import Thread, Semaphore
import time

class AbstractSimulation(Object, ISimulation):
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
   
    @public
    def addSimulationEventGenerator(self, simulationEventGenerator):
        requires(simulationEventGenerator, ISimulationEventGenerator)
        pre_condition(simulationEventGenerator, lambda x: x <> None)
        if simulationEventGenerator in self.__simulationEventGenerators:
            return None
        self.__simulationEventGenerators.append(simulationEventGenerator)
        simulationEventGenerator.setSimulation(self)
        return returns(self.__simulationEventGenerators[self.__simulationEventGenerators.index(simulationEventGenerator)], ISimulationEventGenerator)
    
    @public
    def registerSimplePeersByTime(self, time, simplePeers):
        self.__simplePeersByTime[time] = simplePeers
        
    @public
    def getSimplePeersByTime(self, time):
        return self.__simplePeersByTime[time]
    
    @public
    def registerSuperPeersByTime(self, time, superPeers):
        self.__superPeersByTime[time] = superPeers
        
    @public
    def getSuperPeersByTime(self, time):
        return self.__superPeersByTime[time]
    
    @public
    def removeSimulationEventGenerator(self, simulationEventGenerator):
        requires(simulationEventGenerator, ISimulationEventGenerator)
        pre_condition(simulationEventGenerator, lambda x: x <> None)
        if not simulationEventGenerator in self.__simulationEventGenerators:
            return None
        self.__simulationEventGenerators.remove(simulationEventGenerator)
        return simulationEventGenerator

    @public
    def getSimulationEventGenerators(self):
        return returns(self.__simulationEventGenerators, list)

    @public
    def countSimulationEventGenerators(self):
        return returns(len(self.__simulationEventGenerators), int)
    
    @public    
    def configure(self):
        handlers = self.__simulator.getSimulationEventHandlers()
        for hndlr in handlers:
            self.__queues[hndlr.getHandle()] = PriorityQueue()
        generatedEvents = 0
        for generator in self.__simulationEventGenerators:
            generatedEvents += generator.generateSimulationEvents()
        return generatedEvents
    
    @public    
    def getPeerToPeerNetwork(self):
        return returns(self.__peerToPeerNetwork, IPeerToPeerNetwork)
    
    @public
    def getSimulationEvent(self, handle):
        requires(handle, str)
        
        pre_condition(handle, lambda x: x <> "")
        pre_condition(handle, lambda x: x <> None)
        pre_condition(handle, lambda x: self.__queues.has_key(x))
        
        return returns(self.__queues[handle].getFirst(), ISimulationEvent)

    @public
    def setPeerToPeerNetwork(self, peerToPeerNetwork):
        requires(peerToPeerNetwork, IPeerToPeerNetwork)
        pre_condition(peerToPeerNetwork, lambda x: x <> None)
        self.__peerToPeerNetwork = peerToPeerNetwork
        self.__peerToPeerNetwork.setSimulation(self)
        return returns(self.__peerToPeerNetwork, IPeerToPeerNetwork)
    
    @public    
    def getSimulationTime(self):
        return returns(self.__simulationTime, int)
    
    @public
    def getEnqueuedTime(self, eventHandle):
        event = self.__queues[eventHandle].getFirst()
        return event.getPriority()

    @public
    def setSimulationTime(self, simulationTime):
        requires(simulationTime, int)
        pre_condition(simulationTime, lambda x: x > 0)
        self.__simulationTime = simulationTime
        return returns(self.__simulationTime, int)
    
    @public
    def getCurrentSimulationTime(self):
        semaphore = Semaphore()
        semaphore.acquire()
        time = self.__currentSimulationTime
        semaphore.release()
        return returns(time, int)

    @public
    def setCurrentSimulationTime(self, currentSimulationTime):
        requires(currentSimulationTime, int)
        pre_condition(currentSimulationTime, lambda x: x > 0)
        semaphore = Semaphore()
        semaphore.acquire()
        self.__currentSimulationTime = currentSimulationTime
        self.__simulator.notifyEventHandlingThreads()
        semaphore.release()
        return returns(currentSimulationTime, int)
    
    @public
    def getSimulator(self):
        return returns(self.__simulator, ISimulator)
    
    @public
    def setSimulator(self, simulator):
        requires(simulator, ISimulator)
        pre_condition(simulator, lambda x: x <> None)
        self.__simulator = simulator
        return returns(self.__simulator, ISimulator)
    
    @public
    def execute(self):
        self.SimulationEngine(self).start()
    
    @public
    def stop(self):
        self.__simulationTime = 0
    
    @public
    def countSimulationEventQueues(self):
        return len(self.__queues)

    @public
    def countSimulationEvents(self, handle):
        requires(handle, str)
        pre_condition(handle, lambda x: x <> "" or x <> None)
        return returns(self.__queues[handle].size(), int)

    @public
    def registerSimulationEvent(self, simulationEvent):
        requires(simulationEvent, ISimulationEvent)
        pre_condition(simulationEvent, lambda x: x <> None)
        if not self.__queues.has_key(simulationEvent.getHandle()):
            raise RegisterSimulationEventError(simulationEvent.getHandle()+" is invalid handle")
        return returns(self.__queues[simulationEvent.getHandle()].enqueue(simulationEvent, simulationEvent.getPriority()), ISimulationEvent)

    @public
    def unregisterSimulationEvent(self, handle):
        requires(handle, str)
        pre_condition(handle, lambda x: x <> None)
        pre_condition(handle, lambda x: x <> "")
        if not self.__queues.has_key(handle):
            raise UnregisterSimulationEventError(handle + "was not registered by simulator.")
        return returns(self.__queues[handle].dequeue(), ISimulationEvent)
    
    @public
    def increaseVersion(self):
        self.__version += 1
    
    @public
    def getVersion(self):
        return self.__version
    
    simulator = property(getSimulator, setSimulator, None, None)
    """
    @type: ISimulator 
    """
    simulationTime = property(getSimulationTime, setSimulationTime, None, None)
    """
    @type: int 
    """
    currentSimulationTime = property(getCurrentSimulationTime, setCurrentSimulationTime, None, None)
    """
    @type: int
    """
    peerToPeerNetwork = property(getPeerToPeerNetwork, setPeerToPeerNetwork, None, None)
    """
    @type: IPeerToPeerNetwork 
    """
    
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

                    if self.__simulation.getSimulationTime() == 0:
                        return 
                    print i
                    time.sleep(0.03)