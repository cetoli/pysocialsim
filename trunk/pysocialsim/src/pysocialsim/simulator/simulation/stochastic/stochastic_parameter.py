from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type

class StochasticParameter(Object):
    
    def __init__(self, elements, time):
        self.initialize(elements, time)
        
    def initialize(self, elements, time):
        self.__elements = elements
        self.__time = time
    
    @public
    def getNumberOfElements(self):
        return self.__elements
    
    @public
    def getTime(self):
        return self.__time