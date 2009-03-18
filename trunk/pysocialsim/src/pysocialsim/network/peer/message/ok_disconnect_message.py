from pysocialsim.network.message.abstract_message import AbstractMessage
from pysocialsim.base.decorator.public import public

class OKDisconnectMessage(AbstractMessage):
    
    def __init__(self, sourceId, targetId, ttl):
        self.initialize("OK_DISCONNECT", sourceId, targetId, ttl)
        
    @public
    def clone(self):
        message = OKDisconnectMessage(self.getSourceId(), self.getTargetId(), self.getTTL())
        for id in self.getTraces():
            message.registerTrace(id)
        return message