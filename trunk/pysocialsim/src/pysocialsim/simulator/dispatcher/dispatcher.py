from pysocialsim.base.interface import Interface

class Dispatcher(object):

    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def handleEvent(self, event):
        raise NotImplementedError()