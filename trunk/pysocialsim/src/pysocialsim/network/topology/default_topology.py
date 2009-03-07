from pysocialsim.network.topology.abstract_topology import AbstractTopology
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from types import NoneType

class DefaultTopology(AbstractTopology):
    
    def __init__(self):
        self.initialize()
        
    @public
    @return_type(NoneType)
    def connect(self, peer):
        pass
    
    @public
    @return_type(NoneType)
    def disconnect(self, peer):
        pass