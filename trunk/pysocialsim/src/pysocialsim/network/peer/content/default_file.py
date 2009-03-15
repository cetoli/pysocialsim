from pysocialsim.network.peer.content.abstract_file import AbstractFile

class DefaultFile(AbstractFile):
    
    def __init__(self, id, concept, folksonomies):
        self.initialize(id, concept, folksonomies)