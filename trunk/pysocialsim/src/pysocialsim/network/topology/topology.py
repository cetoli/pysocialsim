from pysocialsim.base.interface import Interface

class Topology(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def connect(self, peer):
        raise NotImplementedError()
    
    def disconnect(self, peer):
        raise NotImplementedError()
    
    def getNeighbors(self, id):
        raise NotImplementedError()
    
    def setNetwork(self, network):
        raise NotImplementedError()
    
    def getNetwork(self):
        raise NotImplementedError()
    
    def getGraph(self):
        raise NotImplementedError()