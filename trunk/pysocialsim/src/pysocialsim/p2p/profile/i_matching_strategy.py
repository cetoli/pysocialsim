from pysocialsim.base.interface import Interface

class IMatchingStrategy(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def execute(self, source, target):
        raise NotImplementedError()