from pysocialsim.common.p2p.peer.context.abstract_context import AbstractContext
from pysocialsim.common.p2p.peer.context.i_opportunity import IOpportunity
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.base.decorators import public

class Opportunity(AbstractContext, IOpportunity):
    
    def __init__(self, id, peer):
        self.initialize(self, id, peer)
    
    def initialize(self, id, peer):
        AbstractContext.initialize(self, IContext.OPPORTUNITY, id, peer)
        self.__durationTime = 0
        self.__startTime = 0
        self.__active = False

    @public
    def getDurationTime(self):
        return self.__durationTime

    @public
    def getStartTime(self):
        return self.__startTime

    @public
    def setDurationTime(self, durationTime):
        self.__durationTime = durationTime

    @public
    def setStartTime(self, startTime):
        self.__startTime = startTime
        
    @public
    def getEndTime(self):
        return self.__startTime + self.__durationTime
    
    @public
    def activate(self):
        self.__active = True
        
    @public
    def deactivate(self):
        self.__active = False
        
    @public
    def isActive(self):
        return self.__active == True

    durationTime = property(getDurationTime, setDurationTime, None, None)

    startTime = property(getStartTime, setStartTime, None, None)