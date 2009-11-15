"""
Defines the module with the ContextIdGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 06/11/2009
"""
from pysocialsim.common.util.rotines import requires
from pysocialsim.common.p2p.peer.i_peer import IPeer
import random
import sha

class ContextIdGenerator(object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @classmethod
    def generateContextId(self, type, peer):
        requires(type, str)
        requires(peer, IPeer)
       
        return "urn:" + type.lower() + ":id:" + sha.new(peer.getId() + type + str(random.random()*100000000000000000)).hexdigest()