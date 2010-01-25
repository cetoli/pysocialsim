"""
Defines the module with the implementation of PeerToPeerNetwork class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.util.rotines import requires, pre_condition, returns
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.peer.i_peer import IPeer
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
from threading import Semaphore

class AbstractPeerToPeerNetwork(Object, IPeerToPeerNetwork):
    """
    Defines the abstract implementation of IPeerToPeerNetwork interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/10/2009
    """

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, simulation):
        requires(simulation, ISimulation)
        pre_condition(simulation, lambda x: x <> None)
        
        self.__simulation = simulation
        self.__peers = {IPeerToPeerNetwork.SUPER_PEER: {}, IPeerToPeerNetwork.SIMPLE_PEER: {}}
        self.__connectionsBetweenSuperPeers = 0
        self.__peerToPeerProtocols = {}
        self.__connectionsBetweenSuperPeerAndSimplePeers = 0
        self.__connectionsBetweenSimplePeerAndSuperPeers = 0
        self.__linkAvailability = 0
        self.__superPeerLink = 0
    
    @public
    def getSimulation(self):
        return returns(self.__simulation, ISimulation)
    
    @public
    def setSimulation(self, simulation):
        requires(simulation, ISimulation)
        pre_condition(simulation, lambda x: x <> None)
        self.__simulation = simulation
        return returns(self.__simulation, ISimulation)

    @public
    def getConnectionsBetweenSuperPeers(self):
        return returns(self.__connectionsBetweenSuperPeers, int)

    @public
    def setConnectionsBetweenSuperPeers(self, connectionsBetweenSuperPeers):
        requires(connectionsBetweenSuperPeers, int)
        
        pre_condition(connectionsBetweenSuperPeers, lambda x: x > 0)
        pre_condition(connectionsBetweenSuperPeers, lambda x: x <> None)
        
        self.__connectionsBetweenSuperPeers = connectionsBetweenSuperPeers
        return returns(self.__connectionsBetweenSuperPeers, int)
    
    @public
    def addPeer(self, peerType, peer):
        requires(peerType, int)
        requires(peer, IPeer)
        
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        pre_condition(peerType, lambda x: self.__peers.has_key(x))
        
        pre_condition(peer, lambda x: x <> None)
        
        if self.__peers[peerType].has_key(peer.getId()):
            return False
        
        self.__peers[peerType][peer.getId()] = peer
        return self.__peers[peerType].has_key(peer.getId())

    @public
    def removePeer(self, peerType, peerId):
        requires(peerType, int)
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        
        return IPeerToPeerNetwork.removePeer(self, peerType, peerId)

    @public
    def getPeer(self, peerType, peerId):
        requires(peerType, int)
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        
        return self.__peers[peerType][peerId]
    @public
    def getPeers(self, peerType):
        requires(peerType, int)
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        
        return self.__peers[peerType].itervalues()

    @public
    def countPeers(self, peerType):
        requires(peerType, int)
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        
        return len(self.__peers[peerType])

    @public
    def getConnectedPeers(self, peerType):
        requires(peerType, int)
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        
        sem = Semaphore()
        sem.acquire()
        peers = []
        
        for peer in self.__peers[peerType].values():
            if peer.isJoined():
                peers.append(peer)
                
        sem.release()
        return peers

    @public
    def getDisconnectedPeers(self, peerType):
        requires(peerType, int)
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        
        peers = []
        
        for peer in self.__peers[peerType].values():
            if peer.isLeaved() == True:
                peers.append(peer)
        
        return peers.__iter__()
    
    @public
    def registerPeerToPeerProtocol(self, peerType, peerToPeerProtocol):
        requires(peerType, int)
        requires(peerToPeerProtocol, IPeerToPeerProtocol)
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        pre_condition(peerType, lambda x: not self.__peerToPeerProtocols.has_key(x))
        pre_condition(peerToPeerProtocol, lambda x: x <> None)
        
        self.__peerToPeerProtocols[peerType] = peerToPeerProtocol
        return self.__peerToPeerProtocols.has_key(peerType)

    @public
    def unregisterPeerToPeerProtocol(self, peerType):
        requires(peerType, int)
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        pre_condition(peerType, lambda x: self.__peerToPeerProtocols.has_key(x))

        del self.__peerToPeerProtocols[peerType]
        
        return returns(not self.__peerToPeerProtocols.has_key(peerType), bool)

    @public
    def getPeerToPeerProtocol(self, peerType):
        requires(peerType, int)
        pre_condition(peerType, lambda x: x == IPeerToPeerNetwork.SUPER_PEER or x == IPeerToPeerNetwork.SIMPLE_PEER)
        pre_condition(peerType, lambda x: self.__peerToPeerProtocols.has_key(x))

        return returns(self.__peerToPeerProtocols[peerType], IPeerToPeerProtocol)
    
    @public
    def hasPeer(self, peer):
        requires(peer, IPeer)
        pre_condition(peer, lambda x: x <> None)
        
        return self.__peers[peer.getType()].has_key(peer.getId())
    
    @public
    def getConnectionsBetweenSuperPeerAndSimplePeers(self):
        return self.__connectionsBetweenSuperPeerAndSimplePeers

    @public
    def getConnectionsBetweenSimplePeerAndSuperPeers(self):
        return self.__connectionsBetweenSimplePeerAndSuperPeers

    @public
    def setConnectionsBetweenSuperPeerAndSimplePeers(self, value):
        self.__connectionsBetweenSuperPeerAndSimplePeers = value
        return self.__connectionsBetweenSuperPeerAndSimplePeers

    @public
    def setConnectionsBetweenSimplePeerAndSuperPeers(self, value):
        self.__connectionsBetweenSimplePeerAndSuperPeers = value
        return self.__connectionsBetweenSimplePeerAndSuperPeers
    
    @public
    def getLinkAvailability(self):
        return self.__availability

    @public
    def setLinkAvailability(self, availability):
        requires(availability, float)
        pre_condition(availability, lambda x: x > 0.0)
        
        self.__availability = availability
        return self.__availability
    
    @public
    def getSuperPeerLink(self):
        return self.__superPeerLink

    @public
    def setSuperPeerLink(self, superPeerLink):
        self.__superPeerLink = superPeerLink
        return self.__superPeerLink
    
    
    simulation = property(getSimulation, setSimulation, None, None)

    connectionsBetweenSuperPeers = property(getConnectionsBetweenSuperPeers, setConnectionsBetweenSuperPeers, None, None)

    connectionsBetweenSuperPeerAndSimplePeers = property(getConnectionsBetweenSuperPeerAndSimplePeers, setConnectionsBetweenSuperPeerAndSimplePeers, None, None)

    connectionsBetweenSimplePeerAndSuperPeers = property(getConnectionsBetweenSimplePeerAndSuperPeers, setConnectionsBetweenSimplePeerAndSuperPeers, None, None)
   
    linkAvailability = property(getLinkAvailability, setLinkAvailability, None, None)

    superPeerLink = property(getSuperPeerLink, setSuperPeerLink, None, None)

