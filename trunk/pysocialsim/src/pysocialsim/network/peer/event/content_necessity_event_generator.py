from pysocialsim.network.peer.event.content_necessity_event import ContentNecessityEvent

class ContentNecessityEventGenerator:
    
    def __init__(self, peer):
        self.__peer = peer
        self.__priority = 0
        self.__active = False
    
    def generateEvents(self, simulation):
        if not self.__peer.isConnected():
            return
        self.__priority = simulation.getCurrentSimulationTime()
        event = ContentNecessityEvent(self.__peer, self.__priority)
        simulation.registerEvent(event)
      
        
    def stop(self):
        self.__active = False