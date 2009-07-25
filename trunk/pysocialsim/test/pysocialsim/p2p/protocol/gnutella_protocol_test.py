from pysocialsim.p2p.protocol.gnutella_protocol import GnutellaProtocol
from pysocialsim.base.interface import implements
from pysocialsim.p2p.protocol.i_p2p_protocol import IP2PProtocol
import unittest

class GnutellaProtocolTest(unittest.TestCase):
    
    def setUp(self):
        self.__protocol = GnutellaProtocol()
        
    def test_implements_interface(self):
        self.assertTrue(implements(self.__protocol, IP2PProtocol))