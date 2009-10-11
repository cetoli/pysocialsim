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
        simulation = self.getSimulation()
        simulator = simulation.getSimulator()
        scheduler = simulator.getScheduler()
        generatedEvents = 0
        for peerId in range(1, self.__peers + 1):
            lastTime = scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peerId)
            time = (self.__scale*pow((-math.log(uniform(0,1))), 1/self.__shape)) * 3600
            scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peerId, int((lastTime + time)))
            generatedEvents += 1
        return generatedEvents      