'''
Created on 02/02/2010

@author: fabricio
'''

from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.topology.graph.i_node import INode

class RequestStorageAgreementPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "REQUEST_STORAGE_AGREEMENT")
        
    def execute(self):
        peer = self.getPeer()
        if not peer.isJoined():
            return
        
        message = self.getPeerToPeerMessage()
        if not message.hasParameter("contentSize"):
            return
        
        if not message.hasParameter("opportunityId"):
            return
        
        contextManager = peer.getContextManager()        
        if not contextManager.hasContext(IContext.OPPORTUNITY, message.getParameter("opportunityId")):
            return
        
        opportunity = contextManager.getContext(IContext.OPPORTUNITY, message.getParameter("opportunityId"))
        socialNetwork = opportunity.getSocialNetwork()
        socialNetworkMember = socialNetwork.getSocialNetworkMember(peer.getId())
        
        hardwareSharings = socialNetworkMember.getHardwareSharings(INode.DISK)
        
        print "COMPARTILHAMENTOS", hardwareSharings
        
        if len(hardwareSharings) == 1:
            
            print 22222222222222222222222222222222222222222222222222
            
            diskSharingInformation = hardwareSharings[0]
            
            diskSharing = peer.getHardwareSharing(diskSharingInformation.getNodeDeviceType(), diskSharingInformation.getId())
            
            if message.getParameter("contentSize") > diskSharing.getFreeCapacity():
                return
            
            
        
            
            