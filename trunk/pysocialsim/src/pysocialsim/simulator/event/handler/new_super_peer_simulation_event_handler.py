"""
Defines the module with the implementation of NewSuperPeerSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class NewSuperPeerSimulationEventHandler(AbstractSimulationEventHandler):
    """
    Defines the implementation of NewSuperPeerSimulationEventHandler
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "NEW_SUPER_PEER")
    
    def execute(self):
        print self.getHandle()
        
        return AbstractSimulationEventHandler.execute(self)
        