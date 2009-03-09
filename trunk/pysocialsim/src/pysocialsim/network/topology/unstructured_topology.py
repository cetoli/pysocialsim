from pysocialsim.network.topology.default_topology import DefaultTopology
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from types import NoneType
from random import randint
from threading import Semaphore

class UnstructuredTopology(DefaultTopology):
    
    def __init__(self):
        DefaultTopology.__init__(self)
        
    @public
    @return_type(NoneType)
    def connect(self, peer):
        sem = Semaphore()
        sem.acquire()
        if peer.isConnected():
            return
        graph = self.getGraph()
        
        node = None
        if len(graph.nodes()) > 0:
            nodes = graph.nodes()
            node = randint(0, len(nodes) - 1)
                
        graph.add_node(peer.getId())
        if node <> None:
            graph.add_edge(peer.getId(), node)
        sem.release()
    
    @public
    @return_type(NoneType)
    def disconnect(self, peer):
        sem = Semaphore()
        sem.acquire()
        if not peer.isConnected():
            return
        graph = self.getGraph()
        graph.delete_node(peer.getId())
        sem.release()
    
    @public
    def dispatchMessage(self, message):
        pass