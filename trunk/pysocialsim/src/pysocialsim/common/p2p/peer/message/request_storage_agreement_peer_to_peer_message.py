'''
Created on 01/02/2010

@author: fabricio
'''
from pysocialsim.common.p2p.message.abstract_peer_to_peer_message import AbstractPeertoPeerMessage
from pysocialsim.common.p2p.message.i_peer_to_peer_message import IPeerToPeerMessage

class RequestStorageAgreementPeerToPeerMessage(AbstractPeertoPeerMessage):
    
    def __init__(self):
        AbstractPeertoPeerMessage.initialize(self, IPeerToPeerMessage.ADVERTISEMENT, "REQUEST_STORAGE_AGREEMENT", 512)