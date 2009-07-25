from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.dispatcher.i_event_handler import IEventHandler
from pysocialsim.simulator.event.i_event import IEvent
from pysocialsim.base.decorator.require import require

class ReceiveEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("RECEIVE_MESSAGE", simulation)
        
    @public
    def clone(self):
        return ReceiveEventHandler(self.getSimulation())
    
    def executeHandler(self, event):
        peer = event.getPeer()
        peer.receiveMessage(event.getP2PMessage())