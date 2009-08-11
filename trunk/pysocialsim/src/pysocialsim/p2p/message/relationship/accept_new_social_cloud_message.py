from pysocialsim.p2p.message.abstract_p2p_message import AbstractP2PMessage
from pysocialsim.base.decorator.public import public

class AcceptNewSocialCloudMessage(AbstractP2PMessage):
    
    def __init__(self, id, sourceId, targetId, ttl, priority):
        self.initialize("ACCEPT_NEW_SOCIAL_CLOUD", id, sourceId, targetId, ttl, priority)
    
    @public
    def clone(self):
        message = AcceptNewSocialCloudMessage(self.getId(), self.getSourceId(), self.getTargetId(), self.getTTL(), self.getPriority())
        message.setHop(self.getHop())
        for id in self.getTraces():
            message.registerTrace(id)
        for name in self.getParameterNames():
            message.setParameter(name, self.getParameter(name))
        return message