from pysocialsim.p2p.dispatcher.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public

class InviteCreateSocialCloudMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("INVITE_CREATE_SOCIAL_CLOUD", peer)
        
    @public
    def clone(self):
        return InviteCreateSocialCloudMessageHandler(self.getPeer())
    
    def executeHandler(self):
        print self.getMessageName()