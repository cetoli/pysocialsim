from pysocialsim.base.interface import Interface

class IStochasticModel(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def generateEvents(self, simulation):
        raise NotImplementedError()