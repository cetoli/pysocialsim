from pysocialsim.network.message.abstract_message import AbstractMessage

class DisconnectMessage(AbstractMessage):
    
    def __init__(self, sourceId, targetId, ttl):
        self.initialize("DISCONNECT", sourceId, targetId, ttl)