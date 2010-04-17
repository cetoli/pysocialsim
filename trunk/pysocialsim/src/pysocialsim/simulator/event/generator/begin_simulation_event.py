"""
Defines the module with the implementation of BeginSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class BeginSimulationEvent(AbstractSimulationEvent):
    """
    Defines the implementation of BeginSimulationEvent
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/09/2009
    """

    def __init__(self):
        """
        @author: Fabricio
        @organization: Federal University of Rio de Janeiro
        @contact: fbarros@gmail.com 
        @since: 11/09/2009
        """
        AbstractSimulationEvent.initialize(self, "BEGIN_SIMULATION", "", 1)
        