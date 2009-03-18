from pysocialsim.network.topology.default_topology import DefaultTopology
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from types import NoneType
from random import randint
from threading import Semaphore
from pysocialsim.network.peer.message.connect_message import ConnectMessage
from pysocialsim.network.peer.message.disconnect_message import DisconnectMessage

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
        if len(graph) > 0:
            nodes = graph.nodes()
            node = randint(0, len(nodes) - 1)
        
        self.addNode(peer.getId())
        if node:
            network = self.getNetwork()
            simulation = network.getSimulation()
            connect = ConnectMessage(peer.getId(), node, simulation.getTTL())
            peer.send(connect)

        sem.release()
    
    @public
    @return_type(NoneType)
    def disconnect(self, peer):
        sem = Semaphore()
        sem.acquire()
        if not peer.isConnected():
            return
        neighbors = self.getNeighbors(peer.getId())
        network = self.getNetwork()
        simulation = network.getSimulation()
        for n in neighbors:
            message = DisconnectMessage(peer.getId(), n, simulation.getTTL())
            peer.send(message)
        sem.release()
    
    