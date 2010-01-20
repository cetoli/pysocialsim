from pysocialsim.common.p2p.peer.context.i_context import IContext

class IOpportunity(IContext):
    
    def setStartTime(self, startTime):
        raise NotImplementedError()
    
    def getStartTime(self):
        raise NotImplementedError()
    
    def setDurationTime(self, durationTime):
        raise NotImplementedError()
    
    def getDurationTime(self):
        raise NotImplementedError()
    
    def getEndTime(self):
        raise NotImplementedError()
    
    def activate(self):
        raise NotImplementedError()
    
    def deactivate(self):
        raise NotImplementedError()
    
    def isActive(self):
        raise NotImplementedError()
    
    def addInterestConstraint(self, interestConstraint):
        raise NotImplementedError()
    
    def removeInterestConstraint(self, interestConstraint):
        raise NotImplementedError()
    
    def getInterestConstraint(self, concept):
        raise NotImplementedError()
    
    def countInterestConstraint(self):
        raise NotImplementedError()
    
    def hasInterestConstraint(self, concept):
        raise NotImplementedError()
    
    def getInterestConstraints(self):
        raise NotImplementedError()