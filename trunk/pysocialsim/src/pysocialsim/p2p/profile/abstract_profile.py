from pysocialsim.base.object import Object
from pysocialsim.p2p.peer.i_peer import IPeer
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type

class AbstractProfile(Object):
    
    def __init__(self, peer):
        raise NotImplementedError()
    
    def initialize(self, peer):
        self.__peer = peer
        self.__folksonomies = {}
        self.__interests = {0: []}
    
    @public
    def addFolksonomy(self, folksonomy):
        if not self.__folksonomies.has_key(folksonomy):
            self.__folksonomies[folksonomy] = 0
        self.__folksonomies[folksonomy] += 1
        return folksonomy
    
    @public
    def removeFolksonomy(self, folksonomy):
        if not self.__folksonomies.has_key(folksonomy):
            raise StandardError()
        if self.__folksonomies[folksonomy] > 0:
            self.__folksonomies[folksonomy] -= 1
        else:
            del self.__folksonomies[folksonomy]
            
        return folksonomy
    
    @public
    @return_type(int)
    def countFolksonomies(self):
        return len(self.__folksonomies)
    
    @public
    def match(self, profile, strategy):
        return strategy.execute(self, profile)
    
    @public
    @return_type(dict)
    def getFolksonomies(self):
        return self.__folksonomies
    
    @public
    @return_type(IPeer)
    def getPeer(self):
        return self.__peer
    
    @public
    def addInterest(self, interest):
        self.__interests[interest.getType()].append(interest)
        return interest
    
    @public
    def matchInterests(self, advertisement, interestMatchingStrategy):
        interestMatchingStrategy.setProfile(self)
        for interest in self.__interests[advertisement.getType()]:
            interestMatchingStrategy.execute(interest, advertisement)            