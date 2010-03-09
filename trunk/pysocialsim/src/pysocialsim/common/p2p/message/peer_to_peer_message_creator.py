"""
Defines the module with the implementation of PeerToPeerMessageCreator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.util.rotines import requires, pre_condition
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage
from pysocialsim.common.p2p.message.i_peer_to_peer_message_creator import IPeerToPeerMessageCreator
from pysocialsim.common.base.decorators import public

class PeerToPeerMessageCreator(Object, IPeerToPeerMessageCreator):
    """
    Defines the implementation of IPeerToPeerMessageCreator interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/10/2009
    """

    def initialize(self):
        self.__messagePrototypes = {}
    
    @public    
    def registerPeerToPeerMessage(self, peerToPeerMessage):
        """
        Registries an peer-to-peer message protypes.
        @param peerToPeerMessage: the peer-to-peer message prototype
        @type peerToPeerMessage: IPeerToPeerMessage
        @return: Returns True, if peer-to-peer message was registered. Else, False.
        @rtype: bool
        """
        requires(peerToPeerMessage, IPeerToPeerMessage)
        pre_condition(peerToPeerMessage, lambda x: x <> None)
        
        if self.__messagePrototypes.has_key(peerToPeerMessage.getHandle()):
            return False
        
        self.__messagePrototypes[peerToPeerMessage.getHandle()] = peerToPeerMessage
        return self.__messagePrototypes.has_key(peerToPeerMessage.getHandle()) 
    
    @public
    def createPeerToPeerMessage(self, handle):
        requires(handle, str)
        pre_condition(handle, lambda x: x <> None)
        pre_condition(handle, lambda x: self.__messagePrototypes.has_key(x))
        
        return self.__messagePrototypes[handle].clone()

    
    