from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.p2p.peer.i_peer import IPeer
from pysocialsim.base.decorator.require import require
from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork
from pysocialsim.p2p.protocol.i_p2p_protocol import IP2PProtocol
from pysocialsim.p2p.peer.default_peer import DefaultPeer
from types import NoneType
from pysocialsim.p2p.content.default_content import DefaultContent
from pysocialsim.p2p.folksonomy.folksonomy_map import FolksonomyMap
from random import randint
from pysocialsim.p2p.profile.i_matching_strategy import IMatchingStrategy

class DefaultPeerBuilder(Object):
    
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        self.__peer = None
        self.__director = None
    
    @public
    def createPeer(self, id, network, protocol, matchingStrategy):
        self.__peer = DefaultPeer(id, network, protocol, matchingStrategy)
        return self.__peer
    
    @public
    def buildContent(self, params):
        content = params["content"]
        totalPeers = content["totalPeers"]
        
        contentPerPeer = content["contentPerPeer"]
        
        if (totalPeers * contentPerPeer) == self.__director.getTotalFile():
            return
        
        network = self.__peer.getP2PNetwork()
        network.registerPeerForAdvertisement(self.__peer.getId())
        
        for id in range(contentPerPeer):
            self.__director.setTotalFile(self.__director.getTotalFile() + 1)
            size = range(content["minSize"], content["maxSize"])
            
            map = FolksonomyMap()
            
            concept = map.mapping.keys()[randint(0, len(map.mapping.keys()) - 1)]
            initial = randint(0, (len(concept)/2) - 1)
            end = randint((len(concept)/2), len(concept) - 1)
            
            c = DefaultContent(self.__director.getTotalFile(), [], size)
            
            for ix in range(initial, end):
                c.addFolksonomy(map.mapping[concept][ix])
                
            self.__peer.addContent(c)
            print "arquivo ", c.getId()
            
    @public
    def getPeer(self):
        return self.__peer
    
    @public
    def setPeerBuilderDirector(self, director):
        self.__director = director
        return self.__director