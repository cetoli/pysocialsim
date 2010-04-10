"""
Defines the module with the implementation of NewSimplePeerSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.util.rotines import requires, pre_condition, factorial
from pysocialsim.common.base.decorators import public
from pysocialsim.common.simulator.event.generator.new_simple_peer_simulation_event import NewSimplePeerSimulationEvent
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.peer_id_generator import PeerIdGenerator
from pysocialsim.common.p2p.peer.simple_peer import SimplePeer
import math

class NewSimplePeerSimulationEventGenerator(AbstractSimulationEventGenerator):
    """
    Defines the implementation of NewSimplePeerSimulationEventGenerator. This generator uses
    poisson distribution to define the appearance of new super peers in distributed system.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

    def __init__(self, average, time, peers):
        self.initialize(average, time, peers)

    def initialize(self, average, time, peers):
        """
        Initializes the simulation event generator.
        @param average: the average of new super peers appearance.
        @type average: a float
        @param time: frequence of new super peers appearance
        @type time: an int
        @param superPeers: maximum number of new superpeers
        @type superPeers: an int 
        @rtype: NoneType
        """
        AbstractSimulationEventGenerator.initialize(self)
        
        requires(average, float)
        requires(time, int)
        requires(peers, int)
        
        pre_condition(average, lambda x: x > 0)
        pre_condition(time, lambda x: x > 0)
        pre_condition(peers, lambda x: x > 0)
        
        self.__average = average
        self.__time = time
        self.__peers = peers
    
    @public    
    def generateSimulationEvents(self):
        print "Generating NEW_SIMPLE_PEER ."
        simulation = self.getSimulation()
        simulator = simulation.getSimulator()
        scheduler = simulator.getScheduler()
        generatedEvents = 0
        priority = 0
        peer = 0
        print "Generating NEW_SIMPLE_PEER .."
        for i in range(1, int(self.__average * 2) + 1):
            distPoisson = (pow(self.__average, i) / factorial(i)) * pow(math.e, -self.__average)
            times = round((simulation.getSimulationTime() / self.__time) * distPoisson)
            for x in range(1, int(times)):
                priority += self.__time
                for j in range(i):
                    peer += 1
                    simplePeer = SimplePeer(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SIMPLE_PEER), simulation.getPeerToPeerNetwork())
                    
                    peersLogFile = open("peers.log", "a")
                    peersLogFile.write(simplePeer.getId()+"\n")
                    peersLogFile.close()
                    
                    prioritiesLogFile = open("priorities.log", "a")
                    prioritiesLogFile.write(str(priority)+"\n")
                    prioritiesLogFile.close()
                    
                    event = NewSimplePeerSimulationEvent(simplePeer.getId(), priority)
                    simulation.registerSimulationEvent(event)
                    generatedEvents += 1
                    scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, simplePeer.getId(), priority)
                    if self.__peers == peer:
                        print "Generating NEW_SIMPLE_PEER ..."
                        print "Done. (" + str(generatedEvents) +" events were generated)"
                        return generatedEvents
        
        print "Generating NEW_SIMPLE_PEER ..."
        print "Done. (" + str(generatedEvents) +" events were generated)"
        
        return generatedEvents