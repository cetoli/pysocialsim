from pysocialsim.p2p.profile.abstract_social_relationship import AbstractSocialRelationship

class DefaultSocialRelationship(AbstractSocialRelationship):
    
    def __init__(self, targetId, targetCloudId):
        self.initialize(targetId, targetCloudId)