from pysocialsim.base.object import Object
from pysocialsim.base.decorator.return_type import return_type
from types import NoneType
from pysocialsim.base.decorator.require import require
from pysocialsim.base.decorator.public import public
from pysocialsim.simulator.event.i_event import IEvent
from pysocialsim.simulator.dispatcher.i_event_handler import IEventHandler
from threading import Thread
from sets import ImmutableSet
import time

class DefaultDispatcher(Object):
    
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        self.__eventHandlers = {}
    
    @public
    def handleEvent(self, event):
        if not self.__eventHandlers.has_key(event.getHandle()):
            return False
        DefaultDispatcher.EventHandlingThread(self.__eventHandlers[event.getHandle()], event).start()
        return event.isHandled()
    
    @public
    def registerEventHandler(self, eventHandler):
        if self.__eventHandlers.has_key(eventHandler.getHandle()):
            return False
        self.__eventHandlers[eventHandler.getHandle()] = eventHandler
        return self.__eventHandlers.has_key(eventHandler.getHandle())
    
    @public
    def unregisterEventHandler(self, handle):
        if not self.__eventHandlers.has_key(handle):
            return False
        del self.__eventHandlers[handle]
        return not self.__eventHandlers.has_key(handle)
    
    @public
    def countEventHandlers(self):
        return len(self.__eventHandlers)
    
    @public
    def getEventHandlers(self):
        return ImmutableSet(self.__eventHandlers.values())
    
    
    class EventHandlingThread(Thread):
        
        @require("handler", IEventHandler)
        @require("event", IEvent)
        def __init__(self, handler, event):
            Thread.__init__(self)
            self.__handler = handler.clone()
            self.__event = event
            
        def run(self):
            
            self.__handler.handleEvent(self.__event)
            self.__event.handled()
            
            peer = self.__event.getPeer()
            network = peer.getP2PNetwork()
            
            line = self.__event.getPriority(), self.__event.getHandle(), self.__event.getPeer().getId(), network.countConnectedPeers()
            
            self.__dispatcherLogFile = open("simulation.log", "a")
            self.__dispatcherLogFile.write(str(line)+"\n")
            self.__dispatcherLogFile.close()