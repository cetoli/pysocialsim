from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.public import public

class SendEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("SEND_MESSAGE", simulation)
    
    @public
    def clone(self):
        return SendEventHandler(self.getSimulation())
    
    def executeHandler(self, event):
        peer = event.getPeer()
        peer.sendMessage(event.getP2PMessage())