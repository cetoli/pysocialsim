"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 26/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.event.share_hardware_simulation_event import ShareHardwareSimulationEvent
from pysocialsim.common.p2p.topology.graph.i_node import INode
from pysocialsim.common.p2p.peer.context.opportunity.social_network_member import SocialNetworkMember
from pysocialsim.common.p2p.peer.message.create_social_network_peer_to_peer_message import CreateSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator

class AcknowledgeComposeSocialNetworkPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "ACK_COMPOSE_SOCIAL_NETWORK")
    
    def execute(self):
        peer = self.getPeer()
        network = peer.getPeerToPeerNetwork()
        simulation = network.getSimulation()
        if peer.isJoined():
            
            if (float(peer.getSharedCapacity(INode.DISK)) / float(peer.getNodeDeviceCapacity(INode.DISK)) >= 1.0) and (float(peer.getSharedCapacity(INode.MEMORY)) / float(peer.getNodeDeviceCapacity(INode.MEMORY)) >= 1.0) and (float(peer.getSharedCapacity(INode.MEMORY)) / float(peer.getNodeDeviceCapacity(INode.MEMORY)) >= 1.0):
                return
            
            message = self.getPeerToPeerMessage()
            message.registerPeerId(peer.getId())
            if message.hasParameter("opportunity"):
                opportunity = message.getParameter("opportunity")
                socialNetwork = opportunity.getSocialNetwork()
                
                member = SocialNetworkMember(message.getSourceId())
                
                socialNetwork.addSocialNetworkMember(member)
                
                contextManager = peer.getContextManager()
                
                contextManager.registerContext(IContext.OPPORTUNITY, opportunity)
                
                if float(peer.getSharedCapacity(INode.DISK)) / float(peer.getNodeDeviceCapacity(INode.DISK)) < 0.9:
                    shareDiskEvent = ShareHardwareSimulationEvent(peer.getId(), message.getPriority() + 5)
                    shareDiskEvent.registerParameter("deviceType", INode.DISK)
                    shareDiskEvent.registerParameter("opportunityId", opportunity.getId())
                    simulation.registerSimulationEvent(shareDiskEvent)
#                
                if float(peer.getSharedCapacity(INode.PROCESSOR)) / float(peer.getNodeDeviceCapacity(INode.PROCESSOR)) < 0.9:
                    shareProcessorEvent = ShareHardwareSimulationEvent(peer.getId(), message.getPriority() + 10)
                    shareProcessorEvent.registerParameter("deviceType", INode.PROCESSOR)
                    shareProcessorEvent.registerParameter("opportunityId", opportunity.getId())
                    simulation.registerSimulationEvent(shareProcessorEvent)
                
                if float(peer.getSharedCapacity(INode.MEMORY)) / float(peer.getNodeDeviceCapacity(INode.MEMORY)) < 0.9:
                    shareMemoryEvent = ShareHardwareSimulationEvent(peer.getId(), message.getPriority() + 15)
                    shareMemoryEvent.registerParameter("deviceType", INode.MEMORY)
                    shareMemoryEvent.registerParameter("opportunityId", opportunity.getId())
                    simulation.registerSimulationEvent(shareMemoryEvent)
#                
#                