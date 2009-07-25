from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class AbstractNeighbor(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    def initialize(self, peer, id):
        self.__peer = peer
        self.__id = id
        self.__routes = {}
        
    @public
    def getId(self):
        return self.__id
    
    @public
    def addRoute(self, route):
        if not self.__routes.has_key(route.getType()):
            self.__routes[route.getType()] = {}
        if not self.__routes[route.getType()].has_key(route.getElementId()):
            self.__routes[route.getType()][route.getElementId()] = []
        if not route in self.__routes[route.getType()][route.getElementId()]:
            self.__routes[route.getType()][route.getElementId()].append(route)
            print "Route ", self.__peer.getId(), route.getElementId(), route.getTrace(), " added."
        
    @public
    def getPeer(self):
        return self.__peer