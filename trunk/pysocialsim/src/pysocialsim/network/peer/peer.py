from pysocialsim.base.interface import Interface

class Peer(object):

    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()