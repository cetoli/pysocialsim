"""
Defines the module with the specification of IPeerToPeerMessageCreator interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""

class IPeerToPeerMessageCreator(object):
    """
    Defines the interface of peer-to-peer message creators.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/10/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def createPeerToPeerMessage(self, handle):
        """
        Creates the IPeerToPeerMessage object by handle parameter.
        @param handle: handle of peer-to-peer message
        @rtype: str
        @return: an IPeerToPeerMessage
        @rtype: IPeerToPeerMessage
        """
        raise NotImplementedError()