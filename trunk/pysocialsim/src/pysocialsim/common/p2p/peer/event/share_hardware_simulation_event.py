'''
Created on 30/01/2010

@author: fabricio
'''
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class ShareHardwareSimulationEvent(AbstractSimulationEvent):
    
    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "SHARE_HARDWARE", peerId, priority)