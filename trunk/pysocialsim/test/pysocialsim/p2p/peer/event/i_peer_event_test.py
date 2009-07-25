from pysocialsim.p2p.peer.event.i_peer_event import IPeerEvent
import unittest

class IPeerEventTest(unittest.TestCase):
    
    def test_try_create_i_peer_event(self):
        self.assertRaises(NotImplementedError, IPeerEvent)