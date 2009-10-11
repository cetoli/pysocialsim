"""
Defines the module with the implementation of NewSimplePeerSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class NewSimplePeerSimulationEventHandler(AbstractSimulationEventHandler):
    """
    Defines the implementation of NewSimplePeerSimulationEventHandler
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "NEW_SIMPLE_PEER")
    
    def execute(self):
        
        
        return AbstractSimulationEventHandler.execute(self)
        