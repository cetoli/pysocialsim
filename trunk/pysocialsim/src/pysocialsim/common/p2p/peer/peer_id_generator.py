"""
Defines the module with the implementation of PeerIdGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.util.rotines import requires, pre_condition
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
import random
import sha

class PeerIdGenerator(object):
    """
    classdocs
    """

    def __init__(self):
        raise NotImplementedError()
    
    @classmethod
    def generatePeerId(self, peerType):
        requires(peerType, int)
        pre_condition(peerType, lambda x: peerType == IPeerToPeerNetwork.SIMPLE_PEER or peerType == IPeerToPeerNetwork.SUPER_PEER)
        
        id = "urn:"
        if peerType == IPeerToPeerNetwork.SUPER_PEER:
            id += "superpeer:id:"+sha.new(str(peerType)+str(random.random()*100000000000000000)).hexdigest()
        elif peerType == IPeerToPeerNetwork.SIMPLE_PEER:
            id += "simplepeer:id:"+sha.new(str(peerType)+str(random.random()*100000000000000000)).hexdigest()
            
        return id