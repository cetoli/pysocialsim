from pysocialsim.network.message.abstract_message import AbstractMessage

class OKConnectMessage(AbstractMessage):
    
    def __init__(self, sourceId, targetId, ttl):
        self.initialize("OK_CONNECT", sourceId, targetId, ttl)