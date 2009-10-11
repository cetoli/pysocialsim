"""
Defines the module with the implementations PeerToPeerTopology class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.p2p.topology.abstract_peer_to_peer_topology import AbstractPeerToPeerTopology

class PeerToPeerTopology(AbstractPeerToPeerTopology):
    """
    Defines the concrete implementation of IPeerToPeerTopology interface.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/10/2009
    """
    
    def __init__(self):
        AbstractPeerToPeerTopology.initialize(self)
        