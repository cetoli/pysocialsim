from pysocialsim.network.message.abstract_message import AbstractMessage

class ConnectMessage(AbstractMessage):
    
    def __init__(self, sourceId, targetId, ttl):
        self.initialize("CONNECT", sourceId, targetId, ttl)