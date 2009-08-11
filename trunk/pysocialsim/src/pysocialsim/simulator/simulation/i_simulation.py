from pysocialsim.base.interface import Interface

class ISimulation(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getP2PNetwork(self):
        raise NotImplementedError()
    
    def registerEvent(self, event):
        raise NotImplementedError()
    
    def unregisterEvent(self, handle):
        raise NotImplementedError()
    
    def countEvents(self, handle):
        raise NotImplementedError()
    
    def execute(self):
        raise NotImplementedError()
    
    def stop(self):
        raise NotImplementedError()
    
    def setSimulationTime(self, simulationTime):
        raise NotImplementedError()
    
    def getSimulationTime(self):
        raise NotImplementedError()
    
    def setGeneratedEvents(self, number):
        raise NotImplementedError()
    
    def getGeneratedEvents(self):
        raise NotImplementedError()
    
    def setSimulationCurrentTime(self, time):
        raise NotImplementedError()
    
    def getSimulationCurrentTime(self):
        raise NotImplementedError()
    
    def setNumberOfContents(self, contents):
        raise NotImplementedError()
    
    def getNumberOfContents(self):
        raise NotImplementedError()
    
    def setNumberOfHops(self, hops):
        raise NotImplementedError()
    
    def getNumberOfHops(self):
        raise NotImplementedError()