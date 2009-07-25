from pysocialsim.base.object import Object
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.simulation.i_simulation import ISimulation
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.event.i_event import IEvent
from pysocialsim.simulator.dispatcher.i_event_handler import IEventHandler

class AbstractEventHandler(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, handle, simulation):
        self.__event = None
        self.__handle = handle
        self.__simulation = simulation
        
    @public
    def getEvent(self):
        return self.__event
    
    @public
    def clone(self):
        raise NotImplementedError()
    
    @public
    def handleEvent(self, event):
        self.__event = event
        self.executeHandler(event)
        return self.__event.handled()
        
    @public
    def getSimulation(self):
        return self.__simulation
    
    @public
    def getHandle(self):
        return self.__handle
    
    @require("event", IEvent)
    def executeHandler(self, event):
        raise NotImplementedError()