from pysocialsim.p2p.dispatcher.abstract_message_handler import AbstractMessageHandler
import unittest

class AbstractMessageHandlerTest(unittest.TestCase):
    
    def test_try_create_abstract_message_handler_test(self):
        self.assertRaises(NotImplementedError, AbstractMessageHandler)