"""
Defines the module with the implementation of AbstractSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 25/08/2009
"""
from pysocialsim.simulator.event.i_simulation_event_handler import ISimulationEventHandler
from pysocialsim.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from Pyro.core import getProxyForURI

class AbstractSimulationEventHandler(ISimulationEventHandler):
    """
    Defines the base implementation of ISimulationEventHandler interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 25/08/2009
    """

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, handle):
        """
        Initializes an AbstractSimulationEventHandler object.
        @param handle: a handle for handling
        @type handle: str
        @rtype: NoneType
        """
        self.__handle = handle
        self.__simulation = None
        self.__simulationEvent = None
    
    
    def clone(self):
        clone = self.__class__()
        clone.init(self.__simulation)
         
        return clone
    
    
    def init(self, simulation):
        self.__simulation = simulation
    
    
    def getHandle(self):
        return self.__handle
    
    
    def getSimulation(self):
        return self.__simulation
    
    
    def getSimulationEvent(self):
        return self.__simulationEvent
        
    def handleSimulationEvent(self, simulationEvent):
        self.__simulationEvent = simulationEvent
        return self.execute()
        
    def execute(self):
        """
        Template method to implement specific algorithm for handling a given simulation event.
        This method must be implemented in AbstractSimulationEventHandler subclasses.
        @note: The visibility of this operation is protected.
        @rtype: NoneType
        """
        self.__simulationEvent.handled()
        network = self.__simulation.getPeerToPeerNetwork()
        superPeers = network.countConnectedPeers(IPeerToPeerNetwork.SUPER_PEER)
        simplePeers = network.countConnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER)
        eventsLogFile = open("simulation.log", "a")
        line = str(self.__simulationEvent.getPriority()) + " " + self.__simulationEvent.getHandle() + " " + self.__simulationEvent.getPeerId() + " " + str(superPeers) + " " + str(simplePeers)
        eventsLogFile.write(str(line)+"\n")
        eventsLogFile.close()
        
        return self.__simulationEvent

    def __eq__(self, other):
        return other.getHandle() == self.__handle and other.getSimulation() == self.__simulation and other.getSimulationEvent() == self.__simulationEvent