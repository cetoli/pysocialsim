from pysocialsim.p2p.profile.abstract_interest import AbstractInterest

class DefaultInterest(AbstractInterest):
    
    def __init__(self, type, initialThreshold, limitThreshold, folksonomies):
        self.initialize(type, initialThreshold, limitThreshold, folksonomies)