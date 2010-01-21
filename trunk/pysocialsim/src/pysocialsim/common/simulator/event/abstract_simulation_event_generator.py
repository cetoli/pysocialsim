"""
Defines the module with the implementation AbstractSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 29/08/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.simulator.event.i_simulation_event_generator import ISimulationEventGenerator
from pysocialsim.common.base.decorators import public
from pysocialsim.common.util.rotines import returns, requires, pre_condition
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation

class AbstractSimulationEventGenerator(Object, ISimulationEventGenerator):
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

    @public    
    def getSimulation(self):
        return returns(self.__simulation, ISimulation)

    @public
    def setSimulation(self, simulation):
        requires(simulation, ISimulation)
        pre_condition(simulation, lambda x: x <> None)
        self.__simulation = simulation
        return returns(self.__simulation, ISimulation)
    
    @public
    def generateSimulationEvents(self):
        return 0
    
    simulation = property(getSimulation, setSimulation, None, None)
    
