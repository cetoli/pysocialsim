from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from sets import ImmutableSet
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.network.network import Network
from pysocialsim.base.decorator.require import require
from networkx.graph import Graph
from networkx.drawing.layout import spring_layout
from networkx.drawing.nx_pylab import draw_networkx_nodes
from networkx.drawing.nx_pylab import draw_networkx_edges
from matplotlib.pyplot import xticks
from matplotlib.pyplot import yticks
from threading import Semaphore
import pylab

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
        if not self.__graph.has_node(id):
            return ImmutableSet([])
        return ImmutableSet(self.__graph.neighbors(id))
    
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
    
    @public
    def show(self):
        pos = spring_layout(self.__graph)
        draw_networkx_nodes(self.__graph, pos, node_size = 200)
        draw_networkx_edges(self.__graph, pos, self.__graph.edges(), width = 1)
        xticks([])
        yticks([])
        pylab.show()
    
    @public    
    def createConnection(self, sourceId, targetId):
        sem = Semaphore()
        sem.acquire()
        self.__graph.add_edge(sourceId, targetId)
        sem.release()
    
    @public
    def removeConnection(self, sourceId, targetId):
        sem = Semaphore()
        sem.acquire()
        self.__graph.delete_edge(sourceId, targetId)
        sem.release()
    
    @public
    def addNode(self, id):
        self.__graph.add_node(id)
    
    @public
    def removeNode(self, id):
        if self.__graph.has_node(id):
            return
        self.__graph.delete_node(id)
        
    @public
    def dispatchMessage(self, message):
        peer = self.getNetwork().getPeer(message.getTargetId())
        peer.receive(message)