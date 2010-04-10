'''
Created on 30/01/2010

@author: fabricio
'''
from pysocialsim.common.p2p.topology.graph.abstract_node_device import AbstractNodeDevice
from pysocialsim.common.p2p.topology.graph.i_node import INode
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.topology.graph.i_node_device import INodeDevice

class Memory(AbstractNodeDevice):
    
    def __init__(self, capacity):
        self.initialize(capacity)
        
    def initialize(self, capacity):
        AbstractNodeDevice.initialize(self, INode.MEMORY, capacity, 0, 0)
        self.__programs = {}
        
    @public
    def input(self, data):
        return INodeDevice.input(self, data)

    @public
    def output(self, data):
        return INodeDevice.output(self, data)

    @public
    def getUsedCapacity(self):
        deviceUse = 0.0
        for program in self.__programs.values():
            pass
        return deviceUse

    @public
    def getFreeCapacity(self):
        return self.getCapacity() - self.getUsedCapacity()
    