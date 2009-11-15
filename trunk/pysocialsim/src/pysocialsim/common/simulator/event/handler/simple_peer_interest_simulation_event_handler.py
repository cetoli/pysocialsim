"""
Defines the module with SimplePeerSimulationEventHandler.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 06/11/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class SimplePeerInterestSimulationEventHandler(AbstractSimulationEventHandler):

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "SIMPLE_PEER_INTEREST")
        
    def execute(self):
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        simplePeer = network.getPeer(IPeerToPeerNetwork.SIMPLE_PEER, self.getSimulationEvent().getPeerId())
        
        return AbstractSimulationEventHandler.execute(self)
        