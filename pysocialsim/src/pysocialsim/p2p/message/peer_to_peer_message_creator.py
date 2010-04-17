"""
Defines the module with the implementation of PeerToPeerMessageCreator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.p2p.message.i_peer_to_peer_message_creator import IPeerToPeerMessageCreator

class PeerToPeerMessageCreator(IPeerToPeerMessageCreator):
    """
    Defines the implementation of IPeerToPeerMessageCreator interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/10/2009
    """
    
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        self.__messagePrototypes = {}
    
        
    def registerPeerToPeerMessage(self, peerToPeerMessage):
        if self.__messagePrototypes.has_key(peerToPeerMessage.getHandle()):
            return False
        
        self.__messagePrototypes[peerToPeerMessage.getHandle()] = peerToPeerMessage
        return self.__messagePrototypes.has_key(peerToPeerMessage.getHandle()) 
    
    
    def createPeerToPeerMessage(self, handle):
        return self.__messagePrototypes[handle].clone()

    
    