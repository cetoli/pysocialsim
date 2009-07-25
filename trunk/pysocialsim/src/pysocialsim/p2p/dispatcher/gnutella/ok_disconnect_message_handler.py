from pysocialsim.p2p.dispatcher.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.p2p.dispatcher.i_message_handler import IMessageHandler

class OKDisconnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("OK_DISCONNECT", peer)
    
    @public
    def clone(self):
        return OKDisconnectMessageHandler(self.getPeer())
    
    def executeHandler(self):
        peer = self.getPeer()
        peer.disconnected()
