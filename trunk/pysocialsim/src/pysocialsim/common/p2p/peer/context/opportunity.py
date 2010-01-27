from pysocialsim.common.p2p.peer.context.abstract_context import AbstractContext
from pysocialsim.common.p2p.peer.context.i_opportunity import IOpportunity
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.peer.context.social_network import SocialNetwork

class Opportunity(AbstractContext, IOpportunity):
    
    def __init__(self, id):
        self.initialize(id)
    
    def initialize(self, id):
        AbstractContext.initialize(self, IContext.OPPORTUNITY, id)
        self.__durationTime = 0
        self.__startTime = 0
        self.__active = False
        self.__interestContraints = {}
        self.__socialNetwork = SocialNetwork(self)

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
    
    @public
    def addInterestConstraint(self, interestConstraint):
        if self.__interestContraints.has_key(interestConstraint.getConcept()):
            return False
        self.__interestContraints[interestConstraint.getConcept()] = interestConstraint
        return self.__interestContraints.has_key(interestConstraint.getConcept())
    
    @public
    def removeInterestConstraint(self, interestConstraint):
        if not self.__interestContraints.has_key(interestConstraint.getConcept()):
            return False
        del self.__interestContraints[interestConstraint.getConcept()]
        return not self.__interestContraints.has_key(interestConstraint.getConcept())
        
    @public
    def getInterestConstraint(self, concept):
        if not self.__interestContraints.has_key(concept):
            return None
        return self.__interestContraints[concept]
    
    @public
    def countInterestConstraint(self):
        return len(self.__interestContraints)
    
    @public
    def hasInterestConstraint(self, concept):
        return self.__interestContraints.has_key(concept)
    
    @public
    def getInterestConstraints(self):
        return self.__interestContraints.values()
    
    @public
    def clone(self):
        cln = Opportunity(self.getId())
        cln.setDurationTime(self.__durationTime)
        cln.setStartTime(self.__durationTime)
        if self.__active:
            cln.activate()
        for ic in self.__interestContraints.values():
            cln.addInterestConstraint(ic)
        
        return cln
    
    @public
    def getSocialNetwork(self):
        return self.__socialNetwork
    
    durationTime = property(getDurationTime, setDurationTime, None, None)

    startTime = property(getStartTime, setStartTime, None, None)