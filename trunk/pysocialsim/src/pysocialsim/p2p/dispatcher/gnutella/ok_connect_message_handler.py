from pysocialsim.p2p.dispatcher.abstract_message_handler import AbstractMessageHandler
from pysocialsim.p2p.dispatcher.i_message_handler import IMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type

class OKConnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("OK_CONNECT", peer)
    
    @public
    def clone(self):
        return OKConnectMessageHandler(self.getPeer())
    
    def executeHandler(self):
        peer = self.getPeer()
        message = self.getP2PMessage()
        peer.createConnection(message.getSourceId())
