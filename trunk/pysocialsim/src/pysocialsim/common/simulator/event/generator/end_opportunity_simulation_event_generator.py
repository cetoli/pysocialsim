from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.util.rotines import requires, pre_condition
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.context.i_context import IContext
from random import uniform
from pysocialsim.common.simulator.event.generator.end_opportunity_simulation_event import EndOpportunitySimulationEvent
import math

class EndOpportunitySimulationEventGenerator(AbstractSimulationEventGenerator):
    
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
        generatedEvents = 0
        peerCounter = 0
        network = simulation.getPeerToPeerNetwork()
        
        for peer in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER):
            contextManager = peer.getContextManager()
            opportunities = contextManager.getContexts(IContext.OPPORTUNITY)
            for opportunity in opportunities:
                time = (self.__scale*pow((-math.log(uniform(0,1))), 1/self.__shape)) * 3600
                opportunity.setDurationTime(time)
                
                event = EndOpportunitySimulationEvent(peer.getId(), int(opportunity.getEndTime()))
                event.registerParameter("opportunityId", opportunity.getId())
                
                print opportunity.getId(), opportunity.getStartTime(), opportunity.getDurationTime(), opportunity.getEndTime()
                simulation.registerSimulationEvent(event)
                
                generatedEvents += 1
            
            peerCounter += 1
            
            if peerCounter > self.__peers:
                break
        
        return generatedEvents