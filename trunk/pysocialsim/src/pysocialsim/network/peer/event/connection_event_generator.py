from pysocialsim.network.peer.event.connection_event import ConnectionEvent

class ConnectionEventGenerator:
    
    def __init__(self, peer):
        self.__peer = peer
        self.__priority = self.__peer.getAbsenceTime()
    
    def generateEvents(self, simulation):
        #if ((simulation.getCurrentSimulationTime() % simulation.getPeerConnectionFrequency()) + self.__peer.getId()) == self.__peer.getId(): 
            if not self.__peer.isConnected():
                if simulation.getCurrentSimulationTime() == self.__priority:
                    event = ConnectionEvent(self.__peer, self.__priority)
                    simulation.registerEvent(event)
                    self.__priority = self.__peer.getPermanenceTime() + self.__peer.getAbsenceTime()
        
    def stop(self):
        self.__active = False