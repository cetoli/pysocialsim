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
        
        if peer.isJoined():
        
            contextManager = peer.getContextManager()
            
            if not event.hasParameter("opportunityId"):
                return AbstractSimulationEventHandler.execute(self)
            
            opportunity = contextManager.getContext(IContext.OPPORTUNITY, event.getParameter("opportunityId"))
            
            opportunityMessage = AdvertiseOpportunityPeerToPeerMessage()
            opportunityMessage.registerParameter("opportunity", opportunity)
            
            peer.push(opportunityMessage)
        
        else:
            print 8888888888888888888888888888888888888888888888888888888888888888888888
        
        return AbstractSimulationEventHandler.execute(self)