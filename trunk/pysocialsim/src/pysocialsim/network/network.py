from pysocialsim.base.interface import Interface
from pysocialsim.simulator.simulation.event.event_generator import EventGenerator

class Network(EventGenerator):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getTopology(self):
        raise NotImplementedError()
    
    def getSimulation(self):
        raise NotImplementedError()
    
    def setSimulation(self, simulation):
        raise NotImplementedError()
    
    def countPeers(self):
        raise NotImplementedError()
    
    def addPeer(self, peer):
        raise NotImplementedError()
    
    def removePeer(self, id):
        raise NotImplementedError()
    
    def getPeer(self, id):
        raise NotImplementedError()
    
    def setEvolutionRate(self, evolutionRate):
        raise NotImplementedError()
    
    def getEvolutionRate(self):
        raise NotImplementedError()
    
    def dispatchMessage(self, message):
        raise NotImplementedError()
    
    def createConnection(self, sourceId, targetId):
        raise NotImplementedError()
    
    def removeConnection(self, sourceId, targetId):
        raise NotImplementedError()