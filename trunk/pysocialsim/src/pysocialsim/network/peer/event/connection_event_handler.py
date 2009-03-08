from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.simulator.simulation.event.event import Event
from pysocialsim.base.decorator.require import require
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.dispatcher.event_handler import EventHandler

class ConnectionEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("CONNECT_PEER", simulation)
        
    @require("event", Event)
    def executeHandler(self, event):
        print event.getHandle(), event.getPriority(), event.getPeer().getId()
        peer = event.getPeer()
        peer.connect()
        
    @public
    @return_type(EventHandler)
    def clone(self):
        return ConnectionEventHandler(self.getSimulation())
        
    