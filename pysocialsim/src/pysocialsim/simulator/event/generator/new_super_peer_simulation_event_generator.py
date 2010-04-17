"""
Defines the module with the implementation of NewSuperPeerSimulationEventGenerator class.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 12/09/2009
"""
from pysocialsim.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator

class NewSuperPeerSimulationEventGenerator(AbstractSimulationEventGenerator):
    """
    Defines the implementation of NewSuperPeerSimulationEventGenerator. This generator uses
    poisson distribution to define the appearance of new super peers in distributed system.
    @author: Fabricio
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com 
    @since: 12/09/2009
    """

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
        
        self.__average = average
        self.__time = time
        self.__superPeers = superPeers
    
    def generateSimulationEvents(self):
        print "Generating NEW_SUPER_PEER ."
        
        simulation = self.getSimulation()
        generatedEvents = 1
#        priority = 1
#        superPeer = SuperPeer(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER), simulation.getPeerToPeerNetwork())
#        aux = 1
#        
#        event = NewSuperPeerSimulationEvent(superPeer.getId(), priority)
#        
#        prioritiesLogFile = open("priorities.log", "a")
#        prioritiesLogFile.write(str(priority)+"\n")
#        prioritiesLogFile.close()
#        
#        peersLogFile = open("peers.log", "a")
#        peersLogFile.write(superPeer.getId()+"\n")
#        peersLogFile.close()
#        
#        print "Generating NEW_SUPER_PEER .."
#        
#        simulation.registerSimulationEvent(event)
#        for i in range(1, int(self.__average * 2) + 1):
#            distPoisson = (pow(self.__average, i) / factorial(i)) * pow(math.e, -self.__average)
#            times = round(((simulation.getSimulationTime()/3.5) / self.__time) * distPoisson)
#            for x in range(1, int(times)):
#                priority += self.__time
#                for j in range(i):
#                    aux += 1
#                    superPeer = SuperPeer(PeerIdGenerator.generatePeerId(IPeerToPeerNetwork.SUPER_PEER), simulation.getPeerToPeerNetwork())
#                    
#                    peersLogFile = open("peers.log", "a")
#                    peersLogFile.write(superPeer.getId()+"\n")
#                    peersLogFile.close()
#                    
#                    prioritiesLogFile = open("priorities.log", "a")
#                    prioritiesLogFile.write(str(priority)+"\n")
#                    prioritiesLogFile.close()
#                    
#                    event = NewSuperPeerSimulationEvent(superPeer.getId(), priority)
#                    simulation.registerSimulationEvent(event)
#                    generatedEvents += 1
#                    if self.__superPeers == aux:
#                        print "Generating NEW_SUPER_PEER ..."
#                        print "Done. (" + str(generatedEvents) +" events were generated)"
#                        return generatedEvents
#        
#        print "Generating NEW_SUPER_PEER ..."
#        print "Done. (" + str(generatedEvents) +" events were generated)"
                    
        return generatedEvents