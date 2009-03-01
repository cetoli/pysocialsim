from pysocialsim.base.interface import Interface

class Simulation(object):

    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def setSimulator(self, simulator):
        raise NotImplementedError()
    
    def getNetwork(self):
        raise NotImplementedError()