from pysocialsim.base.object import Object
from pysocialsim.base.decorator.public import public

class DefaultMatchingStrategy(Object):
    
    @public
    def execute(self, source, target):
        return 0