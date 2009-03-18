from pysocialsim.network.peer.event.file_advertisement_event import FileAdvertisementEvent

class FileAdvertisementEventGenerator:
    
    def __init__(self, peer):
        self.__peer = peer
        self.__priority = 0
        self.__active = False
    
    def generateEvents(self, simulation):
        if not self.__peer.isConnected():
            return
        self.__priority = self.__peer.getCurrentTime()
        event = FileAdvertisementEvent(self.__peer, self.__priority)
        simulation.registerEvent(event)
      
        
    def stop(self):
        self.__active = False