from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require
from pysocialsim.network.network_builder import NetworkBuilder

class NetworkBuilderDirector(Object):
    
    @require("builder", NetworkBuilder)
    def __init__(self, builder):
        self.__builder = builder
    
    @public
    def build(self, topology, **params):
        self.__builder.createNetwork(topology)
        self.__builder.buildNetwork(**params)