from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.context.tags_map import TagsMap
from random import randint

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
        
        issue = tagMap[tagMap.keys()[randint(0, len(tagMap.keys()))]]
        
        initial = randint(0, len(issue)/2)
        final = randint(len(issue)/2, len(issue))
        
        for tag in issue[initial:final]:
            opportunity.registerTag(tag)
            
        
        
        