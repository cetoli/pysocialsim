from pysocialsim.base.interface import Interface

class IProfile(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def addFolksonomy(self, folksonomy):
        raise NotImplementedError()
    
    def removeFolksonomy(self, folksonomy):
        raise NotImplementedError()
    
    def countFolksonomies(self):
        raise NotImplementedError()
    
    def getPeer(self):
        raise NotImplementedError()
    
    def match(self, profile, strategy):
        raise NotImplementedError()
    
    def matchInterests(self, advertisement, strategy):
        raise NotImplementedError()
    
    def getFolksonomies(self):
        raise NotImplementedError()
    
    def addInterest(self, interest):
        raise NotImplementedError()
    
    