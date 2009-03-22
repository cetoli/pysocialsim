from pysocialsim.network.peer.interest.abstract_interest import AbstractInterest

class DefaultInterest(AbstractInterest):
    
    def __init__(self, folksonomy):
        self.initialize(folksonomy)