from pysocialsim.network.peer.message.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.network.peer.message.ok_disconnect_message import OKDisconnectMessage

class DisconnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("DISCONNECT", peer)
        
    @public
    def executeHandler(self, message):
        network = self.getPeer().getNetwork()
        peer = network.getPeer(message.getSourceId())
        message = OKDisconnectMessage(message.getTargetId(), message.getSourceId(), message.getTTL())
        peer.send(message)
        self.getPeer().getNetwork().getTopology().removeNode(self.getPeer().getId())
        
    @public
    def clone(self):
        return DisconnectMessageHandler(self.getPeer())