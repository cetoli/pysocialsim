from pysocialsim.base.interface import Interface

class IDispatcher(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def handleEvent(self, event):
        raise NotImplementedError()
    
    def registerEventHandler(self, eventHandler):
        raise NotImplementedError()
    
    def unregisterEventHandler(self, handle):
        raise NotImplementedError()
    
    def countEventHandlers(self):
        raise NotImplementedError()
    
    def getEventHandlers(self):
        raise NotImplementedError()