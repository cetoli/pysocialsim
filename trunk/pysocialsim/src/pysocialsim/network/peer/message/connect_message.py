from pysocialsim.network.message.abstract_message import AbstractMessage
from pysocialsim.base.decorator.public import public

class ConnectMessage(AbstractMessage):
    
    def __init__(self, id, sourceId, targetId, ttl):
        self.initialize("CONNECT", id, sourceId, targetId, ttl)
    
    @public
    def clone(self):
        message = ConnectMessage(self.getId(), self.getSourceId(), self.getTargetId(), self.getTTL())
        message.setHop(self.getHop())
        for id in self.getTraces():
            message.registerTrace(id)
        return message