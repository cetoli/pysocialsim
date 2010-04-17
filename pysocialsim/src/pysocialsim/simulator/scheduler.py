"""
Defines the module with the implementation of Scheduler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/09/2009
"""
from pysocialsim.error.invalid_value_error import InvalidValueError
from pysocialsim.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class Scheduler(object):
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
        self.__simulator = simulator
        self.__peerTimes = {IPeerToPeerNetwork.SUPER_PEER: {}, IPeerToPeerNetwork.SIMPLE_PEER: {}}
        self.__contextTimes = {}
    
    
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
        peers = self.__peerTimes[peerType]
        if not peers.has_key(peerId):
            peers[peerId] = []
        times = peers[peerId]
        times.append(time)
        return times[times.index(time)]
    
    
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
        peers = self.__peerTimes[peerType]
        times = peers[peerId]
        return times.pop(len(times) - 1)
        
    
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
        peers = self.__peerTimes[peerType]
        if not peers.has_key(peerId):
            raise InvalidValueError()
        times = peers[peerId]
        return times[len(times) - 1]
    
    
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
        peers = self.__peerTimes[peerType]
        if not peers.has_key(peerId):
            raise InvalidValueError()
        times = peers[peerId]
        return len(times)
    
    
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
        peers = self.__peerTimes[peerType]
        if not peers.has_key(peerId):
            raise InvalidValueError()
        times = peers[peerId]
        return times.__iter__()
    
    
    def registerTimeForContext(self, contextType, peerId, time):
        contexts = self.__contextTimes[contextType]
        if not contexts.has_key(peerId):
            contexts[peerId] = []
        times = contexts[peerId]
        times.append(time)
        return times[times.index(time)]
    
    
    def unregisterTimeForContext(self, contextType, peerId):
        contexts = self.__contextTimes[contextType]
        times = contexts[peerId]
        return times.pop(len(times) - 1)
    
    
    def getTimeForContext(self, contextType, peerId):
        contexts = self.__contextTimes[contextType]
        if not contexts.has_key(peerId):
            raise InvalidValueError()
        times = contexts[peerId]
        return times[len(times) - 1]
    
       
    def getTimesForContext(self, contextType, peerId): 
        contexts = self.__contextTimes[contextType]
        if not contexts.has_key(peerId):
            raise InvalidValueError()
        times = contexts[peerId]
        return times.__iter__()
    
    
    def countTimesForContext(self, contextType, peerId):
        contexts = self.__contextTimes[contextType]
        if not contexts.has_key(peerId):
            return 0
        times = contexts[peerId]
        return len(times)
     
    
    def getSimulator(self):
        """
        Gets the simulator object.
        @return: an ISimulator
        @rtype: ISimulator
        """
        return self.__simulator