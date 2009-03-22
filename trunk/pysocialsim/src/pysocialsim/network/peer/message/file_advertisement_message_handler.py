from pysocialsim.network.peer.message.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public

class FileAdvertisementMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("FILE_ADVERTISEMENT", peer)
        
    @public
    def executeHandler(self, message):
        message.registerTrace(self.getPeer().getId())
        print message.getHop(), message.getTTL()
        print message.getTraces()
        message.setSourceId(self.getPeer().getId())
        network = self.getPeer().getNetwork()
        topology = network.getTopology()
        neighbors = topology.getNeighbors(self.getPeer().getId())
        if message.getHop() + 1 > message.getTTL():
            return
        for id in neighbors:
            if not id in message.getTraces():
                msg = message.clone()
                msg.setTargetId(id)
                msg.setHop(msg.getHop() + 1)
                network.getPeer(id).send(msg)
        
    @public
    def clone(self):
        return FileAdvertisementMessageHandler(self.getPeer())