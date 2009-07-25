from pysocialsim.p2p.message.abstract_p2p_message import AbstractP2PMessage

class DefaultP2PMessage(AbstractP2PMessage):
    
    def __init__(self, id, sourceId, targetId, ttl, priority):
        self.initialize("DEFAULT", id, sourceId, targetId, ttl, priority)