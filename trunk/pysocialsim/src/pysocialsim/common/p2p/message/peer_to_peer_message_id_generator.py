"""
Defines the module with the implementation PeerToPeerMessageIdGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
from pysocialsim.common.util.rotines import requires, pre_condition
from pysocialsim.common.p2p.peer.i_peer import IPeer
import sha
import random
import time

class PeerToPeerMessageIdGenerator(object):
    """
    Implements the generator for peer-to-peer message identifiers.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 11/10/2009
    """

    def __init__(self):
        raise NotImplementedError()
    
    @classmethod
    def generatePeerToPeerMessageId(self, peer):
        requires(peer, IPeer)
        pre_condition(peer, lambda x: x <> None)
        
        id = "urn:message:id:"+sha.new(str(peer.getType()) + peer.getId() + str(random.random() * 100000000000000000) + str(time.time())).hexdigest()
        
        return id