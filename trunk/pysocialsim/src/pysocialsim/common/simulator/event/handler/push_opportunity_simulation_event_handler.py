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
        
        if not event.hasParameter("opportunityId"):
            return AbstractSimulationEventHandler.execute(self)
        
        opportunity = contextManager.getContext(IContext.OPPORTUNITY, event.getParameter("opportunityId"))
        socialNetwork = opportunity.getSocialNetwork()
        
        if socialNetwork.countSocialNetworkMembers() == 0:
            if peer.isJoined():
                opportunityMessage = AdvertiseOpportunityPeerToPeerMessage()
                opportunityMessage.registerParameter("opportunity", opportunity)
                
                peer.push(opportunityMessage)
                print "FOI PUBLICADA"
        else:
            for member in socialNetwork.getSocialNetworkMembers():
                peer = network.getPeer(IPeerToPeerNetwork.SIMPLE_PEER, member.getId())
                if peer.isJoined():
                    opportunityMessage = AdvertiseOpportunityPeerToPeerMessage()
                    opportunityMessage.registerParameter("opportunity", opportunity)
                    
                    peer.push(opportunityMessage)
                    print "TEM MAIS GENTE PUBLICANDO"
        
        return AbstractSimulationEventHandler.execute(self)