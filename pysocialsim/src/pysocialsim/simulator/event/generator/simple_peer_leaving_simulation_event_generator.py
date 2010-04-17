"""
Defines the module with the implementation SimplePeerLeavingSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 13/09/2009
"""
from pysocialsim.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator
class SimplePeerLeavingSimulationEventGenerator(AbstractSimulationEventGenerator):
    """
    Defines the implementation of SimplePeerLeavingSimulationEventGenerator
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 13/09/2009
    """

    def __init__(self, shape, scale, peers):
        self.initialize(shape, scale, peers)
    
    def initialize(self, shape, scale, peers):
        AbstractSimulationEventGenerator.initialize(self)
        
        self.__shape = shape
        self.__scale = scale
        self.__peers = peers
        
    def generateSimulationEvents(self):
        print "Generating SIMPLE_PEER_LEAVE ."
        simulation = self.getSimulation()
        simulator = simulation.getSimulator()
        scheduler = simulator.getScheduler()
        generatedEvents = 0
#        network = simulation.getPeerToPeerNetwork()
#        print "Generating SIMPLE_PEER_LEAVE .."
#        messagesLogFile = open("distWeibull.log", "a")
#        for peer in network.getPeers(IPeerToPeerNetwork.SIMPLE_PEER):
#            lastTime = scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId())
#            time = (self.__scale*pow((-math.log(uniform(0,1))), 1/self.__shape)) * 3600
#            
#            scheduler.registerTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId(), int((lastTime + time)))
#            event = SimplePeerLeavingSimulationEvent(peer.getId(), scheduler.getTimeForPeer(IPeerToPeerNetwork.SIMPLE_PEER, peer.getId()))
#            simulation.registerSimulationEvent(event)
#            generatedEvents += 1
#            
#            line = str(time) 
#            messagesLogFile.write(str(line)+"\n")
#        messagesLogFile.close()
#            
#        print "Generating SIMPLE_PEER_LEAVE ..."
#        print "Done. (" + str(generatedEvents) +" events were generated)"
        return generatedEvents      