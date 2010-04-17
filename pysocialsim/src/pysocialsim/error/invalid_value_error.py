"""
Defines the module with the implementation of InvalidValueError class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 25/08/2009
"""

class InvalidValueError(RuntimeError):
    """
    Runtime error for invalid values for pre-condition violation.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 25/08/2009
    """

    def __init__(self, *args, **kwrgs):
        return RuntimeError.__init__(self, *args, **kwrgs)


    
        