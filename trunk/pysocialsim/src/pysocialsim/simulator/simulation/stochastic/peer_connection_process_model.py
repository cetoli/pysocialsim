from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.event.peer_connection_event import PeerConnectionEvent

class PeerConnectionProcessModel(Object):
    
    def __init__(self, peersForConnection, entryTime):
        self.initialize(peersForConnection, entryTime)
    
    def initialize(self, peersForConnection, entryTime):
        self.__peersForConnection = peersForConnection
        self.__entryTime = entryTime
        self.__generatedEvents = 0
        self.__second = 0
        
    @public
    def generateEvents(self, simulation):
        network = simulation.getP2PNetwork()
        self.__second += 1
        self.__generatedEvents = 0
        if simulation.getSimulationCurrentTime() > 0:
            if self.__second % self.__entryTime == 0:
                id = network.getPeerForConnection()
                if id == None:
                    return self.__generatedEvents
                peer = network.getPeer(id)
                if peer.isConnected():
                    return self.__generatedEvents
                event = PeerConnectionEvent(peer, simulation.getSimulationCurrentTime())
                simulation.registerEvent(event)
                self.__generatedEvents += 1
        
        return self.__generatedEvents
        
