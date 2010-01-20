from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.context.tags_map import TagsMap
from random import randint, uniform
from pysocialsim.common.p2p.peer.profile.interest import Interest
from pysocialsim.common.p2p.peer.context.interest_constraint import InterestConstraint
from pysocialsim.common.p2p.peer.message.advertise_opportunity_peer_to_peer_message import AdvertiseOpportunityPeerToPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator

class StartOpportunitySimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "START_OPPORTUNITY")
    
    def execute(self):
        event = self.getSimulationEvent()
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        
        peer = network.getPeer(IPeerToPeerNetwork.SIMPLE_PEER, event.getPeerId())
        
        contextManager = peer.getContextManager()
        opportunity = contextManager.getContext(IContext.OPPORTUNITY, event.getParameter("opportunityId"))
        
        opportunity.activate()
        
        tagMap = TagsMap.getMap()
        
        issue = tagMap[tagMap.keys()[randint(0, len(tagMap.keys()) - 1)]]
        
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
            
        return AbstractSimulationEventHandler.execute(self)
        