from pysocialsim.base.object import Object
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.simulation.simulation import Simulation
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.simulation.event.event import Event
from pysocialsim.simulator.dispatcher.event_handler import EventHandler
from copy import copy

class AbstractEventHandler(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @require("handle", str)
    @require("simulation", Simulation)
    def initialize(self, handle, simulation):
        self.__event = None
        self.__handle = handle
        self.__simulation = simulation
        
    @public
    @return_type(Event)
    def getEvent(self):
        return self.__event
    
    @public
    @return_type(EventHandler)
    def clone(self):
        raise NotImplementedError()
    
    @public
    @require("event", Event)
    def handleEvent(self, event):
        self.__event = event
        self.executeHandler(event)
        return self.__event.handled()
        
    @public
    @return_type(Simulation)
    def getSimulation(self):
        return self.__simulation
    
    @public
    @return_type(str)
    def getHandle(self):
        return self.__handle
    
    @require("event", Event)
    def executeHandler(self, event):
        raise NotImplementedError()