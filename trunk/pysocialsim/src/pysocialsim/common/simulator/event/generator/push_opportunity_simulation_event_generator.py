from pysocialsim.common.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
from pysocialsim.common.base.decorators import public
from pysocialsim.common.p2p.network.i_peer_to_peer_network import IPeerToPeerNetwork
from pysocialsim.common.p2p.peer.context.i_context import IContext
from pysocialsim.common.simulator.event.generator.push_opportunity_simulation_event import PushOpportunitySimulationEvent

class PushOpportunitySimulationEventGenerator(AbstractSimulationEventGenerator):
    
    def __init__(self, pushFrequency):
        self.initialize(pushFrequency)
        
    def initialize(self, pushFrequency):
        AbstractSimulationEventGenerator.initialize(self)
        
        self.__pushFrequency = pushFrequency
        
    @public    
    def generateSimulationEvents(self):
        simulation = self.getSimulation()
        generatedEvents = 0
        peerCounter = 0
        network = simulation.getPeerToPeerNetwork()
        
        for peer in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER):
            contextManager = peer.getContextManager()
            opportunities = contextManager.getContexts(IContext.OPPORTUNITY)
            for opportunity in opportunities:
                print opportunity.getId(), int(opportunity.getEndTime())/self.__pushFrequency
                for i in range(1, int(opportunity.getEndTime())/self.__pushFrequency):
                    prioritiesLogFile = open("priorities.log", "a")
                    prioritiesLogFile.write(str(opportunity.getStartTime() + (i * self.__pushFrequency))+"\n")
                    prioritiesLogFile.close()
                    event = PushOpportunitySimulationEvent(peer.getId(), opportunity.getStartTime() + (i * self.__pushFrequency))
                    event.registerParameter("opportunityId", opportunity.getId())
                    simulation.registerSimulationEvent(event)
                    generatedEvents += 1
                
        return generatedEvents