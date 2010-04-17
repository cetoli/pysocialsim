"""
Defines the module with SimplePeerInterestSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 06/11/2009
"""
from pysocialsim.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class SimplePeerInterestSimulationEvent(AbstractSimulationEvent):

    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "SIMPLE_PEER_INTEREST", peerId, priority)
        