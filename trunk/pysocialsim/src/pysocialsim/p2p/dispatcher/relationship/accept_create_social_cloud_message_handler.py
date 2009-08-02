from pysocialsim.p2p.dispatcher.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.profile.default_social_cloud_view import DefaultSocialCloudView
from random import randint

class AcceptCreateSocialCloudMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("ACCEPT_CREATE_SOCIAL_CLOUD", peer)
        
    @public
    def clone(self):
        return AcceptCreateSocialCloudMessageHandler(self.getPeer())
    
    def executeHandler(self):
        
        cloud = DefaultSocialCloudView(randint(0, 9999999999999999))