'''
Created on 02/02/2010

@author: fabricio
'''
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class ShareContentSimulationEvent(AbstractSimulationEvent):
    
    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "SHARE_CONTENT", peerId, priority)
    
