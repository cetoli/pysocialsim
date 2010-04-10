from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.context.tags_map import TagsMap
from random import randint, uniform
from pysocialsim.common.p2p.peer.profile.interest import Interest
from pysocialsim.common.p2p.peer.context.interest_constraint import InterestConstraint
from pysocialsim.common.p2p.peer.message.advertise_opportunity_peer_to_peer_message import AdvertiseOpportunityPeerToPeerMessage
from pysocialsim.common.p2p.peer.context.context_id_generator import ContextIdGenerator
from pysocialsim.common.simulator.event.generator.push_opportunity_simulation_event import PushOpportunitySimulationEvent
from pysocialsim.common.simulator.event.generator.end_opportunity_simulation_event import EndOpportunitySimulationEvent
from pysocialsim.common.p2p.peer.context.opportunity.opportunity import Opportunity
import math

class StartOpportunitySimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "START_OPPORTUNITY")
    
    def execute(self):
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        simulator = simulation.getSimulator()
        scheduler = simulator.getScheduler()
        
        peers = network.getConnectedPeers(IPeerToPeerNetwork.SIMPLE_PEER)
        peer = peers[randint(0, len(peers) - 1)]
        
        contextManager = peer.getContextManager()
        
        opportunity = Opportunity(ContextIdGenerator.generateContextId(IContext.OPPORTUNITY, peer))
        
        contextManager.registerContext(IContext.OPPORTUNITY, opportunity)
        
        opportunity.activate()
        
        tagMap = TagsMap.getMap()
        
        numberOfConcepts = randint(1, len(tagMap))
        
        concepts = [c for c in tagMap.keys()]
        
        for i in range(numberOfConcepts):
            ix = randint(0, len(concepts) - 1)
            concept = concepts[ix]
            
            interest = Interest(concept)
            constraint = InterestConstraint(uniform(0.01, 1.0), interest)
            for j in range(len(tagMap[concept])):
                interest.registerTag(tagMap[concept][randint(0, len(tagMap[concept]) - 1)])
            
            opportunity.addInterestConstraint(constraint)
            
            concepts.remove(concept)
        
        opportunityMessage = AdvertiseOpportunityPeerToPeerMessage()
        opportunityMessage.registerParameter("opportunity", opportunity)
        
        peer.push(opportunityMessage)
        
        initialTime = scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId())
        
        joinTime = peer.getJoinTime()
        
        #endOpportunityTime = (1.5618*pow((-math.log(uniform(0,1))), 1/6.0013)) * 3600
        endOpportunityTime = 432000
        times = int((joinTime + endOpportunityTime) / 600)
        
        event = self.getSimulationEvent()
        event.setPeerId(peer.getId())
        
        opportunity.setStartTime(event.getPriority())
        opportunity.setDurationTime(endOpportunityTime)
        
        endOpportunityEvent = EndOpportunitySimulationEvent(peer.getId(), int(joinTime + endOpportunityTime))
        simulation.registerSimulationEvent(endOpportunityEvent)
        pushEvent = PushOpportunitySimulationEvent(peer.getId(), event.getPriority() + 600)
        pushEvent.registerParameter("opportunityId", opportunity.getId())
        
        simulation.registerSimulationEvent(pushEvent)
        
        simulator.startEventHandlingThread(pushEvent.getHandle())
        
        for i in range(2, times + 1):
            pushEvent = PushOpportunitySimulationEvent(peer.getId(), event.getPriority() + (600 * i))
            
            pushEvent.registerParameter("opportunityId", opportunity.getId())
            
            simulation.registerSimulationEvent(pushEvent)
        
        return AbstractSimulationEventHandler.execute(self)
        