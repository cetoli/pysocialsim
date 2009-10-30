"""
Defines the module with the implementation of SimplePeerLeavingSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 30/10/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class SimplePeerLeavingSimulationEventHandler(AbstractSimulationEventHandler):
    """
    classdocs
    """

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "SIMPLE_PEER_LEAVE")
    
    def execute(self):
        return AbstractSimulationEventHandler.execute(self)