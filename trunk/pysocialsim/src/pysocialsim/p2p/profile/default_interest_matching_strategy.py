from pysocialsim.base.decorator.public import public

class DefaultInterestMatchingStrategy:
    
    @public
    def execute(self, interest, advertisement):
        count = 0
        for f in interest.getFolksonomies():
            if f in advertisement.getFolksonomies():
                count += 1
        if len(interest.getFolksonomies()) == 0:
            return 0
        else:            
            return (count * 100)/len(interest.getFolksonomies())