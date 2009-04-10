from pysocialsim.network.peer.necessity.abstract_necessity import AbstractNecessity
from pysocialsim.network.peer.necessity.necessity_constants import NecessityConstants

class ContentNecessity(AbstractNecessity):
    
    def __init__(self, peer, minimumTrustDegree, maximumTrustDegree, maximumMatchingNumber):
        self.initialize(NecessityConstants.CONTENT, peer, minimumTrustDegree, maximumTrustDegree, maximumMatchingNumber)