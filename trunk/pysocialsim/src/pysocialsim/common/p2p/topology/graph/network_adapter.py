"""
Defines the module with the implementation of NetworkAdapter class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/10/2009
"""
from pysocialsim.common.p2p.topology.graph.abstract_node_device import AbstractNodeDevice
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import pre_condition
from pysocialsim.common.p2p.topology.graph.i_node import INode
from random import uniform

class NetworkAdapter(AbstractNodeDevice):
    """
    Defines the implementation of network adapter.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 13/10/2009
    """

    def __init__(self, capacity, inputSpeed, outputSpeed):
        AbstractNodeDevice.initialize(self, INode.NETWORK_ADAPTER, capacity, inputSpeed, outputSpeed)

    @public
    def input(self, data):
        node = self.getNode()
        peer = node.getPeer()
        network = peer.getPeerToPeerNetwork()
        
        self.setCapacity(uniform(0.01, network.getLinkAvailability()/100.0))
        protocol = peer.getPeerToPeerProtocol()
        protocol.receive(peer, data)
        
        speed = (self.getInputSpeed() * self.getCapacity())
        streamSize = data.getSize() * 8
        
        data.setTime(data.getTime() + (streamSize / speed))
        
    @public
    def output(self, data):
        pre_condition(data, lambda x: x <> None)
        
        node = self.getNode()
        peer = node.getPeer()
        network = peer.getPeerToPeerNetwork()
        
        self.setCapacity(uniform(0.01, network.getLinkAvailability()/100.0))
        
        topology = node.getPeerToPeerTopology()
        edge = topology.getEdge(node.getId(), data.getTargetId())
        targetNode = edge.getTargetNode()
        targetNode.input(INode.NETWORK_ADAPTER, data)

    @public
    def getUsedCapacity(self):
        return self.getCapacity()

    @public
    def getFreeCapacity(self):
        return (1 - self.getCapacity())

    
    