from pysocialsim.network.peer.event.abstract_peer_event import AbstractPeerEvent

class ReceiveEvent(AbstractPeerEvent):
    
    def __init__(self, peer, priority, message):
        self.initialize("RECEIVE_MESSAGE", peer, priority, message)