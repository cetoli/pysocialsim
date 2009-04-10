from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.simulator.simulation.event.event import Event
from pysocialsim.base.decorator.require import require
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.dispatcher.event_handler import EventHandler
from pysocialsim.network.peer.necessity.necessity_constants import NecessityConstants

class ContentNecessityEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("CONTENT_NECESSITY", simulation)
        
    @require("event", Event)
    def executeHandler(self, event):
        peer = event.getPeer()
        peer.createNecessity(NecessityConstants.CONTENT)
        
    @public
    @return_type(EventHandler)
    def clone(self):
        return ContentNecessityEventHandler(self.getSimulation())