"""
Defines the module with the implementation of NewSuperPeerSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.util.rotines import requires, pre_condition, factorial
from pysocialsim.common.base.decorators import public
from pysocialsim.common.simulator.event.generator.new_super_peer_simulation_event import NewSuperPeerSimulationEvent
import math

class NewSuperPeerSimulationEventGenerator(AbstractSimulationEventGenerator):
    """
    Defines the implementation of NewSuperPeerSimulationEventGenerator. This generator uses
    poisson distribution to define the appearance of new super peers in distributed system.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

    def __init__(self, average, time, superPeers):
        self.initialize(average, time, superPeers)

    def initialize(self, average, time, superPeers):
        """
        Initializes the simulation event generator.
        @param average: the average of new super peers appearance.
        @type average: a float
        @param time: frequence of new super peers appearance
        @type time: an int
        @param superPeers: maximum number of new superpeers
        @type superPeers: an int 
        @rtype: NoneType
        """
        AbstractSimulationEventGenerator.initialize(self)
        
        requires(average, float)
        requires(time, int)
        requires(superPeers, int)
        
        pre_condition(average, lambda x: x > 0)
        pre_condition(time, lambda x: x > 0)
        pre_condition(superPeers, lambda x: x > 0)
        
        self.__average = average
        self.__time = time
        self.__superPeers = superPeers
    
    @public    
    def generateSimulationEvents(self):
        simulation = self.getSimulation()
        generatedEvents = 1
        priority = 1
        superPeerId = 1
        event = NewSuperPeerSimulationEvent(superPeerId, priority)
        simulation.registerSimulationEvent(event)
        for i in range(1, int(self.__average * 2)):
            distPoisson = (pow(self.__average, i) / factorial(i)) * pow(math.e, -self.__average)
            times = round((simulation.getSimulationTime() / self.__time) * distPoisson)
            for i in range(1, int(times) + 1):
                priority += self.__time
                for j in range(i):
                    superPeerId += 1
                    event = NewSuperPeerSimulationEvent(superPeerId, priority)
                    simulation.registerSimulationEvent(event)
                    generatedEvents += 1
                    if self.__superPeers == superPeerId:
                        return generatedEvents
        return generatedEvents