from pysocialsim.network.peer.event.abstract_peer_event import AbstractPeerEvent

class SendEvent(AbstractPeerEvent):
    
    def __init__(self, peer, priority, message):
        self.initialize("SEND_MESSAGE", peer, priority, message)