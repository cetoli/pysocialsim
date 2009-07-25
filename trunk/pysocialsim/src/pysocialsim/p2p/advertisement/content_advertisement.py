from pysocialsim.p2p.advertisement.abstract_advertisement import AbstractAdvertisement

class ContentAdvertisement(AbstractAdvertisement):
    
    def __init__(self, peerId, elementId, folksonomies, type):
        self.initialize("CONTENT_ADVERTISEMENT", peerId, elementId, folksonomies, type)