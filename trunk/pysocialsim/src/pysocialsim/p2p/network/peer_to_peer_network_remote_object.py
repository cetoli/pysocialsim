"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/04/2010
"""
from pysocialsim.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from Pyro.core import ObjBase
from threading import Semaphore

class PeerToPeerNetworkRemoteObject(IPeerToPeerNetwork, ObjBase):
    
    def __init__(self):
        ObjBase.__init__(self)
        self.initialize()
        
    def initialize(self):
        self.__peers = {IPeerToPeerNetwork.SUPER_PEER: {}, IPeerToPeerNetwork.SIMPLE_PEER: {}}
        self.__connectionsBetweenSuperPeers = 0
        self.__peerToPeerProtocols = {}
        self.__connectionsBetweenSuperPeerAndSimplePeers = 0
        self.__connectionsBetweenSimplePeerAndSuperPeers = 0
        self.__linkAvailability = 0
        self.__superPeerLink = 0
        self.__simplePeerLink = 0
        self.__sizesOfDisk = []
        self.__sizesOfMemory = []
        self.__diskAvailability = 0
        self.__memoryAvailability = 0
        self.__processorAvailability = 0
        self.__processorClocks = []
        self.__peerAvailabilities = {IPeerToPeerNetwork.SUPER_PEER: 0, IPeerToPeerNetwork.SIMPLE_PEER : 0}
        self.__connectedPeers = {IPeerToPeerNetwork.SUPER_PEER: {}, IPeerToPeerNetwork.SIMPLE_PEER : {}}
        
    def getSimulation(self):
        raise NotImplementedError()
    
    def setSimulation(self, simulation):
        raise NotImplementedError()
    
    def addPeer(self, peerType, peerId):
        sem = Semaphore()
        sem.acquire()
        self.__peers[peerType][peerId] = "PYRONAME://"+peerId
        sem.release()
    
    def removePeer(self, peerType, peerId):
        sem = Semaphore()
        sem.acquire()
        del self.__peers[peerType][peerId]
        sem.release()
    
    def getPeer(self, peerType, peerId):
        sem = Semaphore()
        sem.acquire()
        peer = self.__peers[peerType][peerId]
        sem.release()
        return peer
    
    def getPeers(self, peerType):
        sem = Semaphore()
        sem.acquire()
        peers = self.__peers[peerType].values()
        sem.release()
    
    def countPeers(self, peerType):
        sem = Semaphore()
        sem.acquire()
        peers = len(self.__peers[peerType])
        sem.release()
        return peers
    
    def getConnectedPeers(self, peerType):
        sem = Semaphore()
        sem.acquire()
        peers = self.__connectedPeers[peerType].values()
        sem.release()
        return peers
    
    def getDisconnectedPeers(self, peerType):
        raise NotImplementedError()
    
    def setConnectionsBetweenSuperPeers(self, numberOfConnections):
        self.__connectionsBetweenSuperPeers = numberOfConnections
    
    def getConnectionsBetweenSuperPeers(self):
        return self.__connectionsBetweenSuperPeers
    
    def registerPeerToPeerProtocol(self, peerType, peerToPeerProtocol):
        raise NotImplementedError()
    
    def unregisterPeerToPeerProtocol(self, peerType):
        raise NotImplementedError()
    
    def getPeerToPeerProtocol(self, peerType):
        raise NotImplementedError()
    
    def hasPeer(self, peerType, peerId):
        sem = Semaphore()
        sem.acquire()
        res = self.__peers[peerType].has_key()
        sem.release()
        return res
    
    def setConnectionsBetweenSuperPeerAndSimplePeers(self, superPeerAndSimplePeers):
        self.__connectionsBetweenSuperPeerAndSimplePeers = superPeerAndSimplePeers
    
    def getConnectionsBetweenSuperPeerAndSimplePeers(self):
        return self.__connectionsBetweenSuperPeerAndSimplePeers
    
    def setConnectionsBetweenSimplePeerAndSuperPeers(self, simplePeerAndSuperPeers):
        self.__connectionsBetweenSimplePeerAndSuperPeers = simplePeerAndSuperPeers
    
    def getConnectionsBetweenSimplePeerAndSuperPeers(self):
        return self.__connectionsBetweenSimplePeerAndSuperPeers
    
    def setLinkAvailability(self, availability):
        self.__linkAvailability = availability
    
    def getLinkAvailability(self):
        return self.__linkAvailability
    
    def setSuperPeerLink(self, superPeerLink):
        self.__superPeerLink = superPeerLink
    
    def getSuperPeerLink(self):
        return self.__superPeerLink
    
    def setSimplePeerLink(self, simplePeerLink):
        self.__simplePeerLink = simplePeerLink
    
    def getSimplePeerLink(self):
        return self.__simplePeerLink
    
    def registerSizeOfDisk(self, sizeOfDisk):
        self.__sizesOfDisk.append(sizeOfDisk)
    
    def unregisterSizeDisk(self, sizeOfDisk):
        self.__sizesOfDisk.remove(sizeOfDisk)
    
    def getSizesOfDisk(self):
        return [] + self.__sizesOfDisk
    
    def countSizesOfDisk(self):
        return len(self.__sizesOfDisk)
    
    def setDiskAvailability(self, availability):
        self.__diskAvailability = availability
    
    def getDiskAvailability(self):
        return self.__diskAvailability
    
    def setMemoryAvailability(self, availability):
        self.__memoryAvailability = availability
    
    def getMemoryAvailability(self):
        return self.__memoryAvailability
    
    def registerSizeOfMemory(self, sizeOfMemory):
        self.__sizesOfMemory.append(sizeOfMemory)
    
    def unregisterSizeMemory(self, sizeOfMemory):
        self.__sizesOfMemory.remove(sizeOfMemory)
    
    def getSizesOfMemory(self):
        return self.__sizesOfMemory
    
    def countSizesOfMemory(self):
        return len(self.__sizesOfMemory)
    
    def registerProcessorClock(self, clock):
        self.__processorClocks.append(clock)
    
    def unregisterProcessorClock(self, clock):
        self.__processorClocks.remove(clock)
    
    def getProcessorClocks(self):
        return [] + self.__processorClocks
    
    def countProcessorClocks(self):
        return len(self.__processorClocks)
    
    def setProcessorAvailability(self, availability):
        self.__processorAvailability = availability
    
    def getProcessorAvailability(self):
        return self.__processorAvailability
    
    def registerConnectedPeer(self, type, peerId):
        self.__connectedPeers[type].append(peerId)
    
    def unregisterConnectedPeer(self, type, peerId):
        self.__connectedPeers[type].remove(peerId)
    
    def countConnectedPeers(self, type):
        return len(self.__connectedPeers[type])
    
