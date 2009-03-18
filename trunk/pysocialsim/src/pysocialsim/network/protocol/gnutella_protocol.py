from pysocialsim.network.protocol.abstract_protocol import AbstractProtocol
from pysocialsim.network.peer.message.connect_message_handler import ConnectMessageHandler
from pysocialsim.network.peer.message.disconnect_message_handler import DisconnectMessageHandler
from pysocialsim.network.peer.message.ok_connect_message_handler import OKConnectMessageHandler
from pysocialsim.network.peer.message.ok_disconnect_message_handler import OKDisconnectMessageHandler
from pysocialsim.base.decorator.public import public

class GnutellaProtocol(AbstractProtocol):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self):
        AbstractProtocol.initialize(self)
        self.registerMessageHandlerClass("CONNECT", ConnectMessageHandler)
        self.registerMessageHandlerClass("DISCONNECT", DisconnectMessageHandler)
        self.registerMessageHandlerClass("OK_CONNECT", OKConnectMessageHandler)
        self.registerMessageHandlerClass("OK_DISCONNECT", OKDisconnectMessageHandler)
    
    @public    
    def sendMessage(self, message):
        self.getTopology().dispatchMessage(message)
    
    @public
    def receiveMessage(self, message):
        peer = self.getPeer()
        if peer.getId() == message.getTargetId():
            dispatcher = peer.getMessageDispatcher()
            dispatcher.handleMessage(message)
        else:
            print message.getName()
            network = peer.getNetwork()
            topology = self.getTopology()
            neighbors = topology.getNeighbors(peer.getId())
            message.registerTrace(peer.getId())
            for id in neighbors:
                if id <> peer.getId():
                    msg = message.clone()
                    msg.setSourceId(peer.getId())
                    msg.setTargetId(id)
                    neighbor = network.getPeer(id)
                    neighbor.send(msg)
            
    
    @public
    def advertise(self, advertisementType):
        raise NotImplementedError()
    
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