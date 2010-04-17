from pysocialsim.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator

class EndOpportunitySimulationEventGenerator(AbstractSimulationEventGenerator):
    
    def __init__(self, shape, scale, peers):
        self.initialize(shape, scale, peers)
    
    def initialize(self, shape, scale, peers):
             
        AbstractSimulationEventGenerator.initialize(self)
        
        self.__shape = shape
        self.__scale = scale
        self.__peers = peers
        
    def generateSimulationEvents(self):
        simulation = self.getSimulation()
        generatedEvents = 0
        peerCounter = 0
#        network = simulation.getPeerToPeerNetwork()
#        
#        for peer in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER):
#            contextManager = peer.getContextManager()
#            opportunities = contextManager.getContexts(IContext.OPPORTUNITY)
#            for opportunity in opportunities:
#                time = (self.__scale*pow((-math.log(uniform(0,1))), 1/self.__shape)) * 3600
#                opportunity.setDurationTime(time)
#                
#                event = EndOpportunitySimulationEvent(peer.getId(), int(opportunity.getEndTime()))
#                event.registerParameter("opportunityId", opportunity.getId())
#                
#                prioritiesLogFile = open("priorities.log", "a")
#                prioritiesLogFile.write(str(int(opportunity.getEndTime()))+"\n")
#                prioritiesLogFile.close()
#                
#                print opportunity.getId(), opportunity.getStartTime(), opportunity.getDurationTime(), opportunity.getEndTime()
#                simulation.registerSimulationEvent(event)
#                
#                generatedEvents += 1
#            
#            peerCounter += 1
#            
#            if peerCounter == self.__peers:
#                break
        
        return generatedEvents