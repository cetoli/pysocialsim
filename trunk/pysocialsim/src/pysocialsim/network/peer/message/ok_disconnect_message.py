from pysocialsim.network.message.abstract_message import AbstractMessage

class OKDisconnectMessage(AbstractMessage):
    
    def __init__(self, sourceId, targetId, ttl):
        self.initialize("OK_DISCONNECT", sourceId, targetId, ttl)