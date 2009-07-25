from pysocialsim.p2p.dispatcher.i_message_handler import IMessageHandler
import unittest

class IMessageHandlerTest(unittest.TestCase):
    
    def test_try_create_i_message_handler(self):
        self.assertRaises(NotImplementedError, IMessageHandler)