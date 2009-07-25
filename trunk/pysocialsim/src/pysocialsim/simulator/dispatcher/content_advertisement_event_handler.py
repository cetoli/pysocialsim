from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.dispatcher.i_event_handler import IEventHandler
from pysocialsim.simulator.event.i_event import IEvent
from pysocialsim.base.decorator.require import require
from pysocialsim.p2p.peer.i_peer import IPeer

class ContentAdvertisementEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("ADVERTISE_CONTENT", simulation)
    
    @public
    def clone(self):
        return ContentAdvertisementEventHandler(self.getSimulation())
    
    def executeHandler(self, event):
        peer = event.getPeer()
        if not peer.isConnected():
            return
        peer.advertise(IPeer.CONTENT_ADVERTISEMENT)