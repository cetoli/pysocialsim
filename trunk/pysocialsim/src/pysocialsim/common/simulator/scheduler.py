"""
Defines the module with the implementation of Scheduler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/09/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.util.rotines import requires, pre_condition, returns
from pysocialsim.common.simulator.i_simulator import ISimulator
from pysocialsim.common.base.decorators import public
from pysocialsim.common.error.invalid_value_error import InvalidValueError
from pysocialsim.common.p2p.peer.context.i_context import IContext

class Scheduler(Object):
    """
    Defines the implementation of simulator scheduler.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 13/09/2009
    """

    def __init__(self, simulator):
        """
        Constructor of Scheduler
        @param simulator: an ISimulator
        @type simulator: ISimulator
        @rtype: NoneType
        """
        self.initialize(simulator)
    
    def initialize(self, simulator):
        """
        Initializes the schedule.
        @param simulator: an ISimulator
        @type simulator: ISimulator
        @rtype: NoneType
        """
        requires(simulator, ISimulator)
        
        pre_condition(simulator, lambda x: x <> None)
        
        self.__simulator = simulator
        self.__peerTimes = {IPeerToPeerNetwork.SUPER_PEER: {}, IPeerToPeerNetwork.SIMPLE_PEER: {}}
        self.__contextTimes = {IContext.INTEREST: {}}
    
    @public
    def registerTimeForPeer(self, peerType, peerId, time):
        """
        Registries a time of peer.
        @param peerType: the type of peer
        @type peerType: int
        @param peerId: the peer indentifier
        @type peerId: int
        @param time: the time for registering
        @type time: int
        @return: the registered time
        @rtype: int
        """
        requires(peerType, int)
        requires(peerId, str)
        requires(time, int)
        
        pre_condition(peerType, lambda x: x <> None)
        pre_condition(peerType, lambda x: self.__peerTimes.has_key(x))
        pre_condition(peerId, lambda x: x <> None)
        pre_condition(peerId, lambda x: x <> "")
        pre_condition(time, lambda x: x <> None)
        pre_condition(time, lambda x: x > 0)
        
        peers = self.__peerTimes[peerType]
        if not peers.has_key(peerId):
            peers[peerId] = []
        times = peers[peerId]
        times.append(time)
        return returns(times[times.index(time)], int)
    
    @public
    def unregisterTimeForPeer(self, peerType, peerId):
        """
        Unregistries a time of peer.
        @param peerType: the type of peer
        @type peerType: int
        @param peerId: the peer indentifier
        @type peerId: int
        @return: the registered time
        @rtype: int
        """
        requires(peerType, int)
        requires(peerId, str)
        
        pre_condition(peerType, lambda x: x <> None)
        pre_condition(peerType, lambda x: self.__peerTimes.has_key(x))
        pre_condition(peerId, lambda x: x <> None)
        pre_condition(peerId, lambda x: x > 0)
        
        pre_condition(peerType, lambda x: x <> None)
        pre_condition(peerType, lambda x: self.__peerTimes.has_key(x))
        pre_condition(peerId, lambda x: x <> None)
        pre_condition(peerId, lambda x: x > 0)

        peers = self.__peerTimes[peerType]
        pre_condition(peerId, lambda x: peers.has_key(x))
        times = peers[peerId]
        return returns(times.pop(len(times) - 1), int)
        
    @public
    def getTimeForPeer(self, peerType, peerId):
        """
        Gets a time of peer.
        @param peerType: the type of peer
        @type peerType: int
        @param peerId: the peer indentifier
        @type peerId: int
        @return: the registered time
        @rtype: int
        """
        requires(peerType, int)
        requires(peerId, str)
        
        pre_condition(peerType, lambda x: x <> None)
        pre_condition(peerType, lambda x: self.__peerTimes.has_key(x))
        pre_condition(peerId, lambda x: x <> None)
        pre_condition(peerId, lambda x: x > 0)

        peers = self.__peerTimes[peerType]
        if not peers.has_key(peerId):
            raise InvalidValueError()
        times = peers[peerId]
        return returns(times[len(times) - 1], int)
    
    @public
    def countTimesForPeer(self, peerType, peerId):
        """
        Counts the times of peer.
        @param peerType: the type of peer
        @type peerType: int
        @param peerId: the peer indentifier
        @type peerId: int
        @return: the registered time
        @rtype: int
        """
        requires(peerType, int)
        requires(peerId, str)
        
        pre_condition(peerType, lambda x: x <> None)
        pre_condition(peerType, lambda x: self.__peerTimes.has_key(x))
        pre_condition(peerId, lambda x: x <> None)
        pre_condition(peerId, lambda x: x > 0)
        
        peers = self.__peerTimes[peerType]
        if not peers.has_key(peerId):
            raise InvalidValueError()
        times = peers[peerId]
        return returns(len(times), int)
    
    @public
    def getTimesForPeer(self, peerType, peerId):
        """
        Gets the list of time.
        @param peerType: the type of peer
        @type peerType: int
        @param peerId: the peer indentifier
        @type peerId: int
        @return: the registered time
        @rtype: int
        """
        requires(peerType, int)
        requires(peerId, str)
        
        pre_condition(peerType, lambda x: x <> None)
        pre_condition(peerType, lambda x: self.__peerTimes.has_key(x))
        pre_condition(peerId, lambda x: x <> None)
        pre_condition(peerId, lambda x: x > 0)
        
        peers = self.__peerTimes[peerType]
        if not peers.has_key(peerId):
            raise InvalidValueError()
        times = peers[peerId]
        return times.__iter__()
    
    @public
    def registerTimeForContext(self, contextType, peerId, time):
        contexts = self.__contextTimes[contextType]
        if not contexts.has_key(peerId):
            contexts[peerId] = []
        times = contexts[peerId]
        times.append(time)
        return returns(times[times.index(time)], int)
    
    @public
    def unregisterTimeForContext(self, contextType, peerId):
        contexts = self.__contextTimes[contextType]
        pre_condition(peerId, lambda x: contexts.has_key(x))
        times = contexts[peerId]
        return returns(times.pop(len(times) - 1), int)
    
    @public
    def getTimeForContext(self, contextType, peerId):
        contexts = self.__contextTimes[contextType]
        if not contexts.has_key(peerId):
            raise InvalidValueError()
        times = contexts[peerId]
        return returns(times[len(times) - 1], int)
    
    @public   
    def getTimesForContext(self, contextType, peerId): 
        contexts = self.__contextTimes[contextType]
        if not contexts.has_key(peerId):
            raise InvalidValueError()
        times = contexts[peerId]
        return times.__iter__()
    
    @public
    def countTimesForContext(self, contextType, peerId):
        contexts = self.__contextTimes[contextType]
        if not contexts.has_key(peerId):
            return 0
        times = contexts[peerId]
        return len(times)
     
    @public
    def getSimulator(self):
        """
        Gets the simulator object.
        @return: an ISimulator
        @rtype: ISimulator
        """
        return returns(self.__simulator, ISimulator)