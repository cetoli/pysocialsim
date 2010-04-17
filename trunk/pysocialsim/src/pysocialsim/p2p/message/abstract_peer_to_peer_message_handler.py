"""
Defines the module with the implementation AbstractPeerToPeerMessageHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/10/2009
"""
from pysocialsim.p2p.message.i_peer_to_peer_message_handler import IPeerToPeerMessageHandler
from pysocialsim.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class AbstractPeerToPeerMessageHandler(IPeerToPeerMessageHandler):
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
    
    
    def getPeer(self):
        return self.__peer    

    
    def getHandle(self):
        return self.__handle

    
    def getPeerToPeerMessage(self):
        return self.__peerToPeerMessage
    
    
    def handlePeerToPeerMessage(self, peerToPeerMessage):
        self.__peerToPeerMessage = peerToPeerMessage
        self.execute()
        
        network = self.__peer.getPeerToPeerNetwork()
        
        simulation = network.getSimulation()
        
        messagesLogFile = open(self.getHandle()+str(simulation.getVersion())+".log", "a")
        line = str(peerToPeerMessage.getPriority()) + " " + peerToPeerMessage.getId() + " " + peerToPeerMessage.getHandle() + " " + peerToPeerMessage.getSourceId() + " " + self.__peerToPeerMessage.getTargetId() + " " + str(peerToPeerMessage.getTime()) + " " + str(peerToPeerMessage.getSize()) + " " + str(int(peerToPeerMessage.getTime() + peerToPeerMessage.getPriority())) + " " + str(peerToPeerMessage.countPeerIds()) + " " + str(network.countConnectedPeers(IPeerToPeerNetwork.SUPER_PEER)) + " " + str(network.countConnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER)) 
        messagesLogFile.write(str(line)+"\n")
        messagesLogFile.close()
        
        return peerToPeerMessage
        
    def execute(self):
        raise NotImplementedError()

    
    def init(self, peer):
        self.__peer = peer
    
    
    def clone(self):
        cloneHandler = self.__class__()
        cloneHandler.init(self.__peer)
        
        return cloneHandler

    
