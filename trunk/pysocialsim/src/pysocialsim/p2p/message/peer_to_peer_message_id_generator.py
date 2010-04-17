"""
Defines the module with the implementation PeerToPeerMessageIdGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 11/10/2009
"""
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
        id = "urn:message:id:"+sha.new(str(peer.getType()) + peer.getId() + str(random.random() * 100000000000000000) + str(time.time())).hexdigest()
        
        return id