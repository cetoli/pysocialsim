from pysocialsim.network.peer.message.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.network.peer.message.ok_connect_message import OKConnectMessage
from pysocialsim.network.message.message_manager import MessageManager

class ConnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("CONNECT", peer)
    
    @public
    def executeHandler(self, message):
        network = self.getPeer().getNetwork()
        peer = network.getPeer(message.getSourceId())
        message = OKConnectMessage(MessageManager().getMessageId(), message.getTargetId(), message.getSourceId(), message.getTTL())
        peer.send(message)
        
    @public
    def clone(self):
        return ConnectMessageHandler(self.getPeer())