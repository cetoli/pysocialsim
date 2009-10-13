"""
Defines the module with the implementation SimplePeerJoiningSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import requires, pre_condition
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from random import uniform

class SimplePeerJoiningSimulationEventGenerator(AbstractSimulationEventGenerator):
    """
    Defines the implementation of SimplePeerLeavingSimulationEventGenerator
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 13/09/2009
    """

    def __init__(self, alpha, minimum, peers):
        self.initialize(alpha, minimum, peers)
    
    def initialize(self, alpha, minimum, peers):
        requires(alpha, float)
        requires(minimum, float)
        requires(peers, int)
        
        pre_condition(alpha, lambda x: x > 0)
        pre_condition(minimum, lambda x: x > 0)
        pre_condition(peers, lambda x: x > 0)
        
        AbstractSimulationEventGenerator.initialize(self)
        
        self.__alpha = alpha
        self.__minimum = minimum
        self.__peers = peers
        
    @public    
    def generateSimulationEvents(self):
        simulation = self.getSimulation()
        simulator = simulation.getSimulator()
        scheduler = simulator.getScheduler()
        generatedEvents = 0
        network = simulation.getPeerToPeerNetwork()
        for peer in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER):
            lastTime = scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId())
            time = self.__minimum/pow(uniform(0,1), 1/self.__alpha)
            scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId(), int(time))
            generatedEvents += 1
        return generatedEvents      