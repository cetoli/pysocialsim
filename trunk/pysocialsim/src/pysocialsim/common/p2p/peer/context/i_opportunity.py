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