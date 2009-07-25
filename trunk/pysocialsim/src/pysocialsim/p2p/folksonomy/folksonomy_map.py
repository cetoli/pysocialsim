class FolksonomyMap:
    
    def __init__(self):
        self.mapping = {}
        self.mapping["design"] = ["inspiration", "webdesign", "web", "blog", "art", "portfolio", "illustration", "typography", "photoshop", "graphic", "graphics"]
        self.mapping["blog"] = ["design", "inspiration", "music", "art", "web2.0", "webdesign", "blogs", "photography", "wordpress", "web", "news"]
        self.mapping["video"] = ["youtube", "software", "tv", "music", "tools", "web2.0", "streaming", "tutorial", "videos", "media", "funny"]
        self.mapping["software"] = ["tools", "windows", "mac", "opensource", "freeware", "osx", "free", "programming", "linux", "web", "web2.0"]
        self.mapping["tools"] = ["web2.0", "software", "web", "webdesign", "twitter", "windows", "tool", "utilities", "resources", "reference", "online"]
        self.mapping["music"] = ["mp3", "blog", "download", "audio", "video", "guitar", "software", "free", "web2.0", "youtube", "radio"]
        self.mapping["programming"] = ["development", "tutorial", "software", "python", "reference", "java", "php", "web", "opensource", "javascript", "webdev"]
        self.mapping["webdesign"] = ["design", "web", "inspiration", "css", "webdev", "resources", "tutorials", "tutorial", "tools", "web2.0", "photoshop"]
        self.mapping["reference"] = ["resources", "tools", "programming", "webdesign", "tutorial", "research", "design", "tips", "web", "tutorials", "howto"]
        self.mapping["tutorial"] = ["photoshop", "webdesign", "tutorials", "programming", "howto", "tips", "reference", "web", "design", "photography", "css"]
        self.mapping["art"] = ["design", "inspiration", "illustration", "photography", "blog", "portfolio", "artist", "gallery", "graphics", "painting", "culture"]
        self.mapping["web"] = ["webdesign", "tools", "web2.0", "design", "webdev", "software", "tutorial", "css", "tutorials", "tool", "resources"]
        self.mapping["howto"] = ["tutorial", "tips", "linux", "reference", "tutorials", "diy", "photography", "ubuntu", "photoshop", "programming", "software"]
        