from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require
from pysocialsim.network.network_builder import NetworkBuilder

class NetworkBuilderDirector(Object):
    
    @require("builder", NetworkBuilder)
    def __init__(self, builder):
        self.__builder = builder
    
    @public
    def build(self, topology, protocol, **params):
        self.__builder.createNetwork(topology, protocol)
        self.__builder.buildNetwork(**params)