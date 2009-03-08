from pysocialsim.base.interface import Interface

class EventHandler(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def handleEvent(self, event):
        raise NotImplementedError()
    
    def clone(self):
        raise NotImplementedError()
    
    def getEvent(self):
        raise NotImplementedError()
    
    def getSimulation(self):
        raise NotImplementedError()
    
    def getHandle(self):
        raise NotImplementedError()