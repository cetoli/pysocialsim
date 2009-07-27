from pysocialsim.simulator.event.abstract_event import AbstractEvent

class SocialCloudCreationEvent(AbstractEvent):
    
    def __init__(self, peer, priority):
        self.initialize("SOCIAL_CLOUD_CREATION", peer, priority)