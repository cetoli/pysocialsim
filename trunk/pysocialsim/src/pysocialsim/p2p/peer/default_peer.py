from pysocialsim.p2p.peer.abstract_peer import AbstractPeer
from pysocialsim.p2p.profile.default_profile import DefaultProfile
from threading import Thread
from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.folksonomy.folksonomy_map import FolksonomyMap
from random import randint
from pysocialsim.p2p.peer.i_peer import IPeer
from pysocialsim.p2p.profile.default_interest import DefaultInterest
from pysocialsim.simulator.event.peer_disconnection_event import PeerDisconnectionEvent
from pysocialsim.simulator.event.interest_specification_event import InterestSpecificationEvent
from pysocialsim.simulator.event.content_sharing_event import ContentSharingEvent
from pysocialsim.simulator.event.social_cloud_creation_event import SocialCloudCreationEvent
from pysocialsim.p2p.dispatcher.relationship.invite_create_social_cloud_message_handler import InviteCreateSocialCloudMessageHandler
import time

class DefaultPeer(AbstractPeer):
    
    def __init__(self, id, network, protocol, matchingStrategy):
        self.initialize(id, network, protocol, matchingStrategy)
        
    def initialize(self, id, network, protocol, matchingStrategy):
        AbstractPeer.initialize(self, id, network, protocol, matchingStrategy)
        profile = DefaultProfile(self)
        self.setProfile(profile)
        
        map = FolksonomyMap()
        
        concept = map.mapping.keys()[randint(0, len(map.mapping.keys()) - 1)]
        initial = randint(0, (len(map.mapping[concept])/2) - 1)
        end = randint((len(map.mapping[concept])/2), len(map.mapping[concept]) - 1)
            
        for ix in range(initial, end):
            profile.addFolksonomy(map.mapping[concept][ix])
            
        dispatcher = self.getMessageDispatcher()
        dispatcher.registerMessageHandler(InviteCreateSocialCloudMessageHandler(self))
        
        
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
            interestTime = 0
            contentSharingTime = 0
            cloudCreationTime = 0
            relationships = 0
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
                
                profile = self.__peer.getProfile()
                if (interestTime == 190) and (profile.countInterests() <= 60):
                    if network.countConnectedPeers() > 2:
                        interestTime = 0
                        event = InterestSpecificationEvent(self.__peer, simulation.getSimulationCurrentTime())
                        simulation.registerEvent(event)
                
                if (contentSharingTime == 360) and (self.__peer.countContents() <= 20):
                    if network.countConnectedPeers() > 2:
                        contentSharingTime = 0
                        event = ContentSharingEvent(self.__peer, simulation.getSimulationCurrentTime())
                        simulation.registerEvent(event)
                        
                if (cloudCreationTime == 200):
                    if network.countConnectedPeers() > 2:
                        cloudCreationTime = 0
                        event = SocialCloudCreationEvent(self.__peer, simulation.getSimulationCurrentTime())
                        simulation.registerEvent(event)
                
                interestTime += 1
                contentSharingTime += 1
                cloudCreationTime += 1
                time.sleep(0.02)
                
                    
                    
        
    
        