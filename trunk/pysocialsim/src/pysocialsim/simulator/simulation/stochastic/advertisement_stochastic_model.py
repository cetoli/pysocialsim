from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.event.content_advertisement_event import ContentAdvertisementEvent

class AdvertisementStochasticModel(object):
    
    def __init__(self, peers, totalElements, entryRate, permanenceRate):
        self.initialize(peers, totalElements, entryRate, permanenceRate)
    
    def initialize(self, peers, totalElements, entryRate, permanenceRate):
        self.__entryRate = entryRate
        self.__permanenceRate = permanenceRate
        self.__peers = peers
        self.__totalElements = totalElements
        self.__generatedEvents = 0
        self.__second = 0
    
    @public
    def generateEvents(self, simulation):
        network = simulation.getP2PNetwork()
        self.__second += 1
        if network.countConnectedPeers() > 1:
            if self.__second % self.__entryRate.getTime() == 0:
                connectedPeers = network.getConnectedPeers()
                for p in connectedPeers:
                    peer = network.getPeer(p)
                    if peer.countContents() > 0:
                        event = ContentAdvertisementEvent(peer, simulation.getSimulationCurrentTime())
                        simulation.registerEvent(event)
                        self.__generatedEvents += 1
                    

        
        return self.__generatedEvents