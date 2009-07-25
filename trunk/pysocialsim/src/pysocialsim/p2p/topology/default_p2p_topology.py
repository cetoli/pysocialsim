from pysocialsim.p2p.topology.abstract_p2p_topology import AbstractP2PTopology
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.base.decorator.require import require
from pysocialsim.p2p.peer.i_peer import IPeer
from threading import Semaphore
from random import randint

class DefaultP2PTopology(AbstractP2PTopology):
    
    def __init__(self):
        self.initialize()
        
    @public
    def connect(self, peer):
        pass
        
    @public
    def disconnect(self, peer):
        raise NotImplementedError()