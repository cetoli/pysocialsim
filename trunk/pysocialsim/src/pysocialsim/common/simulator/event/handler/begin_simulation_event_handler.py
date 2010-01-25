"""
Defines the module with the implementation of BeginSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class BeginSimulationEventHandler(AbstractSimulationEventHandler):
    """
    Defines the implementation of BeginSimulationEventHandler
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/09/2009
    """

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "BEGIN_SIMULATION")
    
    def execute(self):
        return AbstractSimulationEventHandler.execute(self)
    
    
        