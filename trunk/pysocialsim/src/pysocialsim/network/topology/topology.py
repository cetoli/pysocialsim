from pysocialsim.base.interface import Interface

class Topology(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()