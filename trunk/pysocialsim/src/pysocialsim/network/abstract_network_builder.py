from pysocialsim.base.decorator.public import public
from pysocialsim.base.object import Object

class AbstractNetworkBuilder(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def setNetwork(self, network):
        self.__network = network
        
    def setProtocol(self, protocol):
        self.__protocol = protocol
    
    @public    
    def buildNetwork(self, **params):
        raise NotImplementedError()
    
    @public
    def createNetwork(self, topology, protocol):
        raise NotImplementedError()
    
    @public
    def getNetwork(self):
        return self.__network
    
    @public
    def getProtocol(self):
        return self.__protocol