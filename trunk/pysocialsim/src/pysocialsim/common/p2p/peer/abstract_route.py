"""
Defines the module with the implementation of AbstractRoute class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 20/10/2009
"""
from pysocialsim.common.base.object import Object
from pysocialsim.common.p2p.peer.i_route import IRoute
from pysocialsim.common.base.decorators import public

class AbstractRoute(Object, IRoute):
    """
    classdocs
    """

    def __init__(self):
        raise NotImplementedError()

    def initialize(self, peerId, trace, cost, freshness):
        self.__peerId = peerId
        self.__trace = trace
        self.__freshness = freshness
        self.__cost = cost
        self.__tags = {}
    
    @public    
    def getPeerId(self):
        return self.__peerId

    @public
    def getTrace(self):
        return self.__trace

    @public
    def getFreshness(self):
        return self.__freshness

    @public
    def getCost(self):
        return self.__cost

    @public
    def getTags(self):
        return self.__tags.keys()

    @public
    def setTrace(self, value):
        self.__trace = value

    @public
    def setFreshness(self, value):
        self.__freshness = value

    @public
    def setCost(self, value):
        self.__cost = value
       
    @public
    def registerTag(self, tag):
        if not self.__tags.has_key(tag):
            self.__tags[tag] = 1
        else:
            self.__tags[tag] += 1
        return self.__tags[tag]

    @public
    def unregisterTag(self, tag):
        incidence = 0
        
        if self.__tags.has_key(tag):
            self.__tags[tag] -= 1
            incidence = self.__tags[tag]
            if incidence == 0:
                del self.__tags[tag]
            
        return incidence

    @public
    def countTags(self):
        return len(self.__tags)

    @public
    def getTagIncidence(self, tag):
        return self.__tags[tag]



    peerId = property(getPeerId, None, None, None)

    trace = property(getTrace, setTrace, None, None)

    freshness = property(getFreshness, setFreshness, None, None)

    cost = property(getCost, setCost, None, None)

    tags = property(getTags, None, None, None)