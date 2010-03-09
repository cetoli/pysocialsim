"""
Defines the module with the implementation SimplePeerLeavingSimulationEventGenerator class.

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
from pysocialsim.common.simulator.event.generator.simple_peer_leaving_simulation_event import SimplePeerLeavingSimulationEvent
import math

class SimplePeerLeavingSimulationEventGenerator(AbstractSimulationEventGenerator):
    """
    Defines the implementation of SimplePeerLeavingSimulationEventGenerator
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 13/09/2009
    """

    def __init__(self, shape, scale, peers):
        self.initialize(shape, scale, peers)
    
    def initialize(self, shape, scale, peers):
        requires(shape, float)
        requires(scale, float)
        requires(peers, int)
        
        pre_condition(shape, lambda x: x > 0)
        pre_condition(scale, lambda x: x > 0)
        pre_condition(peers, lambda x: x > 0)
        
        AbstractSimulationEventGenerator.initialize(self)
        
        self.__shape = shape
        self.__scale = scale
        self.__peers = peers
        
    @public    
    def generateSimulationEvents(self):
        print "Generating SIMPLE_PEER_LEAVE ."
        simulation = self.getSimulation()
        simulator = simulation.getSimulator()
        scheduler = simulator.getScheduler()
        generatedEvents = 0
        network = simulation.getPeerToPeerNetwork()
        print "Generating SIMPLE_PEER_LEAVE .."
        for peer in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER):
            lastTime = scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId())
            time = (self.__scale*pow((-math.log(uniform(0,1))), 1/self.__shape)) * 3600
            
            scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId(), int((lastTime + time)))
            event = SimplePeerLeavingSimulationEvent(peer.getId(), scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId()))
            simulation.registerSimulationEvent(event)
            generatedEvents += 1
            
        print "Generating SIMPLE_PEER_LEAVE ..."
        print "Done. (" + str(generatedEvents) +" events were generated)"
        return generatedEvents      