"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/04/2010
"""
from pysocialsim.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from Pyro.core import getProxyForURI

class PeerToPeerNetwork(IPeerToPeerNetwork):
    
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        self.__simulation = None
        self.__network = getProxyForURI("PYRONAME://network")
        self.__peerToPeerProtocols = {}
        
    def getSimulation(self):
        return self.__simulation
    
    def setSimulation(self, simulation):
        self.__simulation = simulation
        self.__simulation.setPeerToPeerNetwork(self)
    
    def addPeer(self, peerType, peerId):
        self.__network.addPeer(peerType, peerId)
    
    def removePeer(self, peerType, peerId):
        self.__network.removerPeer(peerType, peerId)
    
    def getPeer(self, peerType, peerId):
        return self.__network.getPeer(peerType, peerId)
    
    def getPeers(self, peerType):
        return self.__network.getPeers()
    
    def countPeers(self, peerType):
        return self.__network.countPeers(peerType)
    
    def getConnectedPeers(self, peerType):
        return self.__network.getConnectedPeers(peerType)
    
    def getDisconnectedPeers(self, peerType):
        return self.__network.getDisconnectedPeers(peerType)
    
    def setConnectionsBetweenSuperPeers(self, numberOfConnections):
        return self.__network.setConnectionsBetweenSuperPeers(numberOfConnections)
    
    def getConnectionsBetweenSuperPeers(self):
        return self.__network.getConnectionsBetweenSuperPeers()
    
    def registerPeerToPeerProtocol(self, peerType, peerToPeerProtocol):
        self.__peerToPeerProtocols[peerType] = peerToPeerProtocol
    
    def unregisterPeerToPeerProtocol(self, peerType):
        del self.__peerToPeerProtocols[peerType]
    
    def getPeerToPeerProtocol(self, peerType):
        return self.__peerToPeerProtocols[peerType]
    
    def hasPeer(self, peerType, peerId):
        return self.__network.hasPeer(peerType, peerId)
    
    def setConnectionsBetweenSuperPeerAndSimplePeers(self, superPeerAndSimplePeers):
        self.__network.setConnectionsBetweenSuperPeerAndSimplePeers(superPeerAndSimplePeers)
    
    def getConnectionsBetweenSuperPeerAndSimplePeers(self):
        self.__network.getConnectionsBetweenSuperPeerAndSimplePeers()
    
    def setConnectionsBetweenSimplePeerAndSuperPeers(self, simplePeerAndSuperPeers):
        self.__network.setConnectionsBetweenSimplePeerAndSuperPeers(simplePeerAndSuperPeers)
    
    def getConnectionsBetweenSimplePeerAndSuperPeers(self):
        return self.__network.getConnectionsBetweenSimplePeerAndSuperPeers(self)
    
    def setLinkAvailability(self, availability):
        self.__network.setLinkAvailability(availability)
    
    def getLinkAvailability(self):
        return self.__network.getLinkAvailability(self)
    
    def setSuperPeerLink(self, superPeerLink):
        self.__network.setSuperPeerLink(superPeerLink)
    
    def getSuperPeerLink(self):
        return self.__network.getSuperPeerLink()
    
    def setSimplePeerLink(self, simplePeerLink):
        self.__network.setSimplePeerLink(simplePeerLink)
    
    def getSimplePeerLink(self):
        return self.__network.getSimplePeerLink()
    
    def registerSizeOfDisk(self, sizeOfDisk):
        self.__network.registerSizeOfDisk(sizeOfDisk)
    
    def unregisterSizeDisk(self, sizeOfDisk):
        self.__network.unregisterSizeOfDisk(sizeOfDisk)
    
    def getSizesOfDisk(self):
        return self.__network.getSizesOfDisk()
    
    def countSizesOfDisk(self):
        return self.__network.countSizesOfDisk()
    
    def setDiskAvailability(self, availability):
        self.__network.setDiskAvailability(availability)
    
    def getDiskAvailability(self):
        return self.__network.getDiskAvailability()
    
    def setMemoryAvailability(self, availability):
        self.__network.setMemoryAvailability(availability)
    
    def getMemoryAvailability(self):
        return self.__network.getMemoryAvailability(self)
    
    def registerSizeOfMemory(self, sizeOfMemory):
        self.__network.registerSizeOfMemory(sizeOfMemory)
    
    def unregisterSizeMemory(self, sizeOfMemory):
        self.__network.unregisterSizeMemory(sizeOfMemory)
    
    def getSizesOfMemory(self):
        return self.__network.getSizesOfMemory()
    
    def countSizesOfMemory(self):
        return self.__network.countSizesOfMemory()
    
    def registerProcessorClock(self, clock):
        self.__network.registerProcessorClock(clock)
    
    def unregisterProcessorClock(self, clock):
        self.__network.unregisterProcessorClock(clock)
    
    def getProcessorClocks(self):
        return self.__network.getProcessorClocks()
    
    def countProcessorClocks(self):
        return self.__network.countProcessorClocks()
    
    def setProcessorAvailability(self, availability):
        self.__network.setProcessorAvailability(availability)
    
    def getProcessorAvailability(self):
        return self.__network.getProcessorAvailability()
    
    def setPeerAvailability(self, type, availability):
        self.__network.setPeerAvailability(type, availability)
    
    def getPeerAvailability(self, type):
        return self.__network.getPeerAvailability(type)
    
    def registerConnectedPeer(self, type, peerId):
        self.__network.registerConnectedPeer(type, peerId)
    
    def unregisterConnectedPeer(self, type, peerId):
        self.__network.unregisterConnectedPeer(type, peerId)
    
    def countConnectedPeers(self, type):
        return self.__network.countConnectedPeers(type)
    
        
