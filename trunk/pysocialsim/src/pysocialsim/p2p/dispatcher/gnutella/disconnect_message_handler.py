from pysocialsim.p2p.dispatcher.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.message.gnutella.ok_disconnect_message import OKDisconnectMessage
from pysocialsim.p2p.message.message_manager import MessageManager

class DisconnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("DISCONNECT", peer)
    
    @public
    def clone(self):
        return DisconnectMessageHandler(self.getPeer())
    
    def executeHandler(self):
        peer = self.getPeer()
        peer.removeConnection(self.getP2PMessage().getSourceId())
        message = OKDisconnectMessage(MessageManager().getMessageId(), peer.getId(), self.getP2PMessage().getSourceId(), 3, self.getP2PMessage().getPriority())
        peer.send(message)