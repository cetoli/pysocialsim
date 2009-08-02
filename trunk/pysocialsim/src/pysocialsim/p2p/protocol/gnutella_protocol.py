from pysocialsim.p2p.protocol.abstract_p2p_protocol import AbstractP2PProtocol
from pysocialsim.base.decorator.public import public
from threading import Semaphore
from random import randint
from pysocialsim.p2p.message.message_manager import MessageManager
from pysocialsim.p2p.dispatcher.gnutella.connect_message_handler import ConnectMessageHandler
from pysocialsim.p2p.dispatcher.gnutella.ok_connect_message_handler import OKConnectMessageHandler
from pysocialsim.p2p.dispatcher.gnutella.disconnect_message_handler import DisconnectMessageHandler
from pysocialsim.p2p.dispatcher.gnutella.ok_disconnect_message_handler import OKDisconnectMessageHandler
from pysocialsim.p2p.message.gnutella.advertise_content_message import AdvertiseContentMessage
from pysocialsim.p2p.dispatcher.gnutella.advertise_content_message_handler import AdvertiseContentMessageHandler

class GnutellaProtocol(AbstractP2PProtocol):
    
    def __init__(self):
        self.initialize()
    
    @public
    def setPeer(self, peer):
        self.registerMessageHandler(ConnectMessageHandler(peer))
        self.registerMessageHandler(OKConnectMessageHandler(peer))
        self.registerMessageHandler(DisconnectMessageHandler(peer))
        self.registerMessageHandler(OKDisconnectMessageHandler(peer))
        self.registerMessageHandler(AdvertiseContentMessageHandler(peer))
        return AbstractP2PProtocol.setPeer(self, peer)
    
    @public    
    def sendMessage(self, message):
        self.getP2PTopology().dispatchMessage(message)
        
    
    @public
    def receiveMessage(self, message):
        if self.getPeer().getId() == message.getTargetId():
            dispatcher = self.getPeer().getMessageDispatcher()
            dispatcher.handleP2PMessage(message)
        else:
            print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            
    @public
    def advertise(self, element, advertisementType):
        peer = self.getPeer()
        neighbors = self.getP2PTopology().getNeighbors(peer.getId())
        for n in neighbors:
            message = AdvertiseContentMessage(MessageManager().getMessageId(), peer.getId(), n, 3, 0)
            message.registerTrace(self.getPeer().getId())
            message.setParameter("contentId", element.getId())
            message.setParameter("folksonomies", element.getFolksonomies())
            message.setParameter("type", advertisementType)
            peer.send(message)
    
    @public
    def connect(self, priority):
        sem = Semaphore()
        sem.acquire()
        if self.getPeer().isConnected():
            return
        topology = self.getP2PTopology()
        
        node = None
        if topology.countNodes() > 0:
            idx = randint(0, topology.countNodes() - 1)
            graph = topology.getGraph()
            node = graph.keys()[idx]
        
        topology.addNode(self.getPeer().getId())
        if node:
            topology.createConnection(self.getPeer().getId(), node)
            
        self.getPeer().connected()
        disconnectionTime = randint(3600, 28800)
        self.getPeer().setDisconnectionTime(disconnectionTime)
        
        sem.release()
    
    @public
    def disconnect(self, priority):
        sem = Semaphore()
        sem.acquire()
        if not self.getPeer().isConnected():
            return
        
        topology = self.getP2PTopology()
        neighbors = topology.getNeighbors(self.getPeer().getId())
        if len(neighbors) > 0:
            for n in neighbors:
                topology.removeConnection(self.getPeer().getId(), n)
                self.getPeer().disconnected()
        else:
            self.getPeer().disconnected()
            
    @public
    def clone(self):
        raise NotImplementedError()