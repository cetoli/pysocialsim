from pysocialsim.base.decorator.public import public
from pysocialsim.p2p.profile.abstract_interest_matching_strategy import AbstractInterestMatchingStrategy
from pysocialsim.p2p.profile.default_social_matching import DefaultSocialMatching

class DefaultInterestMatchingStrategy(AbstractInterestMatchingStrategy):
    
    def __init__(self):
        self.initialize()
    
    @public
    def execute(self, interest, advertisement):
        count = 0
        for f in interest.getFolksonomies():
            if f in advertisement.getFolksonomies():
                count += 1
        if len(interest.getFolksonomies()) == 0:
            return
        threshold = (count * 100)/len(interest.getFolksonomies())
        if (threshold >= interest.getInitialThreshold()) and (threshold <= interest.getLimitThreshold()):
            socialMatching = DefaultSocialMatching(advertisement.getPeerId(), advertisement.getElementId(), threshold)
            interest.addSocialMatching(socialMatching)