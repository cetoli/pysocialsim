from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.simulation.event.event import Event
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.dispatcher.event_handler import EventHandler
from pysocialsim.network.peer.peer_constants import PeerConstants

class FileAdvertisementEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("FILE_ADVERTISEMENT", simulation)
        
    @require("event", Event)
    def executeHandler(self, event):
        peer = event.getPeer()
        peer.advertise(PeerConstants.FILE_ADVERTISEMENT)
        
    @public
    @return_type(EventHandler)
    def clone(self):
        return FileAdvertisementEventHandler(self.getSimulation())