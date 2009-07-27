from pysocialsim.p2p.dispatcher.abstract_message_handler import AbstractMessageHandler
from pysocialsim.base.decorator.public import public

class CreateRelationshipMessageHandler(AbstractMessageHandler):
    
    def __init__(self, peer):
        self.initialize("CREATE_RELATIONSHIP", peer)
    
    @public
    def clone(self):
        return CreateRelationshipMessageHandler(self.getPeer())
    
    def executeHandler(self):
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", self.getMessageName()
        