"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 21/01/2010
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork

class SimplePeerJoiningSimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "SIMPLE_PEER_JOIN")
        
    def execute(self):
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        simplePeer = network.getPeer(IPeerToPeerNetwork.SIMPLE_PEER, self.getSimulationEvent().getPeerId())
        simplePeer.join()
        
        return AbstractSimulationEventHandler.execute(self)