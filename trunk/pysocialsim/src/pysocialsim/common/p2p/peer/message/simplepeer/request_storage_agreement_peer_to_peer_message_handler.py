'''
Created on 02/02/2010

@author: fabricio
'''
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message_handler import AbstractPeerToPeerMessageHandler

class RequestStorageAgreementPeerToPeerMessageHandler(AbstractPeerToPeerMessageHandler):
    
    def __init__(self):
        AbstractPeerToPeerMessageHandler.initialize(self, "REQUEST_STORAGE_AGREEMENT")
        
    def execute(self):
        peer = self.getPeer()
        if not peer.isJoined():
            return
        
        message = self.getPeerToPeerMessage()
        print self.getHandle()