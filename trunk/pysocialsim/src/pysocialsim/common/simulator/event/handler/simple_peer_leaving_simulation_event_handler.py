"""
Defines the module with the implementation of SimplePeerLeavingSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 30/10/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class SimplePeerLeavingSimulationEventHandler(AbstractSimulationEventHandler):
    """
    classdocs
    """

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "SIMPLE_PEER_LEAVE")
    
    def execute(self):
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        superPeer = network.getPeer(IPeerToPeerNetwork.SUPER_PEER, self.getSimulationEvent().getPeerId())
        superPeer.leave()
        
        return AbstractSimulationEventHandler.execute(self)