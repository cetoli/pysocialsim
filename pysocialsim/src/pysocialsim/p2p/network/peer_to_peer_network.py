"""
Defines the module with objective.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/04/2010
"""
from pysocialsim.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from Pyro.core import ObjBase

class PeerToPeerNetwork(IPeerToPeerNetwork, ObjBase):
    
    def __init__(self):
        ObjBase.__init__(self)
