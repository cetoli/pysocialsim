"""
Defines the module with the implementation of BeginSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.base.decorators import public
from pysocialsim.common.simulator.event.generator.begin_simulation_event import BeginSimulationEvent

class BeginSimulationEventGenerator(AbstractSimulationEventGenerator):
    """
    Defines the the implementation of BeginSimulationEventGenerator.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/09/2009
    """

    def __init__(self):
        AbstractSimulationEventGenerator.initialize(self)
    
    @public
    def generateSimulationEvents(self):
        simulation = self.getSimulation()
        event = BeginSimulationEvent()
        simulation.registerSimulationEvent(event)
        return 1