from pysocialsim.p2p.dispatcher.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.dispatcher.i_message_handler import IMessageHandler
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.p2p.message.message_manager import MessageManager
from pysocialsim.p2p.message.gnutella.ok_connect_message import OKConnectMessage

class ConnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("CONNECT", peer)
    
    @public
    def clone(self):
        return ConnectMessageHandler(self.getPeer())
    
    def executeHandler(self):
        peer = self.getPeer()
        message = self.getP2PMessage()
        msg = OKConnectMessage(MessageManager().getMessageId(), peer.getId(), message.getSourceId(), 3, message.getPriority())
        peer.send(msg)