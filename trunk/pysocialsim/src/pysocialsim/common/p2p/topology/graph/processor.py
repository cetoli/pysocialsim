'''
Created on 30/01/2010

@author: fabricio
'''
from pysocialsim.common.p2p.topology.graph.abstract_node_device import AbstractNodeDevice
from pysocialsim.common.p2p.topology.graph.i_node import INode
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.topology.graph.i_node_device import INodeDevice

class Processor(AbstractNodeDevice):
    
    def __init__(self, capacity):
        self.initialize(capacity)
        
    def initialize(self, capacity):
        AbstractNodeDevice.initialize(self, INode.PROCESSOR, capacity, 0, 0)
        self.__tasks = {}
        
    @public
    def input(self, data):
        return INodeDevice.input(self, data)

    @public
    def output(self, data):
        return INodeDevice.output(self, data)

    @public
    def getUsedCapacity(self):
        deviceUse = 0.0
        for task in self.__tasks.values():
            pass
        return deviceUse

    @public
    def getFreeCapacity(self):
        return self.getCapacity() - self.getUsedCapacity()
    
    