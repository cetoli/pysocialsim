from pysocialsim.p2p.content.abstract_content import AbstractContent

class DefaultContent(AbstractContent):
    
    def __init__(self, id, folksonomies, size):
        self.initialize(id, folksonomies, size)