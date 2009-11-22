"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 06/11/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from random import uniform
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.simulator.event.generator.simple_peer_interest_simulation_event import SimplePeerInterestSimulationEvent

class SimplePeerInterestSimulationEventGenerator(AbstractSimulationEventGenerator):

    def __init__(self, alpha, minimum):
        self.initialize(alpha, minimum)
        
    def initialize(self, alpha, minimum):
        AbstractSimulationEventGenerator.initialize(self)
        
        self.__alpha = alpha
        self.__minimum = minimum
        
    @public    
    def generateSimulationEvents(self):
        simulation = self.getSimulation()
        simulator = simulation.getSimulator()
        scheduler = simulator.getScheduler()
        generatedEvents = 0
        network = simulation.getPeerToPeerNetwork()
        
        for peer in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER):
            time = self.__minimum/pow(uniform(0,1), 1/self.__alpha)
            
            if scheduler.countTimesForContext(IContext.INTEREST, peer.getId()) == 0:
                peerTime = scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId())
                scheduler.registerTimeForContext(IContext.INTEREST, peer.getId(), int(peerTime + time))
                event = SimplePeerInterestSimulationEvent(peer.getId(), int(peerTime + time))
                simulation.registerSimulationEvent(event)
                generatedEvents += 1
                continue
            
            lastTime = scheduler.getTimeForContext(IContext.INTEREST, peer.getId())
            event = SimplePeerInterestSimulationEvent(peer.getId(), int(lastTime + time))
            simulation.registerSimulationEvent(event)
            scheduler.registerTimeForContext(IContext.INTEREST, peer.getId(), int(lastTime + time))
            generatedEvents += 1
        
        return generatedEvents      