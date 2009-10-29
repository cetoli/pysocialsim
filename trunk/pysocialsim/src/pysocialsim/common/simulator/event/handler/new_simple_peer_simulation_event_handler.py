"""
Defines the module with the implementation of NewSimplePeerSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class NewSimplePeerSimulationEventHandler(AbstractSimulationEventHandler):
    """
    Defines the implementation of NewSimplePeerSimulationEventHandler
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "NEW_SIMPLE_PEER")
    
    def execute(self):
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        simplePeer = network.getPeer(IPeerToPeerNetwork.SIMPLE_PEER, self.getSimulationEvent().getPeerId())
        simplePeer.join()
        
        return AbstractSimulationEventHandler.execute(self)
        