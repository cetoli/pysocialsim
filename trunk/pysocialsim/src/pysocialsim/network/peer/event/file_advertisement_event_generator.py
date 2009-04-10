from pysocialsim.network.peer.event.file_advertisement_event import FileAdvertisementEvent

class FileAdvertisementEventGenerator:
    
    def __init__(self, peer):
        self.__peer = peer
        self.__priority = 0
        self.__time = 0
        self.__active = False
    
    def generateEvents(self, simulation):
        if not self.__peer.isConnected():
            return
        if self.__time % 3 == 0:
            self.__priority = simulation.getCurrentSimulationTime()
            
            event = FileAdvertisementEvent(self.__peer, self.__priority)
            simulation.registerEvent(event)
        else:
            self.__time + 1
      
        
    def stop(self):
        self.__active = False