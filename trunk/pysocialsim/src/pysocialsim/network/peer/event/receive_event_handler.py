from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.simulation.event.event import Event
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.dispatcher.event_handler import EventHandler

class ReceiveEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("RECEIVE_MESSAGE", simulation)
        
    @require("event", Event)
    def executeHandler(self, event):
        simulation = self.getSimulation()
        network = simulation.getNetwork()
        message = event.getMessage()
        peer = event.getPeer()
        peer.receiveMessage(message)
        
        
    @public
    @return_type(EventHandler)
    def clone(self):
        return ReceiveEventHandler(self.getSimulation())