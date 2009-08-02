from pysocialsim.p2p.dispatcher.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.message.relationship.accept_create_social_cloud_message_handler import AcceptCreateSocialCloudMessage
from pysocialsim.p2p.message.message_manager import MessageManager
from pysocialsim.p2p.profile.default_social_cloud_view import DefaultSocialCloudView
from random import randint
from pysocialsim.p2p.profile.default_social_retationship import DefaultSocialRelationship

class InviteCreateSocialCloudMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("INVITE_CREATE_SOCIAL_CLOUD", peer)
        
    @public
    def clone(self):
        return InviteCreateSocialCloudMessageHandler(self.getPeer())
    
    def executeHandler(self):
        network = self.getPeer().getP2PNetwork()
        simulation = network.getSimulation()
        message = AcceptCreateSocialCloudMessage(MessageManager().getMessageId(), self.getPeer().getId(), self.getP2PMessage().getSourceId(), 3, simulation.getSimulationCurrentTime())
        self.getPeer().send(message)
        
        cloud = DefaultSocialCloudView(randint(0, 9999999999999999))
        profile = self.getPeer().getProfile()
        profile.addSocialCloud(cloud)
        
        relationship = DefaultSocialRelationship(self.getP2PMessage().getSourceId(), 1048576)
        
        cloud.addSocialRelationship(relationship)
        
        print "FOOOOOOOOOOOOOOOOIIIIIIIIIIIII", self.getPeer().getId(), self.getP2PMessage().getParameter("elementId")
        
        content = self.getPeer().getContent(self.getP2PMessage().getParameter("elementId"))
#        
        cloud.addSharedContent(content)
        
        