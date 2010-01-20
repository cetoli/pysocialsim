from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.util.rotines import requires, pre_condition, factorial
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.simulator.event.generator.start_opportunity_simulation_event import StartOpportunitySimulationEvent
from pysocialsim.common.p2p.peer.context.opportunity import Opportunity
from pysocialsim.common.p2p.peer.context.context_id_generator import ContextIdGenerator
from pysocialsim.common.p2p.peer.context.i_context import IContext
import math

class StartOpportunitySimulationventGenerator(AbstractSimulationEventGenerator):
    
    def __init__(self, average, time, superPeers):
        self.initialize(average, time, superPeers)
            
    def initialize(self, average, time, superPeers):
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
        requires(superPeers, int)
        
        pre_condition(average, lambda x: x > 0)
        pre_condition(time, lambda x: x > 0)
        pre_condition(superPeers, lambda x: x > 0)
        
        self.__average = average
        self.__time = time
        self.__superPeers = superPeers
    
    @public    
    def generateSimulationEvents(self):
        simulation = self.getSimulation()
        simulator = simulation.getSimulator()
        scheduler = simulator.getScheduler()
        generatedEvents = 0
        peerCounter = 0
        network = simulation.getPeerToPeerNetwork()
        for peer in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER):
            lastTime = scheduler.unregisterTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId())
            nextLastTime = scheduler.unregisterTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId())
            priority = nextLastTime + self.__time
            for i in range(1, int(self.__average * 2) + 1):
                distPoisson = (pow(self.__average, i) / factorial(i)) * pow(math.e, -self.__average)
                times = round((simulation.getSimulationTime() / self.__time) * distPoisson)
                for x in range(1, int(times)):
                    for j in range(i):
                        event = StartOpportunitySimulationEvent(peer.getId(), priority)
                        
                        id = ContextIdGenerator.generateContextId(IContext.OPPORTUNITY, peer)
                        
                        opportunity = Opportunity(id)
                        opportunity.setStartTime(priority)
                        
                        contextManager = peer.getContextManager()
                        contextManager.registerContext(IContext.OPPORTUNITY, opportunity)
                        
                        event.registerParameter("opportunityId", id)
                        
                        simulation.registerSimulationEvent(event)
                        
                        print event.getPeerId(), event.getPriority()
                    priority += self.__time
                if not (priority > nextLastTime and priority <= lastTime):
                    break
            peerCounter += 1
            
            scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId(), nextLastTime)
            scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId(), lastTime)
            
            if peerCounter > self.__superPeers:
                break
                
            
        return 0