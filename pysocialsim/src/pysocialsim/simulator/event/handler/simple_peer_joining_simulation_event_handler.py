"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 21/01/2010
"""
from pysocialsim.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class SimplePeerJoiningSimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "SIMPLE_PEER_JOIN")
        
    def execute(self):
        print self.getHandle()
        
        return AbstractSimulationEventHandler.execute(self)