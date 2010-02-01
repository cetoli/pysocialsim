"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 25/01/2010
"""
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.message.acknowledge_compose_social_network_peer_to_peer_message import AcknowledgeComposeSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.message.peer_to_peer_message_id_generator import PeerToPeerMessageIdGenerator
from pysocialsim.common.p2p.peer.message.create_social_network_peer_to_peer_message import CreateSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.peer.message.update_social_network_peer_to_peer_message import UpdateSocialNetworkPeerToPeerMessage
from pysocialsim.common.p2p.peer.event.share_hardware_simulation_event import ShareHardwareSimulationEvent
from pysocialsim.common.p2p.topology.graph.i_node import INode
from pysocialsim.common.p2p.peer.context.opportunity.social_network_member import SocialNetworkMember

class ComposeSocialNetworkPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "COMPOSE_SOCIAL_NETWORK")
        
    def execute(self):
        message = self.getPeerToPeerMessage()
        peer = self.getPeer()
        message.registerPeerId(peer.getId())
        network = peer.getPeerToPeerNetwork()
        simulation = network.getSimulation()
        if peer.isJoined():
            
            if (float(peer.getSharedCapacity(INode.DISK)) / float(peer.getNodeDeviceCapacity(INode.DISK)) >= 1.0) and (float(peer.getSharedCapacity(INode.MEMORY)) / float(peer.getNodeDeviceCapacity(INode.MEMORY)) >= 1.0) and (float(peer.getSharedCapacity(INode.MEMORY)) / float(peer.getNodeDeviceCapacity(INode.MEMORY)) >= 1.0):
                print "PAREI DE COMPARTILHAR", self.getHandle()
                return
            
            contextManager = peer.getContextManager()
            if message.hasParameter("opportunityId"):
                if contextManager.hasContext(IContext.OPPORTUNITY, message.getParameter("opportunityId")):
                    opportunity = contextManager.getContext(IContext.OPPORTUNITY, message.getParameter("opportunityId"))
                    socialNetwork = opportunity.getSocialNetwork()
                    
                    if socialNetwork.hasSocialNetworkMember(message.getSourceId()):
                        return
                    
                    member = SocialNetworkMember(message.getSourceId())
                    socialNetwork.addSocialNetworkMember(member)
                    if not socialNetwork.hasSocialNetworkMember(peer.getId()):
                        member = SocialNetworkMember(peer.getId())
                        socialNetwork.addSocialNetworkMember(member)
                    
                    opportunity.setVersion(opportunity.getVersion() + 1)
                    opportunityClone = opportunity.clone()
                    
                    if opportunity.getVersion() == 2 and socialNetwork.countSocialNetworkMembers() == 2:
                        if peer.countNeighbors() > 0:
                            
                            neighbors = peer.getNeighbors()
                            for neighbor in neighbors:
                                createMessage = CreateSocialNetworkPeerToPeerMessage()
                                createMessage.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), neighbor.getId(), message.getTTL(), message.getPriority(), createMessage.getSize(), createMessage.getTime())
                                createMessage.registerParameter("opportunity", opportunityClone)
                                peer.send(createMessage)

                            if float(peer.getSharedCapacity(INode.DISK)) / float(peer.getNodeDeviceCapacity(INode.DISK)) < 1.0:
                                print "PERCENTAGE", float(peer.getSharedCapacity(INode.DISK)) / float(peer.getNodeDeviceCapacity(INode.DISK))
                                shareDiskEvent = ShareHardwareSimulationEvent(peer.getId(), message.getPriority() + 5)
                                shareDiskEvent.registerParameter("deviceType", INode.DISK)
                                shareDiskEvent.registerParameter("opportunityId", opportunity.getId())
                                simulation.registerSimulationEvent(shareDiskEvent)
                            else:
                                print "ACABOU DISK", peer.getId()
            
                            if float(peer.getSharedCapacity(INode.PROCESSOR)) / float(peer.getNodeDeviceCapacity(INode.PROCESSOR)) < 1.0:
                                shareProcessorEvent = ShareHardwareSimulationEvent(peer.getId(), message.getPriority() + 10)
                                shareProcessorEvent.registerParameter("deviceType", INode.PROCESSOR)
                                shareProcessorEvent.registerParameter("opportunityId", opportunity.getId())
                                simulation.registerSimulationEvent(shareProcessorEvent)
                            else:
                                print "ACABOU PROCESSOR", peer.getId()
                            
                            if float(peer.getSharedCapacity(INode.MEMORY)) / float(peer.getNodeDeviceCapacity(INode.MEMORY)) < 1.0:
                                shareMemoryEvent = ShareHardwareSimulationEvent(peer.getId(), message.getPriority() + 15)
                                shareMemoryEvent.registerParameter("deviceType", INode.MEMORY)
                                shareMemoryEvent.registerParameter("opportunityId", opportunity.getId())
                                simulation.registerSimulationEvent(shareMemoryEvent)
                            else:
                                print "ACABOU MEMORY", peer.getId()

                    elif opportunity.getVersion() > 2 and socialNetwork.countSocialNetworkMembers() > 2:
                        if peer.countNeighbors() > 0:
                            neighbors = peer.getNeighbors()
                            for neighbor in neighbors:
                                updateMessage = UpdateSocialNetworkPeerToPeerMessage()
                                updateMessage.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), neighbor.getId(), message.getTTL(), message.getPriority(), updateMessage.getSize(), updateMessage.getTime())
                                updateMessage.registerParameter("opportunity", opportunityClone)
                                peer.send(updateMessage)
                    
                    ack_message = AcknowledgeComposeSocialNetworkPeerToPeerMessage()
                    ack_message.init(PeerToPeerMessageIdGenerator.generatePeerToPeerMessageId(peer), peer.getId(), message.getSourceId(), message.getTTL(), message.getPriority(), ack_message.getSize(), ack_message.getTime())
                    
                    ack_message.registerParameter("opportunity", opportunityClone)
                    
                    peer.send(ack_message)
                