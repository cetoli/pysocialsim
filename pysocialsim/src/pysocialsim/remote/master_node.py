"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/04/2010
"""
from threading import Thread
from Pyro.core import Daemon, ObjBase
from Pyro.naming import NameServerLocator
from pysocialsim.p2p.network.peer_to_peer_network import PeerToPeerNetwork

class MasterNode(Thread):
    
    def __init__(self, ):
        Thread.__init__(self)
        self.__daemon = Daemon()
        self.__daemon.useNameServer(NameServerLocator().getNS())
        
    def run(self):
        self.__daemon.connect(self.MasterNodeRemoteObject(self.__daemon), "PYRONAME://master")
        print "Registering master node service."
        self.__daemon.connect(PeerToPeerNetwork(), "PYRONAME://network")
        print "Registering peer-to-peer network service."
        self.__daemon.requestLoop()
        
    class MasterNodeRemoteObject(ObjBase):
        
        def __init__(self, daemon):
            ObjBase.__init__(self)
            self.__daemon = daemon
            
            
        