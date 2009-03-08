from pysocialsim.base.object import Object
from pysocialsim.simulator.simulator import Simulator
from pysocialsim.base.decorator.require import require
from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.simulation.event.event import Event
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.dispatcher.event_handler import EventHandler

class AbstractDispatcher(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @require("simulator", Simulator)
    def initialize(self, simulator):
        self.__eventHandlers = {}
        self.__simulator = simulator
        self.__simulator.setDispatcher(self)
    
    @public
    @require("event", Event)    
    def handleEvent(self, event):
        if not self.__eventHandlers.has_key(event.getHandle()):
            return False
        clone = self.__eventHandlers[event.getHandle()].clone()
        return clone.handleEvent(event)
    
    @public
    @return_type(bool)
    @require("eventHandler", EventHandler)
    def registerEventHandler(self, eventHandler):
        if self.__eventHandlers.has_key(eventHandler.getHandle()):
            return False
        self.__eventHandlers[eventHandler.getHandle()] = eventHandler
        return True
    
    @public
    @return_type(bool)
    @require("handle", str)
    def unregisterEventHandler(self, handle):
        if not self.__eventHandlers.has_key(handle):
            return False
        del self.__eventHandlers[handle]
        return True
    
    @public
    @return_type(int)
    def countEventHandlers(self):
        return len(self.__eventHandlers)