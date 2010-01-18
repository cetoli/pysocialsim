"""
Defines the module with the implementation AbstractPeerToPeerMessageHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/10/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.message.i_peer_to_peer_message_handler import IPeerToPeerMessageHandler
from pysocialsim.common.base.decorators import public

class AbstractPeerToPeerMessageHandler(Object, IPeerToPeerMessageHandler):
    """
    Defines the commom implementation for IPeerToPeerMessageHandler subtypes.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 17/10/2009
    """
    
    def __init__(self):
        raise NotImplementedError()

    def initialize(self, handle):
        self.__handle = handle
        self.__peerToPeerProtocol = None
        self.__peerToPeerMessage = None
        self.__peer = None
    
    @public
    def getPeer(self):
        return self.__peer    

    @public
    def getHandle(self):
        return self.__handle

    @public
    def getPeerToPeerMessage(self):
        return self.__peerToPeerMessage
    
    @public
    def handlePeerToPeerMessage(self, peerToPeerMessage):
        self.__peerToPeerMessage = peerToPeerMessage
        self.execute()
        
        messagesLogFile = open("messages.log", "a")
        line = str(peerToPeerMessage.getPriority()) + " " + peerToPeerMessage.getId() + " " + peerToPeerMessage.getHandle() + " " + peerToPeerMessage.getSourceId() + " " + peerToPeerMessage.getTargetId() + " " + str(peerToPeerMessage.getTime()) + " " + str(peerToPeerMessage.getSize()) + " " + str(int(peerToPeerMessage.getTime() + peerToPeerMessage.getPriority())) + " " + str(peerToPeerMessage.getHop() + 1)
        messagesLogFile.write(str(line)+"\n")
        messagesLogFile.close()
        
        return peerToPeerMessage
        
    def execute(self):
        raise NotImplementedError()

    @public
    def init(self, peer):
        self.__peer = peer

    @public
    def clone(self):
        cloneHandler = Object.clone(self)
        cloneHandler.init(self.__peer)
        return cloneHandler

    handle = property(getHandle, None, None, None)

    peerToPeerMessage = property(getPeerToPeerMessage, None, None, None)

    peer = property(getPeer, None, None, None)

