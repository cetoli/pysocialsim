from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.public import public

class RelationshipCreationEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("RELATIONSHIP_CREATION", simulation)
    
    @public
    def clone(self):
        return RelationshipCreationEventHandler(self.getSimulation())
    
    def executeHandler(self, event):
        peer = event.getPeer()
        peer.createRelationship()
        print event.getHandle()