from pysocialsim.p2p.network.default_p2p_network import DefaultP2PNetwork
from pysocialsim.base.object import Object
from pysocialsim.p2p.peer.default_peer import DefaultPeer
from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.topology.i_p2p_topology import IP2PTopology
from pysocialsim.base.decorator.require import require
from pysocialsim.base.decorator.return_type import return_type
from types import NoneType
from pysocialsim.p2p.network.i_p2p_network import IP2PNetwork

class DefaultP2PNetworkBuilder(Object):
    
    def __init__(self):
        self.__network = None
    
    @public
    def createP2PNetwork(self, topology):
        self.__network = DefaultP2PNetwork(topology)
    
    @public
    def buildP2PNetwork(self, params):
        if not params.has_key("peers"):
            raise StandardError()
        peers = params["peers"]
        peerConf = params["peer"]
        
        protocol = peerConf["protocol"]
        module = __import__(protocol["module"], globals, locals, [protocol["className"]], -1)
        protocolClass = module.__getattribute__(protocol["className"])
        
        builder = peerConf["builder"]
        module = __import__(builder["module"], globals, locals, [builder["className"]], -1)
        peerBuilderClass = module.__getattribute__(builder["className"])
        builder = peerBuilderClass()
        
        strategy = peerConf["matchingStrategy"]
        module = __import__(strategy["module"], globals, locals, [strategy["className"]], -1)
        matchingStrategyClass = module.__getattribute__(strategy["className"])
        
        print "Building peers."
        
        for id in range(1, peers + 1):
            peer = DefaultPeer(id, self.__network, protocolClass(), matchingStrategyClass())
            self.__network.addPeer(peer)
        print "Building peers is done."

    @public
    def getP2PNetwork(self):
        return self.__network