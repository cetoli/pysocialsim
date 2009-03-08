from pysocialsim.base.interface import Interface

class Simulation(object):

    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def setSimulator(self, simulator):
        raise NotImplementedError()
    
    def getNetwork(self):
        raise NotImplementedError()
    
    def registerEvent(self, event):
        raise NotImplementedError()
    
    def countEvents(self):
        raise NotImplementedError()
    
    def unregisterEvent(self):
        raise NotImplementedError()
    
    def generateEvents(self):
        raise NotImplementedError()
    
    def simulate(self):
        raise NotImplementedError()
    
    def stop(self):
        raise NotImplementedError()