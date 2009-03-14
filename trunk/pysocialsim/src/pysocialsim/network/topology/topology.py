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
    
    def show(self):
        raise NotImplementedError()
    
    def dispatchMessage(self, message):
        raise NotImplementedError()
    
    def createConnection(self, sourceId, targetId):
        raise NotImplementedError()
    
    def removeConnection(self, sourceId, targetId):
        raise NotImplementedError()