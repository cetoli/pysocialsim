from pysocialsim.network.peer.message.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public

class OKConnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("OK_CONNECT", peer)
        
    @public
    def executeHandler(self, message):
        self.getPeer().createConnection(message.getTargetId())
        
        
    @public
    def clone(self):
        return OKConnectMessageHandler(self.getPeer())