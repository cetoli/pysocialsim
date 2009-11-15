"""
Defines the module with the specification of INode class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 19/09/2009
"""

class INode(object):
    
    PROCESSOR = 0
    DISK = 1
    NETWORK_ADAPTER = 2
    
    def __init__(self):
        raise NotImplementedError()
    
    def getId(self):
        raise NotImplementedError()
    
    def addNodeDevice(self, nodeDevice):
        raise NotImplementedError()
    
    def removeNodeDevice(self, nodeDevice):
        raise NotImplementedError()
    
    def getNodeDevice(self, nodeDeviceType):
        raise NotImplementedError()
    
    def getNodeDevices(self):
        raise NotImplementedError()
    
    def countNodeDevices(self):
        raise NotImplementedError()
    
    def getPeerToPeerTopology(self):
        raise NotImplementedError()
    
    def input(self, nodeDeviceType, data):
        raise NotImplementedError()
    
    def output(self, nodeDeviceType, data):
        raise NotImplementedError()
    
    def addEdge(self, edge):
        raise NotImplementedError()
    
    def removeEdge(self, edge):
        raise NotImplementedError()
    
    def getEdge(self, targetNodeId):
        raise NotImplementedError()
    
    def getEdges(self):
        raise NotImplementedError()
    
    def countEdges(self):
        raise NotImplementedError()
    
    def hasEdge(self, targetNodeId):
        raise NotImplementedError()
    
    def setPeer(self, peer):
        raise NotImplementedError()
    
    def getPeer(self):
        raise NotImplementedError()