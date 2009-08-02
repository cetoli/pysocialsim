from pysocialsim.p2p.profile.abstract_social_cloud_view import AbstractSocialCloudView

class DefaultSocialCloudView(AbstractSocialCloudView):
    
    def __init__(self, id):
        self.initialize(id)