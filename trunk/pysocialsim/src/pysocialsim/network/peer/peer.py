from pysocialsim.base.interface import Interface
from pysocialsim.simulator.simulation.event.event_generator import EventGenerator

class Peer(EventGenerator):

    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getId(self):
        raise NotImplementedError()
    
    def addEventGenerator(self, generator):
        raise NotImplementedError()
    
    def removeEventGenerator(self, generator):
        raise NotImplementedError()
    
    def countEventGenerators(self):
        raise NotImplementedError()
    
    def getNetwork(self):
        raise NotImplementedError()
    
    def isConnected(self):
        raise NotImplementedError()
    
    def connect(self):
        raise NotImplementedError()
    
    def disconnect(self):
        raise NotImplementedError()