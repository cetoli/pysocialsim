from threading import Thread
from pysocialsim.network.peer.event.disconnection_event import DisconnectionEvent

class DisconnectionEventGenerator:
    
    def __init__(self, peer):
        self.__peer = peer
        self.__active = False
        self.__priority = (self.__peer.getPermanenceTime() + self.__peer.getAbsenceTime()) / 100000000.0
    
    def generateEvents(self, simulation):
        self.__simulation = simulation
        event = DisconnectionEvent(self.__peer, self.__priority)
        self.__simulation.registerEvent(event)
        self.__priority += (self.__peer.getPermanenceTime() + self.__peer.getAbsenceTime()) / 100000000.0
    
    def stop(self):
        self.__active = False