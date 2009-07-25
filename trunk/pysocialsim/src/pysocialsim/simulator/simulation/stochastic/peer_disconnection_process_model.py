from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.event.peer_disconnection_event import PeerDisconnectionEvent

class PeerDisconnectionProcessModel(Object):
    
    def __init__(self, peersForDisconnection, exitTime):
        self.initialize(peersForDisconnection, exitTime)
    
    def initialize(self, peersForDisconnection, exitTime):
        self.__peersForDisconnection = peersForDisconnection
        self.__exitTime = exitTime
        self.__generatedEvents = 0
        self.__second = 0
        
    @public
    def generateEvents(self, simulation):
        network = simulation.getP2PNetwork()
        self.__second += 1
        self.__generatedEvents = 0
        id = network.getPeerForDisconnection()
        if id == None:
            return self.__generatedEvents
        
        peer = network.getPeer(id)
        if self.__second % (peer.getConnectionTime() + self.__exitTime) == 0:
            if not peer.isConnected():
                return self.__generatedEvents
            print "blalalalalalalalalala"
            event = PeerDisconnectionEvent(peer, simulation.getSimulationCurrentTime())
            simulation.registerEvent(event)
            self.__generatedEvents += 1
            
        return self.__generatedEvents