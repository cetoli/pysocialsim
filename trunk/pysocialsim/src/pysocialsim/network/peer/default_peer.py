from pysocialsim.network.peer.abstract_peer import AbstractPeer
from pysocialsim.network.peer.peer_constants import PeerConstants
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.base.decorator.require import require
from pysocialsim.network.network import Network
from pysocialsim.network.peer.event.connection_event_generator import ConnectionEventGenerator
from pysocialsim.network.peer.event.disconnection_event_generator import DisconnectionEventGenerator
from pysocialsim.network.peer.event.file_advertisement_event_generator import FileAdvertisementEventGenerator
from pysocialsim.base.decorator.public import public
from pysocialsim.network.peer.interest.default_interest import DefaultInterest

class DefaultPeer(AbstractPeer):
    
    def __init__(self, id, network, permancence, absence):
        self.initialize(id, network, PeerConstants.DEFAULT_PEER, permancence, absence)
        
    @return_type(None.__class__)
    @require("id", int)
    @require("network", Network)
    @require("type", int)
    @require("permanence", int)
    @require("absence", int)
    def initialize(self, id, network, type, permanence, absence):
        AbstractPeer.initialize(self, id, network, type, permanence, absence)
        self.addEventGenerator(ConnectionEventGenerator(self))
        self.addEventGenerator(DisconnectionEventGenerator(self))
        self.addEventGenerator(FileAdvertisementEventGenerator(self))
    
    @public
    def addFile(self, file):
        AbstractPeer.addFile(self, file)
        
        interests = self.getInterests()
        if not interests.has_key(file.getConcept()):
            interests[file.getConcept()] = {}
            concept = interests[file.getConcept()]
            for f in file.getFolksonomies():
                interest = DefaultInterest(f)
                concept[interest.getFolksonomy()] = interest
        else:
            concept = interests[file.getConcept()]
            for f in file.getFolksonomies():
                if not concept.has_key(f):
                    interest = DefaultInterest(f)
                    concept[interest.getFolksonomy()] = interest
        