from pysocialsim.p2p.profile.abstract_social_matching import AbstractSocialMatching

class DefaultSocialMatching(AbstractSocialMatching):
    
    def __init__(self, peerId, elementId, percentage):
        self.initialize(peerId, elementId, percentage)