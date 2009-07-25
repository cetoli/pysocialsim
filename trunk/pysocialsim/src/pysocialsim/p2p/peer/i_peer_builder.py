from pysocialsim.base.interface import Interface

class IPeerBuilder(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def createPeer(self, id, network, protocol, matchingStrategy):
        raise NotImplementedError()
    
    def buildContent(self, params):
        raise NotImplementedError()
    
    def getPeer(self):
        raise NotImplementedError()
    
    def setPeerBuilderDirector(self, director):
        raise NotImplementedError()