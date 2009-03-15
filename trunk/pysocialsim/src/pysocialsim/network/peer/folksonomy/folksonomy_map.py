
class FolksonomyMap:
    
    def __init__(self):
        self.mapping = {}
        self.mapping["software"] = ["tools", "windows", "mac", "opensource", "programming", "web2.0", "web", "linux", "osx", "freeware", "free"]
        self.mapping["rss"] = ["atom", "feed", "news", "google", "html", "web2.0", "reader", "software"]
        self.mapping["web2.0"] = ["tools", "web", "webdesign", "technology", "software", "social", "socialnetworking", "webdev", "socialmedia", "education", "ajax", "xml", "framework", "blog", "wiki"]
        self.mapping["e-science"] = ["imported", "openaccess", "geosciences", "facetedbrowsing", "europe", "bioinformatics", "semanticweb", "nsf", "cyberinfrastructure", "astronomy", 
                                     "workflow", "software", "opensource", "java", "grid", "tools", "science", "webservices", "programming", "xml"]
        self.mapping["cell"] = ["umts", "wcdma", "ev-do", "3g", "broadband"]
        self.mapping["programming"] = ["net", "RUP", "agile", "ajax", "architecture", "build", "checkstyle", "comet", "community",
                                       "controls", "patterns", "design", "design patters", "database", "development", "dojo", "eclipse",
                                       "extension", "firefox", "free", "freelance", "grid", "gridcomputing", "gui", "guide", "http",
                                       "ide", "java", "javascript", "ruby", "python", "jobs", "language", "library", "mac", "messaging",
                                       "methodology", "metrics", "networking", "opensource", "osx", "outsourcing", "parallel", "plugin", 
                                       "protocol1", "reference", "regex", "resources", "scaling", "schema", "server", "p2p", "servlet",
                                       "software", "swing", "toolkit", "tools", "translation", "tutorial", "tutorials", "ui", "unix", "vb",
                                       "versioncontrol", "virtualization", "visualbasic", "web3", "web2", "webdev", "windows", "xml"]
        self.mapping["science"] = ["3d1", "animals", "anthropology", "architecture", "art4", "article5", "articles", "astronomy", "attraction", "bias",
                                   "biology5", "blog2", "blogs", "body4", "book", "books", "brain8", "brains", "brainteasers", "business6", "cancer",
                                   "career", "charts", "cognition", "cognitive" , "cognitivescience", "cogsci", "color", "colors", "colortheory", "colorwheel",
                                   "community", "computer", "computers", "computing", "coolstuff", "creative", "creativity", "credibility", "culture",
                                   "data", "decisionmaking", "decisions", "design", "development", "dna", "drugs", "eclectic", "ecommerce", "education", 
                                   "einstein", "entrepreneurship", "ergonomics", "essay", "essays", "evolution", "experiment", "experiments", "eyes", "feynman",
                                   "finance", "fitts", "freakonomics", "funny", "future", "game", "geek", "genetics", "gibson", "graphing", "graphs", "happiness",
                                   "happinessatwork", "health", "history", "human", "humaninterface", "humor", "ideas", "illusions", "industrialdesign", "innovation",
                                   "innovative", "inspiration", "inspiring", "interesting", "internet", "invention", "jfs", "jobs", "justplaincool", "learning", 
                                   "life", "love", "marketing", "math", "medicine", "metaphor", "mind", "MIT", "money", "mustread", "nature", "net", "neuromarketing",
                                   "neuroscience", "news", "perception", "philosophy", "photography", "physics", "politics", "programming", "programmingtheory", 
                                   "psychology", "puzzle", "rabies", "reference", "religion", "research", "reviews", "scary", "search", "self", "sex", "shopping", 
                                   "sight", "social", "society", "sociology", "spe", "statistics", "study"]