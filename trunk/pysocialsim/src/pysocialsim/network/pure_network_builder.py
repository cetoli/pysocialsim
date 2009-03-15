from pysocialsim.network.abstract_network_builder import AbstractNetworkBuilder
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.require import require
from pysocialsim.network.topology.topology import Topology
from pysocialsim.network.pure_network import PureNetwork
from pysocialsim.network.peer.default_peer import DefaultPeer
from random import randint
from pysocialsim.network.peer.message.default_message_dispatcher import DefaultMessageDispatcher
from pysocialsim.network.peer.message.connect_message_handler import ConnectMessageHandler
from pysocialsim.network.peer.message.ok_connect_message_handler import OKConnectMessageHandler
from pysocialsim.network.peer.message.disconnect_message_handler import DisconnectMessageHandler
from pysocialsim.network.peer.message.ok_disconnect_message_handler import OKDisconnectMessageHandler

class PureNetworkBuilder(AbstractNetworkBuilder):
    
    def __init__(self):
        self.setNetwork(None)
    
    @public    
    def buildNetwork(self, **params):
        if not params.has_key("peers"):
            return 0
        peers = 0
        for id in range(params["peers"]):
            peer = DefaultPeer(id, self.getNetwork(), randint(params["min_permanence"], params["max_permanence"]), randint(params["min_absence"], params["max_absence"]))
            dispatcher = DefaultMessageDispatcher(peer)
            dispatcher.registerMessageHandler(ConnectMessageHandler(peer))
            dispatcher.registerMessageHandler(OKConnectMessageHandler(peer))
            dispatcher.registerMessageHandler(DisconnectMessageHandler(peer))
            dispatcher.registerMessageHandler(OKDisconnectMessageHandler(peer))
            self.getNetwork().addPeer(peer)
            peers += 1
            
        return peers
    
    @public
    @require("topology", Topology)
    def createNetwork(self, topology):
        self.setNetwork(PureNetwork(topology))
        return self.getNetwork()
    
