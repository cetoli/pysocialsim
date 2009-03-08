from threading import Thread
from pysocialsim.network.peer.event.connection_event import ConnectionEvent
import time

class ConnectionEventGenerator(Thread):
    
    def __init__(self, peer):
        Thread.__init__(self)
        self.__peer = peer
        self.__active = False
        self.__priority = self.__peer.getAbsenceTime() / 100000000.0
    
    def generateEvents(self, simulation):
        self.__simulation = simulation
        self.start()
        
    def run(self):
        self.__active = True
        while self.__active:
            event = ConnectionEvent(self.__peer, self.__priority)
            self.__simulation.registerEvent(event)
            if not self.__active:
                return
            self.__priority += (self.__peer.getPermanenceTime() + self.__peer.getAbsenceTime()) / 100000000.0
    
    def stop(self):
        self.__active = False