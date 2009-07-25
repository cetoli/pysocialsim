from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.event.content_sharing_event import ContentSharingEvent

class ContentSharingProcessModel(Object):
    
    def __init__(self, contentsForSharing, totalContents, entryTime):
        self.initialize(contentsForSharing, totalContents, entryTime)
    
    def initialize(self, contentsForSharing, totalContents, entryTime):
        self.__contentsForSharing = contentsForSharing
        self.__totalContents = totalContents
        self.__entryTime = entryTime
        self.__second = 0
        self.__generatedEvents = 0
        self.__element = 0
        
    @public
    def generateEvents(self, simulation):
        network = simulation.getP2PNetwork()
        self.__second += 1
        self.__generatedEvents = 0
        if network.countConnectedPeers() >= 2:
            if self.__element == self.__totalContents:
                return self.__generatedEvents
            connectedPeers = network.getConnectedPeers()
            for id in connectedPeers:
                peer = network.getPeer(id)
                if peer.countContents() == (self.__totalContents / network.countPeers()):
                    continue
                if self.__second % (peer.getConnectionTime() + self.__entryTime) == 0:
                    event = ContentSharingEvent(peer, simulation.getSimulationCurrentTime())
                    simulation.registerEvent(event)
                    self.__generatedEvents += 1
                    self.__element += 1
                if self.__element == self.__totalContents:
                    return self.__generatedEvents
        return self.__generatedEvents
                    