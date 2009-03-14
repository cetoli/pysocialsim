from pysocialsim.network.peer.message.abstract_message_dispatcher import AbstractMessageDispatcher

class DefaultMessageDispatcher(AbstractMessageDispatcher):
    
    def __init__(self, peer):
        self.initialize(peer)