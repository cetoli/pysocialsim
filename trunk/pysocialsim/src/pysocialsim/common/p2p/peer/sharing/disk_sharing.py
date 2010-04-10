'''
Created on 31/01/2010

@author: fabricio
'''
from pysocialsim.common.p2p.peer.sharing.abstract_hardware_sharing import AbstractHardwareSharing
from pysocialsim.common.p2p.topology.graph.i_node import INode
from pysocialsim.common.p2p.peer.context.sharing.disk_sharing_context_information import DiskSharingContextInformation
from pysocialsim.common.base.decorators import public

class DiskSharing (AbstractHardwareSharing):
    
    def __init__(self, id, peer, capacity):
        self.initialize(id, peer, capacity)
    
    def initialize(self, id, peer, capacity):
        AbstractHardwareSharing.initialize(self, id, peer, capacity, INode.DISK)

    @public
    def getContext(self):
        return DiskSharingContextInformation(self.getId(), self.getCapacity(), self.getUsedCapacity(), self.getUsedCapacity(), self.getPeer().getId())

        
    