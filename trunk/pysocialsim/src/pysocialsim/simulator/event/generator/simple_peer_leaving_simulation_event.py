"""
Defines the module with SimplePeerLeavingSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 30/10/2009
"""
from pysocialsim.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class SimplePeerLeavingSimulationEvent(AbstractSimulationEvent):

    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "SIMPLE_PEER_LEAVE", peerId, priority)
        