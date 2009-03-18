from pysocialsim.network.peer.abstract_peer import AbstractPeer
from pysocialsim.network.peer.peer_constants import PeerConstants
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.base.decorator.require import require
from pysocialsim.network.network import Network
from pysocialsim.network.peer.event.connection_event_generator import ConnectionEventGenerator
from pysocialsim.network.peer.event.disconnection_event_generator import DisconnectionEventGenerator
from pysocialsim.network.peer.event.file_advertisement_event_generator import FileAdvertisementEventGenerator
from pysocialsim.base.decorator.public import public
from random import randint
from pysocialsim.network.peer.message.file_advertisement_message import FileAdvertisementMessage
from pysocialsim.network.message.message_manager import MessageManager

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
    def advertise(self, advertisementType):
        if advertisementType == PeerConstants.FILE_ADVERTISEMENT:
            self.advertiseFile()
    
    def advertiseFile(self):
        if self.countFiles() == 0:
            return
        fileId = randint(0, self.countFiles() - 1)
        files = self.getFiles()
        network = self.getNetwork()
        topology = network.getTopology()
        neighbors = topology.getNeighbors(self.getId())
        for id in neighbors:
            message = FileAdvertisementMessage(MessageManager().getMessageId(), self.getId(), id, network.getSimulation().getTTL())
            message.setHop(1)
            message.registerTrace(self.getId())
            message.setParameter("fileId", fileId)
            message.setParameter("folksonomies", files[fileId].getFolksonomies())
            self.send(message)