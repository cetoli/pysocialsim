from pysocialsim.p2p.message.abstract_p2p_message import AbstractP2PMessage
from pysocialsim.base.decorator.public import public

class ShareContentSocialCloudMessage(AbstractP2PMessage):
    
    def __init__(self, id, sourceId, targetId, ttl, priority):
        self.initialize("SHARE_CONTENT_SOCIAL_CLOUD", id, sourceId, targetId, ttl, priority)
    
    @public
    def clone(self):
        message = ShareContentSocialCloudMessage(self.getId(), self.getSourceId(), self.getTargetId(), self.getTTL(), self.getPriority())
        message.setHop(self.getHop())
        for id in self.getTraces():
            message.registerTrace(id)
        for name in self.getParameterNames():
            message.setParameter(name, self.getParameter(name))
        return message