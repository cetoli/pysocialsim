"""
Defines the module with the implementation of Node class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/09/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.util.rotines import requires, returns, pre_condition
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology
from pysocialsim.common.base.decorators import public
from pysocialsim.common.error import io_error
from pysocialsim.common.p2p.topology.graph.i_node_device import INodeDevice
from pysocialsim.common.p2p.topology.graph.i_edge import IEdge
from pysocialsim.common.p2p.topology.graph.i_node import INode

class Node(Object, INode):
    """
    Defines the implementation of network node.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 18/09/2009
    """
    
    PROCESSOR = 0
    DISK = 1
    NETWORK_ADAPTER = 2
    
    __public__ = ["PROCESSOR", "DISK", "NETWORK_ADAPTER"]
    
    def __init__(self, id, topology):
        """
        Constructor of Node class
        @param id: the node identifier
        @type id: int
        @param topology: an IPeerToPeerTopology
        @type topology: IPeerToPeerTopology
        @rtype: NoneType
        """
        self.initialize(id, topology)
    
    def initialize(self, id, topology):
        """
        Initializes the object
        @param id: the node identifier
        @type id: int
        @param topology: an IPeerToPeerTopology
        @type topology: IPeerToPeerTopology
        @rtype: NoneType
        """
        requires(topology, IPeerToPeerTopology)
        self.__id = id
        self.__topology = topology
        self.__edges = {}
        self.__devices = {}
    
    @public
    def getId(self):
        return returns(self.__id, int)
    
    @public    
    def addNodeDevice(self, nodeDevice):
        """
        Adds a node device.
        @param nodeDevice: INodeDevice
        @rtype: INodeDevice
        """
        requires(nodeDevice, INodeDevice)
        
        pre_condition(nodeDevice, lambda x: x <> None)
        
        self.__devices[nodeDevice.getType()] = nodeDevice
        return returns(self.__devices.has_key(nodeDevice.getType()), bool)
    
    @public
    def removeNodeDevice(self, nodeDevice):
        """
        Removes a node device.
        @param nodeDevice: INodeDevice
        @rtype: INodeDevice
        """
        requires(nodeDevice, INodeDevice)
        pre_condition(nodeDevice, lambda x: x <> None)
        del self.__devices[nodeDevice.getType()]
        return returns(not self.__devices.has_key(nodeDevice.getType()), bool)
    
    @public
    def getNodeDevice(self, nodeDeviceType):
        """
        Gets a node device.
        @param nodeDeviceType: the type of node device
        @type nodeDeviceType: int
        """
        requires(nodeDeviceType, int)
        
        pre_condition(nodeDeviceType, lambda x: x <> None)
        pre_condition(nodeDeviceType, lambda x: self.__devices.has_key(x))
        
        return returns(self.__devices[nodeDeviceType], INodeDevice)
    
    @public
    def getNodeDevices(self):
        """
        Gets the list of node devices
        @return: an list
        @rtype: list
        """
        return self.__devices.itervalues()
    
    @public
    def countNodeDevices(self):
        """
        Counts the number of node devices.
        @return: a int
        @rtype: int
        """
        return len(self.__devices)
    
    @public
    def getPeerToPeerTopology(self):
        """
        Gets the peer-to-peer topology
        @return: a IPeerToPeerTopology
        @rtype: IPeerToPeerTopology
        """
        return returns(self.__topology, IPeerToPeerTopology)
    
    @public
    def input(self, nodeDeviceType, data):
        requires(nodeDeviceType, int)
        
        pre_condition(nodeDeviceType, lambda x: x <> None)
        pre_condition(data, lambda x: x <> None)
        
        if not self.__devices.has_key(nodeDeviceType):
            raise io_error.IOError()
        
        return self.__devices[nodeDeviceType].input(data)
    
    @public
    def output(self, nodeDeviceType, data):
        requires(nodeDeviceType, int)
        
        pre_condition(nodeDeviceType, lambda x: x <> None)
        pre_condition(data, lambda x: x <> None)
        
        if not self.__devices.has_key(nodeDeviceType):
            raise io_error.IOError()
        
        return self.__devices[nodeDeviceType].output(data)
    
    @public
    def addEdge(self, edge):
        requires(edge, IEdge)
        pre_condition(edge, lambda x: x <> None)
        
        if self.__edges.has_key(edge.getTargetNode().getId()):
            return False
        if self.__id == edge.getTargetNode().getId():
            return False
        self.__edges[edge.getTargetNode().getId()] = edge
        return returns(self.__edges.has_key(edge.getTargetNode().getId()), bool)
    
    @public
    def removeEdge(self, edge):
        requires(edge, IEdge)
        pre_condition(edge, lambda x: x <> None)
        
        if not self.__edges.has_key(edge.getTargetNode().getId()):
            return False
        del self.__edges[edge.getTargetNode().getId()]
        return returns(not self.__edges.has_key(edge.getTargetNode().getId()), bool)
    
    @public
    def getEdge(self, targetNodeId):
        requires(targetNodeId, int)
        
        pre_condition(targetNodeId, lambda x: x <> None)
        pre_condition(targetNodeId, lambda x: x > 0)
        pre_condition(targetNodeId, lambda x: self.__edges.has_key(targetNodeId))
        
        return returns(self.__edges[targetNodeId], IEdge)
    
    @public
    def getEdges(self):
        return self.__edges.itervalues()
    
    @public
    def countEdges(self):
        return returns(len(self.__edges), int)
    
    @public
    def hasEdge(self, targetNodeId):
        return returns(self.__edges.has_key(targetNodeId), bool)