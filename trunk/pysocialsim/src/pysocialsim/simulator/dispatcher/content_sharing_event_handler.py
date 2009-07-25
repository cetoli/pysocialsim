from pysocialsim.simulator.dispatcher.abstract_event_handler import AbstractEventHandler
from pysocialsim.base.decorator.public import public
from pysocialsim.base.decorator.return_type import return_type
from pysocialsim.simulator.dispatcher.i_event_handler import IEventHandler
from pysocialsim.base.decorator.require import require
from pysocialsim.simulator.event.i_event import IEvent
from random import randint
from pysocialsim.p2p.folksonomy.folksonomy_map import FolksonomyMap
from pysocialsim.p2p.content.default_content import DefaultContent

class ContentSharingEventHandler(AbstractEventHandler):
    
    def __init__(self, simulation):
        self.initialize("SHARE_CONTENT", simulation)
    
    @public
    def clone(self):
        return ContentSharingEventHandler(self.getSimulation())
    
    def executeHandler(self, event):
        peer = event.getPeer()
        if not peer.isConnected():
            return
        size = randint(256, 1024)
        map = FolksonomyMap()
                    
        concept = map.mapping.keys()[randint(0, len(map.mapping.keys()) - 1)]
        initial = randint(0, (len(map.mapping[concept])/2) - 1)
        end = randint((len(map.mapping[concept])/2), len(map.mapping[concept]) - 1)
                      
        c = DefaultContent(randint(1, 1000000000), [], size)
                       
        for ix in range(initial, end):
            c.addFolksonomy(map.mapping[concept][ix])
                            
        peer.addContent(c)
