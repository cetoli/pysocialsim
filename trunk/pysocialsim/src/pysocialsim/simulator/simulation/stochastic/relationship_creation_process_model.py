from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class RelationshipCreationProcessModel(Object):
    
    def __init__(self, peerRelationships, totalRelationships, entryTime):
        self.initialize(peerRelationships, totalRelationships, entryTime)
    
    def initialize(self, peerRelationships, totalRelationships, entryTime):
        self.__peerRelationships = peerRelationships
        self.__totalRelationships = totalRelationships
        self.__entryTime = entryTime
        self.__second = 0
        self.__generatedEvents = 0
        self.__element = 0
    
    @public
    def generateEvents(self, simulation):
        network = simulation.getP2PNetwork()
        self.__second += 1
        self.__generatedEvents = 0
        
        if network.countConnectedPeers() > 2:
            if self.__element == self.__totalRelationships:
                return self.__generatedEvents
            connectedPeers = network.getConnectedPeers()
            for id in connectedPeers:
                peer = network.getPeer(id)
                if self.__second % (peer.getConnectionTime() + self.__entryTime) == 0:
                    event = RelationshipCreationEvent(peer, simulation.getSimulationCurrentTime())
                    simulation.registerEvent(event)
                    self.__generatedEvents += 1
                    self.__element += 1
                if self.__element == self.__totalRelationships:
                    return self.__generatedEvents
        
        return self.__generatedEvents