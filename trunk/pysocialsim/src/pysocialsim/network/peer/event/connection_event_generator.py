from pysocialsim.network.peer.event.connection_event import ConnectionEvent

class ConnectionEventGenerator:
    
    def __init__(self, peer):
        self.__peer = peer
        self.__priority = 0.0
    
    def generateEvents(self, simulation):
        self.__simulation = simulation
        event = ConnectionEvent(self.__peer, self.__priority)
        self.__simulation.registerEvent(event)
        self.__priority += (self.__peer.getPermanenceTime() + self.__peer.getAbsenceTime()) / 100000000.0
        self.__peer.setCurrentTime(self.__peer.getCurrentTime() + self.__priority)
        
    def stop(self):
        self.__active = False