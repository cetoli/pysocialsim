from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.public import public

class PeerDisconnectionEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("DISCONNECT_PEER", simulation)
    
    @public
    def clone(self):
        return PeerDisconnectionEventHandler(self.getSimulation())
    
    def executeHandler(self, event):
        peer = event.getPeer()
        peer.disconnect(event.getPriority())
        peer.setScheduledForDisconnection(False)