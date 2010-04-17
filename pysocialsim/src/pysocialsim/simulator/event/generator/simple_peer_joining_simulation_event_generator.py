"""
Defines the module with the implementation SimplePeerJoiningSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/09/2009
"""
from pysocialsim.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator

class SimplePeerJoiningSimulationEventGenerator(AbstractSimulationEventGenerator):
    """
    Defines the implementation of SimplePeerLeavingSimulationEventGenerator
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 13/09/2009
    """

    def __init__(self, alpha, minimum, peers):
        self.initialize(alpha, minimum, peers)
    
    def initialize(self, alpha, minimum, peers):
        AbstractSimulationEventGenerator.initialize(self)
        
        self.__alpha = alpha
        self.__minimum = minimum
        self.__peers = peers
        
    def generateSimulationEvents(self):
        print "Generating SIMPLE_PEER_JOIN ."
        simulation = self.getSimulation()
        simulator = simulation.getSimulator()
        scheduler = simulator.getScheduler()
        generatedEvents = 0
        print "Generating SIMPLE_PEER_JOIN .."
#        messagesLogFile = open("distPareto.log", "a")
#        network = simulation.getPeerToPeerNetwork()
#        for peer in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER):
#            lastTime = scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId())
#            time = self.__minimum/pow(uniform(0,1), 1/self.__alpha)
#            event = SimplePeerJoiningSimulationEvent(peer.getId(), int(time + lastTime))
#            simulation.registerSimulationEvent(event)
#            
#            scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId(), int(time + lastTime))
#            generatedEvents += 1
#            
#            line = str(time) 
#            messagesLogFile.write(str(line)+"\n")
#        messagesLogFile.close()
#        
#        print "Generating SIMPLE_PEER_JOIN ..."
#        print "Done. (" + str(generatedEvents) +" events were generated)"
        return generatedEvents      