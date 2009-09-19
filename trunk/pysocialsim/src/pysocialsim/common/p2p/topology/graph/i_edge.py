"""
Defines the module with the specification od IEdge interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 19/09/2009
"""

class IEdge(object):
    
    def getTargetNode(self):
        """
        Gets the target node.
        @return: a Node
        @rtype: Node
        """
        raise NotImplementedError()
    
    def dispatchData(self, data):
        """
        Dispatches data to target node
        @param data: an object
        @type data: object
        @return: an object
        @rtype: object
        """
        raise NotImplementedError()
        