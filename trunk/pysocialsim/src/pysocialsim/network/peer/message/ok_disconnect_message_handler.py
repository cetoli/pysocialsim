from pysocialsim.network.peer.message.abstract_message_handler import AbstractMessageHandler

class OKDisconnectMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("OK_DISCONNECT", peer)