from pysocialsim.base.interface import Interface

class IP2PNetworkBuilder(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def createP2PNetwork(self, topology):
        raise NotImplementedError()
    
    def buildP2PNetwork(self, params):
        raise NotImplementedError()
    
    def getP2PNetwork(self):
        raise NotImplementedError()