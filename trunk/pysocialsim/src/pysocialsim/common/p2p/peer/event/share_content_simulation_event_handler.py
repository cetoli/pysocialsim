'''
Created on 02/02/2010

@author: fabricio
'''
from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.content.content import Content
from pysocialsim.common.p2p.peer.content.content_id_generator import ContentIdGenerator
from random import uniform

class ShareContentSimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "SHARE_CONTENT")
        
    def execute(self):
        simulation = self.getSimulation()
        network = simulation.getPeerToPeerNetwork()
        event = self.getSimulationEvent()
        simplePeer = network.getPeer(IPeerToPeerNetwork.SIMPLE_PEER, event.getPeerId())
        
        alpha = 1.8
        k = 1073741824
        
        content = Content(ContentIdGenerator.generateId(simplePeer), int(k/pow(uniform(0,1), 1/alpha)))
        
        simplePeer.shareContent(event.getPriority(), content, event.getParameter("opportunityId"))
        
        return AbstractSimulationEventHandler.execute(self)