from pysocialsim.base.interface import Interface

class Simulator(object):

    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def handleEvent(self, event):
        raise NotImplementedError()
    
    def setDispatcher(self, dispatcher):
        raise NotImplementedError()
    
    def getSimulation(self):
        raise NotImplementedError()