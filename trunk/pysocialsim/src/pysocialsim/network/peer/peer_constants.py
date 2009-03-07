from pysocialsim.base.interface import Interface

class PeerConstants(object):
    
    DEFAULT_PEER = 0
    SIMPLE_PEER = 1
    SUPER_PEER = 2
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()