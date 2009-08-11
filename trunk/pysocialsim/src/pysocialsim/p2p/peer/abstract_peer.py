from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.dispatcher.message_dispatcher import MessageDispatcher
from sets import ImmutableSet
from pysocialsim.p2p.peer.i_peer import IPeer
from random import randint
from pysocialsim.p2p.message.message_manager import MessageManager

class AbstractPeer(Object):
    
    CONTENT_ADVERTISEMENT = 0
    
    __public__ = ["CONTENT_ADVERTISEMENT"]
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, id, network, protocol, matchingStrategy):
        self.__id = id
        self.__network = network
        self.__isConnected = False
        self.__dispatcher = MessageDispatcher(self)
        self.__protocol = None
        self.setP2PProtocol(protocol)
        self.__contents = {}
        self.__profile = None
        self.__sharedContent = []
        self.__unsharedContent = []
        self.__connectionTime = 0
        self.__neighbors = {}
        self.__disconnectionTime = 0
        self.__scheduledDisconnection = False
        self.__diskSpace = 83886080
        
    @public
    def getId(self):
        return self.__id
    
    @public
    def isConnected(self):
        return self.__isConnected
    
    @public
    def setP2PProtocol(self, protocol):
        self.__protocol = protocol
        self.__protocol.setPeer(self)
        self.__protocol.setP2PTopology(self.__network.getP2PTopology())
        
        for h in self.__protocol.getMessageHandlers():
            self.__dispatcher.registerMessageHandler(h)
            
        return self.__protocol
    
    @public
    def connect(self, priority):
        if self.__isConnected == True:
            return
        self.__protocol.connect(priority)
        self.__connectionTime = priority
        
    
    @public
    def disconnect(self, priority):
        if self.__isConnected == False:
            return
        self.__protocol.disconnect(priority)
    
    @public
    def connected(self):
        if self.__isConnected:
            return True
        self.__isConnected = True
        self.__network.increaseNumberOfConnectedPeers(self.__id)
        return self.__isConnected
    
    @public
    def disconnected(self):
        if not self.__isConnected:
            return
        self.__isConnected = False
        self.__network.decreaseNumberOfConnectedPeers(self.__id)
        return not self.__isConnected
    
    @public
    def getP2PNetwork(self):
        return self.__network
    
    @public
    def send(self, message):
        self.sendMessage(message)
        return message
    
    @public
    def sendMessage(self, message):
        return self.__protocol.sendMessage(message)
    
    @public
    def receive(self, message):
        if self.__id == message.getSourceId():
            return message
        self.receiveMessage(message)
        return message
    
    @public
    def receiveMessage(self, message):
        return self.__protocol.receiveMessage(message)
    
    @public
    def getMessageDispatcher(self):
        return self.__dispatcher
    
    @public
    def createConnection(self, targetId):
        self.__network.createConnection(self.__id, targetId)
        self.connected()
        return self.isConnected()
    
    @public
    def removeConnection(self, targetId):
        self.__network.removeConnection(self.__id, targetId)
        if self.__neighbors.has_key(targetId):
            del self.__neighbors[targetId]
        return not self.isConnected()
    
    @public
    def addContent(self, content):
        self.__contents[content.getId()] = content
        if not content.getId() in self.__sharedContent:
            self.__sharedContent.append(content.getId())
            content.addOwner(self.__id)
            for f in content.getFolksonomies():
                self.__profile.addFolksonomy(f)
        return self.__contents[content.getId()]
    
    @public
    def removeContent(self, id):
        if not self.__contents.has_key(id):
            raise StandardError()
        content = self.__contents[id]
        content.removeOwner(self.__id)
        for f in content.getFolksonomies():
            self.__profile.removeFolksonomy(f)
        del self.__contents[id]
        return content
    
    @public
    def countContents(self):
        return len(self.__contents)
    
    @public
    def getContents(self):
        return ImmutableSet(self.__contents.values())
    
    @public
    def getContentsByFolksonomy(self, folksonomy):
        contents = []
        for c in self.__contents.values():
            if c.hasFolksonomy(folksonomy):
                contents.append(c)
        return ImmutableSet(contents)
    
    @public
    def getProfile(self):
        return self.__profile
    
    
    def setProfile(self, profile):
        self.__profile = profile
        return self.__profile
    
    @public
    def advertise(self, type):
        if type == IPeer.CONTENT_ADVERTISEMENT:
            for c in self.__contents.values():
                self.__protocol.advertise(c, type)
    
    @public
    def share(self, type):
        pass
    
    @public
    def setConnectionTime(self, time):
        self.__connectionTime = time
    
    @public
    def getConnectionTime(self):
        return self.__connectionTime
    
    @public
    def specifyInterest(self):
        raise NotImplementedError()
    
    @public
    def getNeighbor(self, id):
        return self.__neighbors[id]
    
    @public
    def getNeighbors(self):
        return ImmutableSet(self.__neighbors.values())    
    
    @public
    def addNeighbor(self, neighbor):
        self.__neighbors[neighbor.getId()] = neighbor
    
    @public    
    def setDisconnectionTime(self, time):
        self.__disconnectionTime = time
    
    @public
    def getDisconnectionTime(self):
        return self.__disconnectionTime
    
    @public
    def setScheduledForDisconnection(self, flag):
        self.__scheduledDisconnection = flag
    
    @public
    def getScheduledForDisconnection(self):
        return self.__scheduledDisconnection
    
    @public
    def setDiskSpace(self, diskSpace):
        self.__diskSpace = diskSpace
    
    @public
    def getDiskSpace(self):
        return self.__diskSpace
    
    @public
    def createSocialCloud(self):
        raise NotImplementedError()
        
    @public    
    def getContent(self, id):
        return self.__contents[id]