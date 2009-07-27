from pysocialsim.p2p.message.abstract_p2p_message import AbstractP2PMessage
from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.message.gnutella.advertise_content_message import AdvertiseContentMessage

class InviteCreateSocialCloudMessage(AbstractP2PMessage):
    
    def __init__(self, id, sourceId, targetId, ttl, priority):
        self.initialize("INVITE_CREATE_SOCIAL_CLOUD", id, sourceId, targetId, ttl, priority)
    
    @public
    def clone(self):
        message = AdvertiseContentMessage(self.getId(), self.getSourceId(), self.getTargetId(), self.getTTL(), self.getPriority())
        message.setHop(self.getHop())
        for id in self.getTraces():
            message.registerTrace(id)
        for name in self.getParameterNames():
            message.setParameter(name, self.getParameter(name))
        return message