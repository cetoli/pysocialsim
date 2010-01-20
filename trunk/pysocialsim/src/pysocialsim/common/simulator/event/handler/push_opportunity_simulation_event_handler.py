from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.message.advertise_opportunity_peer_to_peer_message import AdvertiseOpportunityPeerToPeerMessage

class PushOpportunitySimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "PUSH_OPPORTUNITY")
    
    def execute(self):
        event = self.getSimulationEvent()
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        
        peer = network.getPeer(IPeerToPeerNetwork.SIMPLE_PEER, event.getPeerId())
        
        contextManager = peer.getContextManager()
        
        opportunity = contextManager.getContext(IContext.OPPORTUNITY, event.getParameter("opportunityId"))
        
        opportunityMessage = AdvertiseOpportunityPeerToPeerMessage()
        opportunityMessage.registerParameter("opportunity", opportunity)
        
        peer.push(opportunityMessage)
        
        return AbstractSimulationEventHandler.execute(self)