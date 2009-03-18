from pysocialsim.network.peer.message.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.network.peer.message.ok_disconnect_message import OKDisconnectMessage
from pysocialsim.network.message.message_manager import MessageManager

class DisconnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("DISCONNECT", peer)
        
    @public
    def executeHandler(self, message):
        network = self.getPeer().getNetwork()
        peer = network.getPeer(message.getSourceId())
        message = OKDisconnectMessage(MessageManager().getMessageId(), message.getTargetId(), message.getSourceId(), message.getTTL())
        peer.send(message)
        self.getPeer().getNetwork().getTopology().removeConnection(message.getTargetId(), message.getSourceId())
        
    @public
    def clone(self):
        return DisconnectMessageHandler(self.getPeer())