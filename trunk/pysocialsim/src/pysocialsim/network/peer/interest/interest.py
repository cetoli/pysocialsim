from pysocialsim.base.interface import Interface

class Interest(object):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getFolksonomy(self):
        raise NotImplementedError()
    
    def addReputation(self, reputation):
        raise NotImplementedError()
    
    def removeReputation(self, index):
        raise NotImplementedError()
    
    def countReputations(self):
        raise NotImplementedError()
    
    def getReputations(self):
        raise NotImplementedError()
    
    def calculateReputationDegree(self, reputationMetric):
        raise NotImplementedError()