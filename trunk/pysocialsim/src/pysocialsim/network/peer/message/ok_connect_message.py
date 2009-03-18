from pysocialsim.network.message.abstract_message import AbstractMessage
from pysocialsim.base.decorator.public import public

class OKConnectMessage(AbstractMessage):
    
    def __init__(self, sourceId, targetId, ttl):
        self.initialize("OK_CONNECT", sourceId, targetId, ttl)
        
    @public
    def clone(self):
        message = OKConnectMessage(self.getSourceId(), self.getTargetId(), self.getTTL())
        for id in self.getTraces():
            message.registerTrace(id)
        return message