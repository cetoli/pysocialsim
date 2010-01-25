"""
Defines the module with the implementation of NewSimplePeerSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.context.tags_map import TagsMap
from random import randint
from pysocialsim.common.p2p.peer.context.context_id_generator import ContextIdGenerator
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.p2p.peer.profile.interest import Interest

class NewSimplePeerSimulationEventHandler(AbstractSimulationEventHandler):
    """
    Defines the implementation of NewSimplePeerSimulationEventHandler
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "NEW_SIMPLE_PEER")
    
    def execute(self):
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        simplePeer = network.getPeer(IPeerToPeerNetwork.SIMPLE_PEER, self.getSimulationEvent().getPeerId())
        
        event = self.getSimulationEvent()
        
        map = TagsMap.getMap()
        
        concept = map.keys()[randint(0, len(map.keys()) - 1)]
        tags = map[concept]
        
        interest = Interest(concept)
        for i in range(len(tags)):
            interest.registerTag(tags[randint(0, len(tags) - 1)]) 
        
        socialProfile = simplePeer.getSocialProfile()
        socialProfile.addInterest(interest)
        if simplePeer.join():
            simplePeer.setJoinTime(event.getPriority())
        
        return AbstractSimulationEventHandler.execute(self)
        