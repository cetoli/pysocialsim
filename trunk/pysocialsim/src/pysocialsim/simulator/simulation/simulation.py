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
    
    def setNumberOfFiles(self, files):
        raise NotImplementedError()
    
    def getNumberOfFiles(self):
        raise NotImplementedError()
    
    def generateFiles(self):
        raise NotImplementedError()
    
    def setTTL(self, ttl):
        raise NotImplementedError()
    
    def getTTL(self):
        raise NotImplementedError()
    
    def setSimulationTime(self, simulationTime):
        raise NotImplementedError()
    
    def getSimulationTime(self):
        raise NotImplementedError()
    
    def getCurrentSimulationTime(self):
        raise NotImplementedError()
    
    def setCurrentSimulationTime(self, currentSimulationTime):
        raise NotImplementedError()
    
    def setPeerConnectionRate(self, peerNumber):
        raise NotImplementedError()
    
    def getPeerConnectionRate(self):
        raise NotImplementedError()
    
    def getPeerConnectionFrequency(self):
        raise NotImplementedError()