from pysocialsim.network.peer.event.disconnection_event import DisconnectionEvent

class DisconnectionEventGenerator:
    
    def __init__(self, peer):
        self.__peer = peer
        self.__active = False
        self.__priority = self.__peer.getPermanenceTime()
    
    def generateEvents(self, simulation):
        if self.__peer.isConnected():
            if simulation.getCurrentSimulationTime() == self.__priority:
                event = DisconnectionEvent(self.__peer, self.__priority)
                simulation.registerEvent(event)
                print "disconnect"
                self.__priority = self.__peer.getPermanenceTime() + self.__peer.getAbsenceTime()
    
    def stop(self):
        self.__active = False