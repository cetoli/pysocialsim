from pysocialsim.base.interface import Interface

class NetworkBuilder(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def buildNetwork(self, **params):
        raise NotImplementedError()
    
    def createNetwork(self, topology, protocol):
        raise NotImplementedError()
    
    def getNetwork(self):
        raise NotImplementedError()
    
    def getProtocol(self):
        raise NotImplementedError()