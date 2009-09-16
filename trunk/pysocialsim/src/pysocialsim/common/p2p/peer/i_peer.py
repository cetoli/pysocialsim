"""
Defines the module with the specification of IPeer interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""

class IPeer(object):
    """
    Defines the interface of peer objects.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 23/08/2009
    """

    def __init__(self):
        """
        @raise NotImplementedError: Interfaces can't be instantiated.
        """
        raise NotImplementedError()
    
    def getId(self):
        """
        Gets the peer identifier.
        @return: a int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getType(self):
        """
        Gets the type of peer.
        @return: a int
        @rtype: int
        """
        raise NotImplementedError()
        