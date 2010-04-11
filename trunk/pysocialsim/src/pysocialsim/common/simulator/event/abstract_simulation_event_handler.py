"""
Defines the module with the implementation of AbstractSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 25/08/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.simulator.event.i_simulation_event_handler import ISimulationEventHandler
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import requires, returns, pre_condition,\
    post_condition
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.event.i_simulation_event import ISimulationEvent
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class AbstractSimulationEventHandler(Object, ISimulationEventHandler):
    """
    Defines the base implementation of ISimulationEventHandler interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 25/08/2009
    """

    eventsLogFile = open("simulation.log", "a")

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, handle):
        """
        Initializes an AbstractSimulationEventHandler object.
        @param handle: a handle for handling
        @type handle: str
        @rtype: NoneType
        """
        requires(handle, str)
        self.__handle = handle
        self.__simulation = None
        self.__simulationEvent = None
    
    @public
    def clone(self):
        clone = self.__class__()
        clone.init(self.__simulation)
         
        return post_condition(returns(clone, ISimulationEventHandler), lambda obj: self.__eq__(obj))
    
    @public
    def init(self, simulation):
        requires(simulation, ISimulation)
        self.__simulation = simulation
    
    @public
    def getHandle(self):
        return returns(self.__handle, str)
    
    @public
    def getSimulation(self):
        return returns(self.__simulation, ISimulation)
    
    @public
    def getSimulationEvent(self):
        return returns(self.__simulationEvent, ISimulationEvent)
        
    handle = property(getHandle, None, None, None)
    """
    @type: str 
    """

    simulation = property(getSimulation, None, None, None)
    """
    @type: ISimulation
    """

    simulationEvent = property(getSimulationEvent, None, None, None)
    """
    @type: ISimulationEvent 
    """
    
    @public
    def handleSimulationEvent(self, simulationEvent):
        requires(simulationEvent, ISimulationEvent)
        pre_condition(simulationEvent, lambda simulationEvent: simulationEvent <> None)
        pre_condition(simulationEvent.getHandle(), lambda x: x == self.__handle)
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
        line = str(self.__simulationEvent.getPriority()) + " " + self.__simulationEvent.getHandle() + " " + self.__simulationEvent.getPeerId() + " " + str(superPeers) + " " + str(simplePeers)
        AbstractSimulationEventHandler.eventsLogFile.write(str(line)+"\n")
        #eventsLogFile.close()
        
        return self.__simulationEvent

    def __eq__(self, other):
        requires(other, ISimulationEventHandler)
        return other.getHandle() == self.__handle and other.getSimulation() == self.__simulation and other.getSimulationEvent() == self.__simulationEvent