from pysocialsim.simulator.simulation.abstract_simulation import AbstractSimulation
from pysocialsim.base.decorator.public import public
from random import randint
from pysocialsim.network.peer.content.default_file import DefaultFile
from pysocialsim.network.peer.folksonomy.folksonomy_map import FolksonomyMap

class DefaultSimulation(AbstractSimulation):
    
    def __init__(self, network):
        self.initialize(network)
    
    @public
    def generateFiles(self):
        for fileId in range(self.getNumberOfFiles()):
            peerId = randint(0, self.getNetwork().countPeers() - 1)
            
            conceptMap = FolksonomyMap()
            concept = conceptMap.mapping.keys()[randint(0, len(conceptMap.mapping.keys()) - 1)]
            tags = conceptMap.mapping[concept]
            initial = randint(0, int(len(tags)/2))
            final = randint(int(len(tags)/2), len(tags) - 1)
            
            folks = []
            
            for j in range(initial, final):
                folks.append(tags[j])
            
            file = DefaultFile(fileId, concept, folks)
            
            peer = self.getNetwork().getPeer(peerId)
            peer.addFile(file)
            
            for f in file.getFolksonomies():
                peer.reputeContent(file.getConcept(), f, randint(0, 100))