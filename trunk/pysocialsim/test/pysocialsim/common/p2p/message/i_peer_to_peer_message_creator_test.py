"""
Defines the module with unit test of IPeerToPeerMessageCreator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 15/10/2009
"""
from pysocialsim.common.p2p.message.i_peer_to_peer_message_creator import IPeerToPeerMessageCreator

import unittest

class IPeerToPeerMessageCreatorTest(unittest.TestCase):
    
    def testTryCreateInterfaceInstance(self):
        self.assertRaises(NotImplementedError, IPeerToPeerMessageCreator)
        
    