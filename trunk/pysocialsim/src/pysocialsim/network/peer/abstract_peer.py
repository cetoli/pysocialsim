from pysocialsim.base.object import Object
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.base.decorator.require import require
from pysocialsim.network.network import Network
from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.simulation.event.event_generator import EventGenerator
from pysocialsim.simulator.simulation.simulation import Simulation
from types import NoneType
from pysocialsim.network.peer.event.send_event import SendEvent
from pysocialsim.network.peer.event.receive_event import ReceiveEvent
from pysocialsim.network.peer.necessity.necessity_constants import NecessityConstants

class AbstractPeer(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @return_type(None.__class__)
    @require("id", int)
    @require("network", Network)
    @require("type", int)
    @require("permanence", int)
    @require("absence", int)
    def initialize(self, id, network, type, permanence, absence):
        self.__id = id
        self.__network = network
        self.__eventGenerators = []
        self.__isConnected = False
        self.__type = type
        self.__permanence = permanence
        self.__absence = absence
        self.__currentTime = 0.0
        self.__messageDispatcher = None
        self.__files = {}
        self.__protocol = None
        self.__messageObservers = {}
        self.__interests = {}
        self.__necessities = {}
        
        self.__necessities[NecessityConstants.CONTENT] = []
    
    @public
    @return_type(int)
    def getId(self):
        return self.__id
    
    @public
    @return_type(Network)
    def getNetwork(self):
        return self.__network
    
    @public
    @return_type(EventGenerator)
    @require("generator", EventGenerator)
    def addEventGenerator(self, generator):
        self.__eventGenerators.append(generator)
        return self.__eventGenerators[len(self.__eventGenerators) - 1]
    
    @public
    @return_type(EventGenerator)
    @require("generator", EventGenerator)
    def removeEventGenerator(self, generator):
        index = self.__eventGenerators.index(generator)
        return self.__eventGenerators.pop(index)
    
    @public
    @return_type(int)
    def countEventGenerators(self):
        return len(self.__eventGenerators)
    
    @public
    @return_type(int)
    @require("simulation", Simulation)
    def generateEvents(self, simulation):
        for generator in self.__eventGenerators:
            generator.generateEvents(simulation)
            
    
    @public
    @return_type(bool)
    def isConnected(self):
        return self.__isConnected
    
    @public
    @return_type(NoneType)
    def connect(self):
        self.__protocol.connect()
    
    @public
    @return_type(NoneType)
    def disconnect(self):
        self.__protocol.disconnect()
        self.__isConnected = False
    
    @public
    @return_type(int)
    def getType(self):
        return self.__type
    
    @public
    @return_type(int)
    def getPermanenceTime(self):
        return self.__permanence
    
    @public
    @return_type(int)
    def getAbsenceTime(self):
        return self.__absence
    
    @public
    @return_type(NoneType)
    def stop(self):
        for generator in self.__eventGenerators:
            generator.stop()
    
    @public        
    def send(self, message):
        simulation = self.__network.getSimulation()
        event = SendEvent(self, simulation.getCurrentSimulationTime(), message)
        simulation.registerEvent(event)
        return message
    
    @public
    def receive(self, message):
        simulation = self.__network.getSimulation()
        event = ReceiveEvent(self, simulation.getCurrentSimulationTime(), message)
        simulation.registerEvent(event)
        return message
    
    @public
    def setCurrentTime(self, currentTime):
        self.__currentTime = currentTime
        return self.__currentTime
    
    @public
    def getCurrentTime(self):
        return self.__currentTime
    
    @public
    def sendMessage(self, message):
        self.__protocol.sendMessage(message)
    
    @public
    def receiveMessage(self, message):
        self.__protocol.receiveMessage(message)
        return message
        
    @public
    def setMessageDispatcher(self, dispatcher):
        self.__messageDispatcher = dispatcher
        return self.__messageDispatcher
    
    @public
    def getMessageDispatcher(self):
        return self.__messageDispatcher
    
    @public
    def createConnection(self, peerId):
        self.__network.createConnection(self.__id, peerId)
    
    @public
    def removeConnection(self, peerId):
        self.__network.removeConnection(self.__id, peerId)
    
    @public    
    def connected(self):
        self.__isConnected = True
        return self.__isConnected
    
    @public
    def disconnected(self):
        self.__isConnected = False
        return self.__isConnected
    
    @public
    def addFile(self, file):
        self.__files[file.getId()] = file
        file.addOwner(self.__id)
            
    
    @public
    def removeFile(self, id):
        del self.__files[id]
        file.removeOwner(self.__id)
    
    @public
    def countFiles(self):
        return len(self.__files)
    
    @public
    def getProtocol(self):
        return self.__protocol
    
    @public
    def setProtocol(self, protocol):
        self.__protocol = protocol.clone()
        self.__protocol.setPeer(self)
        for handlerClass in self.__protocol.getMessageHandlerClasses():
            handler = handlerClass(self)
            self.__messageDispatcher.registerMessageHandler(handler)
            handler.getMessageName()
        return self.__protocol
    
    @public
    def advertise(self, advertisementType):
        self.getProtocol().advertise(advertisementType)
    
    @public
    def getFile(self, id):
        return self.__files[id]
    
    @public
    def getFiles(self):
        return self.__files.values()
    
    @public
    def notifyMessageObservers(self, message):
        raise NotImplementedError()
    
    @public
    def addMessageObserver(self, observer):
        raise NotImplementedError()
    
    @public
    def removeMessageObserver(self, messageName):
        raise NotImplementedError()
    
    @public
    def countMessageObservers(self, messageName):
        raise NotImplementedError()
    
    def getInterests(self):
        return self.__interests
    
    @public
    def reputeContent(self, concept, folksonomy, reputationValue):
        concept = self.__interests[concept]
        interest = concept[folksonomy]
        interest.addReputation(reputationValue)
    
    @public
    def createNecessity(self, type):
        raise NotImplementedError()
    
    def registerNecessity(self, necessity):
        self.__necessities[necessity.getType()].append(necessity)