from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require
from pysocialsim.network.topology.topology import Topology
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.simulation.simulation import Simulation
from pysocialsim.network.peer.peer import Peer
from types import NoneType
import time

class AbstractNetwork(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None.__class__)
    @require("topology", Topology)
    def initialize(self, topology):
        self.__topology = topology
        self.__peers = {}
        self.__simulation = None
        self.__evolutionRate = 0
    
    @public
    @return_type(Topology)
    def getTopology(self):
        return self.__topology
    
    @public
    @return_type(int)
    @require("simulation", Simulation)
    def generateEvents(self, simulation):
        peers = 0
        day = 1
        while peers < len(self.__peers):
            for id in range(peers, (self.__evolutionRate * day) - 1):
                self.__peers[id].generateEvents(simulation)
                peers += 1
            day += 1
            peers += 1
            time.sleep(0.02592)
        return simulation.countEvents()
    
    @public
    @return_type(Simulation)
    def getSimulation(self):
        return self.__simulation
    
    @public
    @return_type(Simulation)
    @require("simulation", Simulation)
    def setSimulation(self, simulation):
        self.__simulation = simulation
        return self.__simulation
    
    @public
    @return_type(int)
    def countPeers(self):
        return len(self.__peers)
    
    @public
    @return_type(Peer)
    @require("peer", Peer)
    def addPeer(self, peer):
        if self.__peers.has_key(peer.getId()):
            return None
        self.__peers[peer.getId()] = peer
        return self.__peers[peer.getId()]
    
    @public
    @return_type(Peer)
    @require("id", int)
    def removePeer(self, id):
        if not self.__peers.has_key(id):
            return None
        peer = self.__peers[id]
        del self.__peers[id]
        return peer
    
    @public
    @return_type(Peer)
    @require("id", int)
    def getPeer(self, id):
        if not self.__peers.has_key(id):
            return None
        return self.__peers[id]
    
    @public
    @return_type(NoneType)
    def stop(self):
        for peer in self.__peers.values():
            peer.stop()
            
    @public
    @return_type(int)
    def setEvolutionRate(self, evolutionRate):
        self.__evolutionRate = evolutionRate
        return self.__evolutionRate
    
    @public
    @return_type(int)
    def getEvolutionRate(self):
        return self.__evolutionRate
    
    @public
    def dispatchMessage(self, message):
        pass