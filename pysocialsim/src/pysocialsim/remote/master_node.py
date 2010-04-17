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

class MasterNode(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.__daemon = Daemon()
        self.__daemon.useNameServer(NameServerLocator().getNS())
    
    def registerRemoteObject(self, obj, name):
        self.__daemon.connect(obj, name)
    
    def run(self):
        self.__daemon.requestLoop()
        
    class MasterNodeRemoteObject(ObjBase):
        
        def __init__(self, daemon):
            ObjBase.__init__(self)
            self.__daemon = daemon
            
            
        