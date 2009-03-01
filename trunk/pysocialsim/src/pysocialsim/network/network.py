from pysocialsim.base.interface import Interface

class Network(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()