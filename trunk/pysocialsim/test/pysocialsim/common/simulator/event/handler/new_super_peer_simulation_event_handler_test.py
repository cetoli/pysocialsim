"""
Defines the module with the unit test of NewSimplePeerSimulationEventHandler class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 17/09/2009
"""
from pysocialsim.common.simulator.simulation.i_simulation import ISimulation
from pysocialsim.common.simulator.event.handler.new_super_peer_simulation_event_handler import NewSuperPeerSimulationEventHandler
from pysocialsim.common.simulator.event.generator.new_super_peer_simulation_event import NewSuperPeerSimulationEvent
from pysocialsim.common.p2p.protocol.i_peer_to_peer_protocol import IPeerToPeerProtocol
from pymockobject.events import ReturnValue
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.topology.i_peer_to_peer_topology import IPeerToPeerTopology
from pysocialsim.common.p2p.topology.graph.i_node import INode
from pysocialsim.common.p2p.peer.i_peer import IPeer
import pymockobject

import unittest

class NewSuperPeerSimulationEventHandlerTest(unittest.TestCase):
    
    def testCreateClassInstance(self):
        self.assertTrue(NewSuperPeerSimulationEventHandler())
        handler = NewSuperPeerSimulationEventHandler()
        self.assertFalse(handler.getSimulation())
        self.assertFalse(handler.getSimulationEvent())
        self.assertEquals("NEW_SUPER_PEER", handler.getHandle())
        
    def testHandleSimulationEvent(self):
        handler = NewSuperPeerSimulationEventHandler()
        peerToPeerNetwork = pymockobject.create(IPeerToPeerNetwork)
        peerToPeerProtocol = pymockobject.create(IPeerToPeerProtocol)
        peerToPeerProtocol.join.will(ReturnValue(True))
        peerToPeerTopology = pymockobject.create(IPeerToPeerTopology)
        peerToPeerTopology.getNode.will(ReturnValue(pymockobject.create(INode)))
        peerToPeerProtocol.getPeerToPeerTopology.will(ReturnValue(peerToPeerTopology))
        peerToPeerNetwork.getPeerToPeerProtocol.expects(IPeerToPeerNetwork.SUPER_PEER).will(ReturnValue(peerToPeerProtocol))
        peerToPeerNetwork.getPeer.expects(IPeerToPeerNetwork.SUPER_PEER, "1").will(ReturnValue(pymockobject.create(IPeer)))
        simulation = pymockobject.create(ISimulation)
        simulation.getPeerToPeerNetwork.will(ReturnValue(peerToPeerNetwork))
        simulationEvent = NewSuperPeerSimulationEvent("1", 10)
        
        handler.init(simulation)
        
        self.assertEquals(simulation, handler.getSimulation())
        self.assertEquals(simulationEvent, handler.handleSimulationEvent(simulationEvent))
        self.assertTrue(simulationEvent.isHandled())