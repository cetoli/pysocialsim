"""
Defines the module with the implementation of PeerToPeerNetwork class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.util.rotines import requires, pre_condition, returns
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.base.decorators import public

class AbstractPeerToPeerNetwork(Object, IPeerToPeerNetwork):
    """
    Defines the abstract implementation of IPeerToPeerNetwork interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/10/2009
    """

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, simulation):
        requires(simulation, ISimulation)
        
        pre_condition(simulation, lambda x: x <> None)
        
        self.__simulation = simulation
        self.__peers = {IPeerToPeerNetwork.SUPER_PEER: {}, IPeerToPeerNetwork.SIMPLE_PEER: {}}
        self.__connectionsBetweenSuperPeers = 0
    
    @public
    def getSimulation(self):
        return returns(self.__simulation, ISimulation)

    @public
    def getConnectionsBetweenSuperPeers(self):
        return returns(self.__connectionsBetweenSuperPeers, int)

    @public
    def setSimulation(self, simulation):
        self.__simulation = simulation
        return returns(self.__simulation, ISimulation)

    @public
    def setConnectionsBetweenSuperPeers(self, connectionsBetweenSuperPeers):
        self.__connectionsBetweenSuperPeers = connectionsBetweenSuperPeers
        return returns(self.__connectionsBetweenSuperPeers, int)
    
    @public
    def addPeer(self, peerType, peer):
        return IPeerToPeerNetwork.addPeer(self, peerType, peer)

    @public
    def removePeer(self, peerType, peerId):
        return IPeerToPeerNetwork.removePeer(self, peerType, peerId)

    @public
    def getPeer(self, peerType, peerId):
        return IPeerToPeerNetwork.getPeer(self, peerType, peerId)

    @public
    def getPeers(self, peerType):
        return IPeerToPeerNetwork.getPeers(self, peerType)

    @public
    def countPeers(self, peerType):
        return IPeerToPeerNetwork.countPeers(self, peerType)

    @public
    def getConnectedPeers(self, peerType):
        return IPeerToPeerNetwork.getConnectedPeers(self, peerType)

    @public
    def getDisconnectedPeers(self, peerType):
        return IPeerToPeerNetwork.getDisconnectedPeers(self, peerType)
    
    simulation = property(getSimulation, setSimulation, None, None)

    connectionsBetweenSuperPeers = property(getConnectionsBetweenSuperPeers, setConnectionsBetweenSuperPeers, None, None)

    

        