'''
Created on 30/01/2010

@author: fabricio
'''

from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.topology.graph.i_node import INode
from random import uniform

class ShareHardwareSimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "SHARE_HARDWARE")
        
    def execute(self):
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        event = self.getSimulationEvent()
        simplePeer = network.getPeer(IPeerToPeerNetwork.SIMPLE_PEER, event.getPeerId())
        
        deviceType = event.getParameter("deviceType")
        
        sharedPercentage = 0
        
        if deviceType == INode.DISK:
            sharedPercentage = uniform(0.01, 1.0)
        elif deviceType == INode.PROCESSOR:
            sharedPercentage = uniform(0.01, 1.0)
        elif deviceType == INode.MEMORY:
            sharedPercentage = uniform(0.01, 1.0)
        
        simplePeer.shareHardware(event.getPriority(), deviceType, sharedPercentage, event.getParameter("opportunityId"))