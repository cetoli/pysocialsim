from pysocialsim.base.decorator.public import public
from pysocialsim.base.object import Object

class AbstractNetworkBuilder(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def setNetwork(self, network):
        self.__network = network
    
    @public    
    def buildNetwork(self, **params):
        raise NotImplementedError()
    
    @public
    def createNetwork(self, topology):
        raise NotImplementedError()
    
    @public
    def getNetwork(self):
        return self.__network