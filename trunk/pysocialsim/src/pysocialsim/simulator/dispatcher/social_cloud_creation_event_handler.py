from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.public import public

class SocialCloudCreationEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("SOCIAL_CLOUD_CREATION", simulation)
        
    @public
    def clone(self):
        return SocialCloudCreationEventHandler(self.getSimulation())
    
    def executeHandler(self, event):
        peer = event.getPeer()
        peer.createSocialCloud()