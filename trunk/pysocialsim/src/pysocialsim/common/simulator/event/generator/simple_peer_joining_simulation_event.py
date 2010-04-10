"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 21/01/2010
"""
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class SimplePeerJoiningSimulationEvent(AbstractSimulationEvent):
    
    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "SIMPLE_PEER_JOIN", peerId, priority)