from pysocialsim.base.interface import Interface

class File(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getId(self):
        raise NotImplementedError()
    
    def addFolksonomy(self, folksonomy):
        raise NotImplementedError()
    
    def removeFolksonomy(self, folksonomy):
        raise NotImplementedError()
    
    def countFolksonomies(self):
        raise NotImplementedError()
    
    def getFolksonomies(self):
        raise NotImplementedError()
    
    def addOwner(self, peerId):
        raise NotImplementedError()
    
    def removeOwner(self, peerId):
        raise NotImplementedError()
    
    def countOwners(self):
        raise NotImplementedError()
    
    def getOwners(self):
        raise NotImplementedError()
    
    def getConcept(self):
        raise NotImplementedError()