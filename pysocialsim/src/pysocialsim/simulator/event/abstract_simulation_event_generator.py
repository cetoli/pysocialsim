"""
Defines the module with the implementation AbstractSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 29/08/2009
"""
from pysocialsim.simulator.event.i_simulation_event_generator import ISimulationEventGenerator

class AbstractSimulationEventGenerator(ISimulationEventGenerator):
    """
    Defines the basic implementation of ISimulationEventGenerator interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 29/08/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        self.__simulation = None

        
    def getSimulation(self):
        return self.__simulation

    
    def setSimulation(self, simulation):
        self.__simulation = simulation
        return self.__simulation
    
    
    def generateSimulationEvents(self):
        return 0
    
    
