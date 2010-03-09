"""
Defines the module with unit test for IPeer interface.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 23/08/2009
"""
from pysocialsim.common.p2p.peer.i_peer import IPeer

import unittest

class IPeerTest(unittest.TestCase):
    
    def testTryInstantiateIPeerInterface(self):
        self.assertRaises(NotImplementedError, IPeer)
        
    def testTryInvokeGetId(self):
        self.assertRaises(NotImplementedError, self.PeerForTest().getId)
        
    def testTryInvokeGetType(self):
        self.assertRaises(NotImplementedError, self.PeerForTest().getType)
        
        
    class PeerForTest(IPeer):
        
        def __init__(self):
            pass