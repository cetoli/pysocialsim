from pysocialsim.p2p.message.abstract_p2p_message import AbstractP2PMessage
from pysocialsim.p2p.message.i_p2p_message import IP2PMessage
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type

class OKConnectMessage(AbstractP2PMessage):
    
    def __init__(self, id, sourceId, targetId, ttl, priority):
        self.initialize("OK_CONNECT", id, sourceId, targetId, ttl, priority)
    
    @public
    def clone(self):
        message = OKConnectMessage(self.getId(), self.getSourceId(), self.getTargetId(), self.getTTL(), self.getPriority())
        message.setHop(self.getHop())
        for id in self.getTraces():
            message.registerTrace(id)
        return message