"""
Defines the module with the implementation of EndSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.base.decorators import public
from pysocialsim.common.simulator.event.generator.end_simulation_event import EndSimulationEvent

class EndSimulationEventGenerator(AbstractSimulationEventGenerator):
    """
    Defines the implementation of EndSimulationEventGenerator
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
        event = EndSimulationEvent(simulation.getSimulationTime() - 1)
        simulation.registerSimulationEvent(event)
        return 1
        