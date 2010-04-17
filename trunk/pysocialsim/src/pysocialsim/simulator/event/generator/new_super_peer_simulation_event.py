"""
Defines the module with the implementation of NewSuperPeerSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class NewSuperPeerSimulationEvent(AbstractSimulationEvent):
    """
    Defines the implementation of NewSuperPeerSimulationEvent.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "NEW_SUPER_PEER", peerId, priority)