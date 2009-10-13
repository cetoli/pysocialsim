"""
Defines the module with the implementation of Edge class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 18/09/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.util.rotines import pre_condition, requires, returns
from pysocialsim.common.p2p.topology.graph.node import Node
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.topology.graph.i_edge import IEdge
from pysocialsim.common.p2p.topology.graph.i_node import INode

class Edge(Object, IEdge):
    """
    Defines the implementation of graph edge.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 18/09/2009
    """

    def __init__(self, node, targetNode):
        """
        Constructor of class
        @param targetNode: an Node
        @type targetNode: Node
        @rtype: None
        """
        self.initialize(node, targetNode)

    def initialize(self, node, targetNode):
        """
        Initialize the object.
        @param targetNode: an Node
        @type targetNode: Node
        @rtype: None
        """
        requires(node, INode)
        pre_condition(node, lambda x: x <> None)
        requires(targetNode, INode)
        pre_condition(targetNode, lambda x: x <> None)
        
        self.__node = node
        self.__targetNode = targetNode
    
    @public
    def getTargetNode(self):
        return self.__targetNode

    @public
    def getNode(self):
        return self.__node
    
    @public
    def dispatchData(self, data):
        """
        Dispatches data to target node
        @param data: an object
        @type data: object
        @return: an object
        @rtype: object
        """
        pre_condition(data, lambda x: x <> None)
        return self.__node.output(Node.NETWORK_ADAPTER, data)

    node = property(getNode, None, None, None)

    targetNode = property(getTargetNode, None, None, None)
    
    