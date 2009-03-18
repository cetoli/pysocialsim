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
    
    def getType(self):
        raise NotImplementedError()
    
    def getPermanenceTime(self):
        raise NotImplementedError()
    
    def getAbsenceTime(self):
        raise NotImplementedError()
    
    def send(self, message):
        raise NotImplementedError()
    
    def receive(self, message):
        raise NotImplementedError()
    
    def setCurrentTime(self, currentTime):
        raise NotImplementedError()
    
    def getCurrentTime(self):
        raise NotImplementedError()
    
    def sendMessage(self, message):
        raise NotImplementedError()
    
    def receiveMessage(self, message):
        raise NotImplementedError()
    
    def setMessageDispatcher(self, dispatcher):
        raise NotImplementedError()
    
    def getMessageDispatcher(self):
        raise NotImplementedError()
    
    def createConnection(self, peerId):
        raise NotImplementedError()
    
    def removeConnection(self, peerId):
        raise NotImplementedError()
    
    def connected(self):
        raise NotImplementedError()
    
    def disconnected(self):
        raise NotImplementedError()
    
    def addFile(self, file):
        raise NotImplementedError()
    
    def removeFile(self, id):
        raise NotImplementedError()
    
    def countFiles(self):
        raise NotImplementedError()
    
    def getFile(self, index):
        raise NotImplementedError()
    
    def getFiles(self):
        raise NotImplementedError()
    
    def advertise(self, advertisementType):
        raise NotImplementedError()
    
    def getProtocol(self):
        raise NotImplementedError()
    
    def setProtocol(self, protocol):
        raise NotImplementedError()