'''
Created on 31/01/2010

@author: fabricio
'''
from pysocialsim.common.p2p.topology.graph.i_node import INode
import sha

class HardwareSharingIdGenerator(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @classmethod
    def generateId(self, peer, opportunity, nodeDeviceType):
        id = "urn:"
        
        if nodeDeviceType == INode.DISK:
            id += "disk:sharing:id:" + sha.new(peer.getId() + opportunity.getId() + str(nodeDeviceType)).hexdigest()
        elif nodeDeviceType == INode.MEMORY:
            id += "memory:sharing:id:" + sha.new(peer.getId() + opportunity.getId() + str(nodeDeviceType)).hexdigest()
        elif nodeDeviceType == INode.PROCESSOR:
            id += "processor:sharing:id:" + sha.new(peer.getId() + opportunity.getId() + str(nodeDeviceType)).hexdigest()
            
        return id
        