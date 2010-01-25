"""
Defines the module with the implementation of NewSuperPeerSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class NewSuperPeerSimulationEventHandler(AbstractSimulationEventHandler):
    """
    Defines the implementation of NewSuperPeerSimulationEventHandler
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "NEW_SUPER_PEER")
    
    def execute(self):
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        superPeer = network.getPeer(IPeerToPeerNetwork.SUPER_PEER, self.getSimulationEvent().getPeerId())
        
        event = self.getSimulationEvent()
        
        if superPeer.join():
            superPeer.setJoinTime(event.getPriority())
        
        return AbstractSimulationEventHandler.execute(self)
        