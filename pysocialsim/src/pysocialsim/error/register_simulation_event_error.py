"""
Defines the module with the implementation of RegisterSimulationEventError class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 27/08/2009
"""

class RegisterSimulationEventError(StandardError):
    """
    Defines an exception for registry error of simulation events.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 27/08/2009
    """

    def __init__(self, *args, **kwrgs):
        StandardError.__init__(self, *args, **kwrgs)


    
        