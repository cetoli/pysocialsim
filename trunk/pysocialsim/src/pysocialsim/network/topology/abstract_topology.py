from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from sets import ImmutableSet
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.network.network import Network
from pysocialsim.base.decorator.require import require
from networkx.graph import Graph

class AbstractTopology(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self):
        self.__network = None
        self.__graph = Graph().to_undirected()
    
    @public
    def connect(self, peer):
        raise NotImplementedError()
    
    @public
    def disconnect(self, peer):
        raise NotImplementedError()
    
    @public
    @return_type(ImmutableSet)
    def getNeighbors(self, id):
        return ImmutableSet(self.__graph.neighbors_iter())
    
    @public
    @return_type(Network)
    @require("network", Network)
    def setNetwork(self, network):
        self.__network = network
        return self.__network
    
    @public
    @return_type(Network)
    def getNetwork(self):
        return self.__network
    
    @public
    @return_type(Graph)
    def getGraph(self):
        return self.__graph