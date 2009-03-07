from pysocialsim.network.topology.default_topology import DefaultTopology
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from types import NoneType

class UnstructuredTopology(DefaultTopology):
    
    def __init__(self):
        DefaultTopology.__init__(self)
        
    @public
    @return_type(NoneType)
    def connect(self, peer):
        pass
    
    @public
    @return_type(NoneType)
    def disconnect(self, peer):
        pass