from pysocialsim.p2p.content.abstract_content import AbstractContent
from pysocialsim.base.decorator.public import public

class DefaultContent(AbstractContent):
    
    def __init__(self, id, folksonomies, size):
        self.initialize(id, folksonomies, size)
    
    @public    
    def clone(self):
        clone = DefaultContent(self.getId(), self.getFolksonomies(), self.getSize())
        for o in self.getOwners():
            clone.addOwner(o)
        
        return clone