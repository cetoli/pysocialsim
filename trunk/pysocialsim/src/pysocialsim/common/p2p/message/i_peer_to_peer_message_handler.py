"""
Defines the module with the specification IPeerToPeerMessageHandler intreface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 15/10/2009
"""

class IPeerToPeerMessageHandler(object):
    """
    Defines the operations of peer-to-peer message handler.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 15/10/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def getHandle(self):
        """
        Gets the handle of peer-to-peer message.
        @return: an str
        @rtype: str
        """
        raise NotImplementedError()
    
    def getPeer(self):
        """
        Gets the target peer of peer-to-peer message.
        @return: an IPeer
        @rtype: IPeer
        """
        raise NotImplementedError()
    
    def getPeerToPeerMessage(self):
        """
        Gets the peer-to-peer message.
        @return: an IPeerToPeerMessage
        @rtype: IPeerToPeerMessage
        """
        raise NotImplementedError()
    
    def handlePeerToPeerMessage(self, peerToPeerMessage):
        """
        Handles peer-to-peer messages.
        @return: an IPeerToPeerMessage
        @rtype: IPeerToPeerMessage
        """
        raise NotImplementedError()
    
    def clone(self):
        """
        Clones the object.
        @return: an IPeerToPeerMessageHandler
        @rtype: IPeerToPeerMessageHandler
        """
        raise NotImplementedError()
        