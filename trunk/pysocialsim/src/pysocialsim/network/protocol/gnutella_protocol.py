from pysocialsim.network.protocol.abstract_protocol import AbstractProtocol
from pysocialsim.network.peer.message.connect_message_handler import ConnectMessageHandler
from pysocialsim.network.peer.message.disconnect_message_handler import DisconnectMessageHandler
from pysocialsim.network.peer.message.ok_connect_message_handler import OKConnectMessageHandler
from pysocialsim.network.peer.message.ok_disconnect_message_handler import OKDisconnectMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.network.peer.message.file_advertisement_message_handler import FileAdvertisementMessageHandler
from random import randint
from pysocialsim.network.peer.message.file_advertisement_message import FileAdvertisementMessage
from pysocialsim.network.message.message_manager import MessageManager
from pysocialsim.network.peer.peer import Peer
from pysocialsim.network.peer.peer_constants import PeerConstants

class GnutellaProtocol(AbstractProtocol):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self):
        AbstractProtocol.initialize(self)
        self.registerMessageHandlerClass("CONNECT", ConnectMessageHandler)
        self.registerMessageHandlerClass("DISCONNECT", DisconnectMessageHandler)
        self.registerMessageHandlerClass("OK_CONNECT", OKConnectMessageHandler)
        self.registerMessageHandlerClass("OK_DISCONNECT", OKDisconnectMessageHandler)
        self.registerMessageHandlerClass("FILE_ADVERTISEMENT", FileAdvertisementMessageHandler)
    
    @public    
    def sendMessage(self, message):
        self.getTopology().dispatchMessage(message)
    
    @public
    def receiveMessage(self, message):
        peer = self.getPeer()
        if peer.getId() == message.getTargetId():
            dispatcher = peer.getMessageDispatcher()
            dispatcher.handleMessage(message)
#        else:
#            print message.getName()
#            network = peer.getNetwork()
#            topology = self.getTopology()
#            neighbors = topology.getNeighbors(peer.getId())
#            message.registerTrace(peer.getId())
#            for id in neighbors:
#                if id <> peer.getId():
#                    msg = message.clone()
#                    msg.setSourceId(peer.getId())
#                    msg.setTargetId(id)
#                    neighbor = network.getPeer(id)
#                    neighbor.send(msg)
            
    
    @public
    def advertise(self, advertisementType):
        if advertisementType == PeerConstants.FILE_ADVERTISEMENT:
            self.advertiseFile()
    
    @public
    def clone(self):
        protocol = GnutellaProtocol()
        protocol.setPeer(self.getPeer())
        protocol.setTopology(self.getTopology())
        return protocol
    
    @public
    def connect(self):
        self.getTopology().connect(self.getPeer())
    
    @public
    def disconnect(self):
        self.getTopology().disconnect(self.getPeer())
        
    def advertiseFile(self):
        if self.getPeer().countFiles() == 0:
            return
        fileId = randint(0, self.getPeer().countFiles() - 1)
        files = self.getPeer().getFiles()
        network = self.getPeer().getNetwork()
        topology = network.getTopology()
        neighbors = topology.getNeighbors(self.getPeer().getId())
        for id in neighbors:
            message = FileAdvertisementMessage(MessageManager().getMessageId(), self.getPeer().getId(), id, network.getSimulation().getTTL())
            message.setHop(1)
            message.registerTrace(self.getPeer().getId())
            message.setParameter("fileId", fileId)
            message.setParameter("folksonomies", files[fileId].getFolksonomies())
            self.getPeer().send(message)