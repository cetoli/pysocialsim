from pysocialsim.p2p.peer.event.abstract_peer_event import AbstractPeerEvent
import unittest

class AbstractPeerEventTest(unittest.TestCase):
    
    def test_try_create_abstract_event(self):
        self.assertRaises(NotImplementedError, AbstractPeerEvent)