from pysocialsim.network.message.abstract_message import AbstractMessage

class PingMessage(AbstractMessage):
    
    def __init__(self, sourceId, targetId, ttl):
        self.initialize("PING", sourceId, targetId, ttl)