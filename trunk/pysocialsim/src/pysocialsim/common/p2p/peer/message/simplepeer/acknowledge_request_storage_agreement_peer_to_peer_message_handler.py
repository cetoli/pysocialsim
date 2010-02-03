'''
Created on 02/02/2010

@author: fabricio
'''

from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler

class RequestStorageAgreementPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "ACK_REQUEST_STORAGE_AGREEMENT")
        
    def execute(self):
        print self.getHandle()            