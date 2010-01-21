"""
Defines the module with the implementation of AbstractPeerToPeerProtocol class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/09/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import requires, pre_condition, returns
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message import AbstractPeertoPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_creator import PeerToPeerMessageCreator
from pysocialsim.common.p2p.message.i_peer_to_peer_message_creator import IPeerToPeerMessageCreator
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
from pysocialsim.common.p2p.peer.i_peer import IPeer

class AbstractPeerToPeerProtocol(Object, IPeerToPeerProtocol):
    """
    Defines the abstract implementation of IPeerToPeerProtocol interface
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 20/09/2009
    """
    
    __public__ = ["PING"]
    
    def __init__(self):
        raise NotImplementedError()

    def initialize(self):
        self.__peerToPeerTopology = None
        self.__pingHops = 0
        self.__pongHops = 0
        self.__pullHops = 0
        self.__pushHops = 0
        self.__peerToPeerMessageCreator = PeerToPeerMessageCreator()
        self.__peerToPeerMessageCreator.registerPeerToPeerMessage(self.PingPeerToPeerMessage())
        self.__peerToPeerMessageCreator.registerPeerToPeerMessage(self.PongPeerToPeerMessage())
        self.__peerToPeerMessageCreator.registerPeerToPeerMessage(self.RoutePeerToPeerMessage())
        self.__peerToPeerMessageCreator.registerPeerToPeerMessage(self.PushPeerToPeerMessage())
    
    @public
    def getPingHops(self):
        return self.__pingHops

    @public
    def getPongHops(self):
        return self.__pongHops

    @public
    def getPullHops(self):
        return self.__pullHops

    @public
    def getPushHops(self):
        return self.__pushHops

    @public
    def setPingHops(self, pingHops):
        self.__pingHops = pingHops
        return self.__pingHops

    @public
    def setPongHops(self, pongHops):
        self.__pongHops = pongHops
        return self.__pongHops

    @public
    def setPullHops(self, pullHops):
        self.__pullHops = pullHops
        return self.__pullHops

    @public
    def setPushHops(self, pushHops):
        self.__pushHops = pushHops
        return self.__pushHops
        
    def getPeerToPeerMessageCreator(self):
        return returns(self.__peerToPeerMessageCreator, IPeerToPeerMessageCreator)
        
    @public
    def setPeerToPeerTopology(self, peerToPeerTopology):
        requires(peerToPeerTopology, IPeerToPeerTopology)
        pre_condition(peerToPeerTopology, lambda x: x <> None)
        
        self.__peerToPeerTopology = peerToPeerTopology
        
        return returns(self.__peerToPeerTopology, IPeerToPeerTopology)

    @public
    def getPeerToPeerTopology(self):
        return returns(self.__peerToPeerTopology, IPeerToPeerTopology)
    
    @public
    def createPeerToPeerMessage(self, handle):
        return self.__peerToPeerMessageCreator.createPeerToPeerMessage(handle)
    
    @public
    def push(self, peer, peerToPeerMessage):
        raise NotImplementedError()
    
    @public
    def pull(self, peer, peerToPeerMessage):
        raise NotImplementedError()
    
    @public
    def ping(self, peer, peerToPeerMessage):
        raise NotImplementedError()
    
    @public
    def pong(self, peer, peerToPeerMessage):
        raise NotImplementedError()
    
    @public
    def route(self, peerToPeerMessage):
        raise NotImplementedError()
    
    @public
    def send(self, peer, peerToPeerMessage):
        if not peer.hasNeighbor(peerToPeerMessage.getTargetId()):
            self.route(peer, peerToPeerMessage)
            return peerToPeerMessage
        
        neighbor = peer.getNeighbor(peerToPeerMessage.getTargetId())
        return neighbor.dispatchData(peerToPeerMessage)
    
    @public
    def receive(self, peer, peerToPeerMessage):
        requires(peer, IPeer)
        requires(peerToPeerMessage, IPeerToPeerMessage)
        
        pre_condition(peer, lambda x: x <> None)
        pre_condition(peerToPeerMessage, lambda x: x <> None)
       
        return peer.receive(peerToPeerMessage)
    
    class PingPeerToPeerMessage(AbstractPeertoPeerMessage):
        
        def __init__(self):
            AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.ADVERTISEMENT, IPeerToPeerProtocol.PING, 512)
    
    class PongPeerToPeerMessage(AbstractPeertoPeerMessage):
        
        def __init__(self):
            AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.ADVERTISEMENT, IPeerToPeerProtocol.PONG, 512)
    
    class RoutePeerToPeerMessage(AbstractPeertoPeerMessage):
        
        def __init__(self):
            AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.SYSTEM, IPeerToPeerProtocol.ROUTE, 512)
        
        @public
        def setTime(self, time):
            if self.hasParameter("peerToPeerMessage"):
                message = self.getParameter("peerToPeerMessage")
                message.setTime(time)
                
            AbstractPeertoPeerMessage.setTime(self, time)
        
    class PushPeerToPeerMessage(AbstractPeertoPeerMessage):
        
        def __init__(self):
            AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.ADVERTISEMENT, IPeerToPeerProtocol.PUSH, 512)
        
        @public    
        def setTime(self, time):
            if self.hasParameter("peerToPeerMessage"):
                message = self.getParameter("peerToPeerMessage")
                message.setTime(time)
                
            return AbstractPeertoPeerMessage.setTime(self, time)
        
        @public    
        def setHop(self, hop):
            if self.hasParameter("peerToPeerMessage"):
                message = self.getParameter("peerToPeerMessage")
                message.setHop(hop)
                
            return AbstractPeertoPeerMessage.setHop(self, hop)
        
        @public    
        def clone(self):
            cln = AbstractPeertoPeerMessage.clone(self)
            if self.hasParameter("peerToPeerMessage"):
                message = self.getParameter("peerToPeerMessage")
                cloneMsg = message.clone()
                cloneMsg.init(message.getId(), message.getSourceId(), cln.getTargetId(), message.getTTL(), message.getPriority(), message.getSize(), message.getTime())
                cln.unregisterParameter("peerToPeerMessage")
                cln.registerParameter("peerToPeerMessage", cloneMsg)
            return cln
                
    pingHops = property(getPingHops, setPingHops, None, None)

    pongHops = property(getPongHops, setPongHops, None, None)

    pullHops = property(getPullHops, setPullHops, None, None)

    pushHops = property(getPushHops, setPushHops, None, None)
