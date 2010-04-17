from pysocialsim.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class PushOpportunitySimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "PUSH_OPPORTUNITY")
    
    def execute(self):
        print self.getHandle()
        
        return AbstractSimulationEventHandler.execute(self)