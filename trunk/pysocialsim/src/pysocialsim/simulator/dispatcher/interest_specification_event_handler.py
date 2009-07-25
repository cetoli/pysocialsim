from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.public import public

class InterestSpecificationEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("INTEREST_SPECIFICATION", simulation)
    
    @public
    def clone(self):
        return InterestSpecificationEventHandler(self.getSimulation())
    
    def executeHandler(self, event):
        peer = event.getPeer()
        peer.specifyInterest()