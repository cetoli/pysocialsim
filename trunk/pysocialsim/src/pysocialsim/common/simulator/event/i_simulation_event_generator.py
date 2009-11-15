"""
Defines the module with the ISimulationEventGenerator interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 29/08/2009
"""

class ISimulationEventGenerator(object):
    """
    Defines the interface of event simulation generators.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 29/08/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    def generateSimulationEvents(self):
        """
        Generates simulation events
        @return: number of generated simulation events.
        @rtype: int
        """
        raise NotImplementedError()
    
    def getSimulation(self):
        """
        Gets a simulation object.
        @return: an ISimulation
        @rtype: ISimulation
        """
        raise NotImplementedError()
    
    def setSimulation(self, simulation):
        """
        Sets a simulation object.
        @param simulation: an ISimulation
        @type simulation: ISimulation
        @return: an ISimulation
        @rtype: ISimulation
        """
        raise NotImplementedError()