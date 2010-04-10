"""
Defines the module with the implementation of DefaultSimulationEvent class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class DefaultSimulationEvent(AbstractSimulationEvent):
    """
    Defines a default implementation of AbstractSimulationEvent class.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 23/08/2009
    """

    def __init__(self, peer, priority):
        self.initialize("DEFAULT", peer, priority)
    