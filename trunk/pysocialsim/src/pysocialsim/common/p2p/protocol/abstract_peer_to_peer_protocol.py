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
        self.__peerToPeerMessageCreator = PeerToPeerMessageCreator()
        self.__peerToPeerMessageCreator.registerPeerToPeerMessage(self.PingPeerToPeerMessage())
        self.__peerToPeerMessageCreator.registerPeerToPeerMessage(self.PongPeerToPeerMessage())
        
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
        raise NotImplementedError()
    
    @public
    def receive(self, peer, peerToPeerMessage):
        raise NotImplementedError()
    
    class PingPeerToPeerMessage(AbstractPeertoPeerMessage):
        
        def __init__(self):
            AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.ADVERTISEMENT, IPeerToPeerProtocol.PING)
    
    class PongPeerToPeerMessage(AbstractPeertoPeerMessage):
        
        def __init__(self):
            AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.ADVERTISEMENT, IPeerToPeerProtocol.PONG)