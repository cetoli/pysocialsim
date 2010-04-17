from pysocialsim.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class StartOpportunitySimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "START_OPPORTUNITY")
    
    def execute(self):
        print self.getHandle()
        
        return AbstractSimulationEventHandler.execute(self)
        