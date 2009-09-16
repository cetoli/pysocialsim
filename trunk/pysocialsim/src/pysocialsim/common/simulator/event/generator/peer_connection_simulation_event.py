"""
Defines the module with the implementation of ConnectSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 29/08/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class PeerConnectionSimulationEvent(AbstractSimulationEvent):
    """
    Defines the implementation of connect simulation event.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 29/08/2009
    """

    def __init__(self, peer, priority):
        """
        Defines the constructor method.
        @param peer: peer of simulation event
        @type peer: IPeer
        @param priority: priority of simulation event.
        @type priority: int
        @rtype: None
        """
        AbstractSimulationEvent.initialize(self, "CONNECT_PEER", peer, priority)