"""
Defines the module with the specification of INodeDevice interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/09/2009
"""

class INodeDevice(object):
    """
    Defines common operations of node devices.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 18/09/2009
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getType(self):
        """
        Gets the type of device
        @return: an int
        @rtype: int
        """
        raise NotImplementedError()
    
    def getCapacity(self):
        """
        Gets the capacity of device.
        @return: a float
        @rtype: float
        """
        raise NotImplementedError()
    
    def input(self, data):
        """
        Inputs data in node device.
        @param data: an object
        @return: an object
        @rtype: object
        """
        raise NotImplementedError()
    
    def output(self, data):
        """
        Outputs data in node device.
        @param data: an object
        @return: an object
        @rtype: object
        """
        raise NotImplementedError()
    
    def getUsedCapacity(self):
        """
        Gets the used capacity of device.
        @return: a float
        @rtype: float
        """
        raise NotImplementedError()
    
    def getFreeCapacity(self):
        """
        Gets the free capacity of device.
        @return: a float
        @rtype: float
        """
        raise NotImplementedError()
    
    def getInputSpeed(self):
        """
        Gets the speed of data input
        @return: a float
        @rtype: float
        """
        raise NotImplementedError()
    
    def getOutputSpeed(self):
        """
        Gets the speed of data output
        @return: a float
        @rtype: float
        """
        raise NotImplementedError()