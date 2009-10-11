"""
Defines the module with the implementation of EndSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class EndSimulationEvent(AbstractSimulationEvent):
    """
    Defines the implementation of EndSimulationEvent.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/09/2009
    """

    def __init__(self, priority):
        AbstractSimulationEvent.initialize(self, "END_SIMULATION", "", priority)
        