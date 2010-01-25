"""
Defines the module with the specification of ISimulationEvent interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""

class ISimulationEvent(object):
    """
    Defines the interface of simulation event objects.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 23/08/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def getHandle(self):
        """
        Gets the handle of simulation event.
        @return: Returns the str object.
        @rtype: str
        """
        raise NotImplementedError()
    
    def getPriority(self):
        """
        Gets the priority of simulation event.
        @return: Returns the int object.
        @rtype: int
        """
        raise NotImplementedError()
    
    def getPeerId(self):
        """
        Gets the peerId of simulation event.
        @return: Returns the int object
        @rtype: int
        """
        raise NotImplementedError()
    
    def handled(self):
        """
        Changes the state of simulation event to handled.
        @return: Returns the bool object.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def isHandled(self):
        """
        Verifies the state of simulation event, returns true if simulation event already was
        handled, else returns false.
        @return: Returns the bool object.
        @rtype: bool
        """
        raise NotImplementedError()
    
    def setPeerId(self, peerId):
        raise NotImplementedError()
    
    def registerParameter(self, name, value):
        raise NotImplementedError()
    
    def hasParameter(self, name):
        raise NotImplementedError()
        
    def getParameter(self, name):
        raise NotImplementedError()