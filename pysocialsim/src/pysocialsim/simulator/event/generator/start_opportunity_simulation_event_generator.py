from pysocialsim.simulator.event.abstract_simulation_event_generator import AbstractSimulationEventGenerator

class StartOpportunitySimulationventGenerator(AbstractSimulationEventGenerator):
    
    def __init__(self, average, time, opportunities):
        self.initialize(average, time, opportunities)
            
    def initialize(self, average, time, opportunities):
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
        self.__opportunities = opportunities
    
    def generateSimulationEvents(self):
        print "Generating START_OPPORTUNITY ."
        simulation = self.getSimulation()
        
        generatedEvents = 0
#        priority = self.__time
#        print "Generating START_OPPORTUNITY .."
#        for i in range(1, int(self.__average * 2) + 1):
#            distPoisson = (pow(self.__average, i) / factorial(i)) * pow(math.e, -self.__average)
#            times = round((simulation.getSimulationTime() / self.__time) * distPoisson)
#            for x in range(1, int(times)):
#                for j in range(i):
#                    event = StartOpportunitySimulationEvent("", priority)
#                    
#                    prioritiesLogFile = open("priorities.log", "a")
#                    prioritiesLogFile.write(str(priority)+"\n")
#                    prioritiesLogFile.close()
#                    
#                    simulation.registerSimulationEvent(event)
#                    generatedEvents += 1
#                    
#                    if generatedEvents == self.__opportunities:
#                        print "Generating START_OPPORTUNITY ..."
#                        print "Done. (" + str(generatedEvents) +" events were generated)"  
#                        return generatedEvents
#                
#                priority += self.__time
#        print "Generating START_OPPORTUNITY ..."
#        print "Done. (" + str(generatedEvents) +" events were generated)"        
        return generatedEvents