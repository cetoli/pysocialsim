from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.public import public

class PeerConnectionEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("CONNECT_PEER", simulation)
    
    @public
    def clone(self):
        return PeerConnectionEventHandler(self.getSimulation())
    
    def executeHandler(self, event):
        peer = event.getPeer()
        peer.connect(event.getPriority())
