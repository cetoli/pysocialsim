from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class EndOpportunitySimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "END_OPPORTUNITY")
        
    def execute(self):
        print self.getHandle()