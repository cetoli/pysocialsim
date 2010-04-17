"""
Defines the module with the implementation of EndSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class EndSimulationEventHandler(AbstractSimulationEventHandler):
    """
    Defines the implementation of EndSimulationEventHandler
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/09/2009
    """

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "END_SIMULATION")
    
    def execute(self):
        return AbstractSimulationEventHandler.execute(self)
    
    
        