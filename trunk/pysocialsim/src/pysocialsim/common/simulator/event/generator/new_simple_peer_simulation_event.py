"""
Defines the module with the implementation of NewSimplePeerSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class NewSimplePeerSimulationEvent(AbstractSimulationEvent):
    """
    Defines the implementation of NewSimplePeerSimulationEvent.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "NEW_SIMPLE_PEER", peerId, priority)
        