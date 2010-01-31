'''
Created on 31/01/2010

@author: fabricio
'''
from pysocialsim.common.p2p.topology.graph.i_node import INode
from pysocialsim.common.p2p.peer.context.sharing.abstract_hardware_sharing_context_information import AbstractHardwareSharingContextInformation

class MemorySharingContextInformation(AbstractHardwareSharingContextInformation):
    
    def __init__(self, id, capacity, usedCapacity, freeCapacity, peerId):
        self.initialize(id, INode.MEMORY, capacity, usedCapacity, freeCapacity, peerId)