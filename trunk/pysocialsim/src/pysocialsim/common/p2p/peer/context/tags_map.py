"""
Defines the module with TagsMap class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 06/11/2009
"""
from pysocialsim.common.base.object import Object

class TagsMap(Object):
    
    def __init__(self):
        raise NotImplementedError()
    
    @classmethod
    def getMap(self):
        mapping = {}
        
        mapping["design"] = ["inspiration", "webdesign", "web", "blog", "art", "portfolio", "illustration", "typography", "photoshop", "graphic", "graphics"]
        mapping["blog"] = ["design", "inspiration", "music", "art", "web2.0", "webdesign", "blogs", "photography", "wordpress", "web", "news"]
        mapping["video"] = ["youtube", "software", "tv", "music", "tools", "web2.0", "streaming", "tutorial", "videos", "media", "funny"]
        mapping["software"] = ["tools", "windows", "mac", "opensource", "freeware", "osx", "free", "programming", "linux", "web", "web2.0"]
        mapping["tools"] = ["web2.0", "software", "web", "webdesign", "twitter", "windows", "tool", "utilities", "resources", "reference", "online"]
        mapping["music"] = ["mp3", "blog", "download", "audio", "video", "guitar", "software", "free", "web2.0", "youtube", "radio"]
        mapping["programming"] = ["development", "tutorial", "software", "python", "reference", "java", "php", "web", "opensource", "javascript", "webdev"]
        mapping["webdesign"] = ["design", "web", "inspiration", "css", "webdev", "resources", "tutorials", "tutorial", "tools", "web2.0", "photoshop"]
        mapping["reference"] = ["resources", "tools", "programming", "webdesign", "tutorial", "research", "design", "tips", "web", "tutorials", "howto"]
        mapping["tutorial"] = ["photoshop", "webdesign", "tutorials", "programming", "howto", "tips", "reference", "web", "design", "photography", "css"]
        mapping["art"] = ["design", "inspiration", "illustration", "photography", "blog", "portfolio", "artist", "gallery", "graphics", "painting", "culture"]
        mapping["web"] = ["webdesign", "tools", "web2.0", "design", "webdev", "software", "tutorial", "css", "tutorials", "tool", "resources"]
        mapping["howto"] = ["tutorial", "tips", "linux", "reference", "tutorials", "diy", "photography", "ubuntu", "photoshop", "programming", "software"]
        mapping["bioinformatics"] = ["eScience", "workflow", "bioinformatics", "blast", "fasta", "gene", "ontology", "biology", "DNA", "RNA", "phylogeny", "system"]
        mapping["oil"] = ["oil", "stratigraphy", "sequence", "workflow", "riser", "sediment", "gas"]
        
        return mapping