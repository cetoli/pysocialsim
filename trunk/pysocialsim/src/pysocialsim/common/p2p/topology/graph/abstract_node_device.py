"""
Defines the module with the implementation of AbstractNodeDevice class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/10/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.topology.graph.i_node_device import INodeDevice
from pysocialsim.common.base.decorators import public

class AbstractNodeDevice(Object, INodeDevice):
    """
    Defines the common implementation of INodeDevice objects.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 13/10/2009
    """

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, type, capacity, inputSpeed, outputSpeed):
        self.__type = type
        self.__capacity = capacity
        self.__inputSpeed = inputSpeed
        self.__outputSpeed = outputSpeed
        self.__node = None
    
    @public    
    def getType(self):
        return self.__type

    @public
    def getCapacity(self):
        return self.__capacity

    @public
    def getInputSpeed(self):
        return self.__inputSpeed

    @public
    def getOutputSpeed(self):
        return self.__outputSpeed

    @public
    def getNode(self):
        return self.__node

    @public
    def setNode(self, node):
        self.__node = node

        
    type = property(getType, None, None, None)

    capacity = property(getCapacity, None, None, None)

    inputSpeed = property(getInputSpeed, None, None, None)

    outputSpeed = property(getOutputSpeed, None, None, None)

    node = property(getNode, setNode, None, None)
