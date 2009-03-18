from pysocialsim.network.peer.message.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public

class OKDisconnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("OK_DISCONNECT", peer)
    
    @public
    def executeHandler(self, message):
        self.getPeer().disconnected()
        self.getPeer().getNetwork().getTopology().removeNode(self.getPeer().getId())
        
        
    @public
    def clone(self):
        return OKDisconnectMessageHandler(self.getPeer())