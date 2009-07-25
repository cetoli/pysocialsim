from pysocialsim.p2p.peer.abstract_peer import AbstractPeer
from pysocialsim.p2p.profile.default_profile import DefaultProfile
from threading import Thread
from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.folksonomy.folksonomy_map import FolksonomyMap
from random import randint
from pysocialsim.p2p.peer.i_peer import IPeer
from pysocialsim.p2p.profile.default_interest import DefaultInterest
from pysocialsim.simulator.event.peer_disconnection_event import PeerDisconnectionEvent

class DefaultPeer(AbstractPeer):
    
    def __init__(self, id, network, protocol, matchingStrategy):
        self.initialize(id, network, protocol, matchingStrategy)
        
    def initialize(self, id, network, protocol, matchingStrategy):
        AbstractPeer.initialize(self, id, network, protocol, matchingStrategy)
        profile = DefaultProfile(self)
        self.setProfile(profile)
        
        map = FolksonomyMap()
        
        #for concept in map.mapping.keys():            
        concept = map.mapping.keys()[randint(0, len(map.mapping.keys()) - 1)]
        initial = randint(0, (len(map.mapping[concept])/2) - 1)
        end = randint((len(map.mapping[concept])/2), len(map.mapping[concept]) - 1)
            
        for ix in range(initial, end):
            profile.addFolksonomy(map.mapping[concept][ix])
    
    @public
    def specifyInterest(self):
        initialThreshold = randint(1, 50)
        limitThreshold = randint(50, 100)
        
        profile = self.getProfile()
        
        first = randint(0, (len(profile.getFolksonomies()) - 1)/2)
        last =  randint((len(profile.getFolksonomies()))/2, len(profile.getFolksonomies()))
        
        
        print "HAH", first, last
        folksonomies = []
        
        for i in range(first, last):
            folksonomies.append(profile.getFolksonomies().keys()[i])
        
        interest = DefaultInterest(0, initialThreshold, limitThreshold, folksonomies)
        
        profile.addInterest(interest)
        
    @public
    def connect(self, priority):
        AbstractPeer.connect(self, priority)
        DefaultPeer.PeerThread(self).start()
        
    class PeerThread(Thread):
        
        def __init__(self, peer):
            Thread.__init__(self)
            self.__peer = peer
            
        def run(self):
            while True:
                network = self.__peer.getP2PNetwork()
                simulation = network.getSimulation()
                if self.__peer.countContents() > 0 and simulation.getSimulationCurrentTime() % 10 == 0:
                    if not self.__peer.getScheduledForDisconnection():
                        self.__peer.advertise(IPeer.CONTENT_ADVERTISEMENT)
                
                    if (self.__peer.getDisconnectionTime() + self.__peer.getConnectionTime()) == simulation.getSimulationCurrentTime():
                        print self.__peer.getId(), "DISCONECTOU", self.__peer.getDisconnectionTime()
                        event = PeerDisconnectionEvent(self.__peer, simulation.getSimulationCurrentTime())
                        self.__peer.setScheduledForDisconnection(True)
                        simulation.registerEvent(event)
                        return
                
                    
                    
        
    
        