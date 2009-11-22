from pysocialsim.common.simulator.event.abstract_simulation_event_handler import AbstractSimulationEventHandler

class PushOpportunitySimulationEventHandler(AbstractSimulationEventHandler):
    
    def __init__(self):
        AbstractSimulationEventHandler.initialize(self, "PUSH_OPPORTUNITY")
    
    def execute(self):
        return AbstractSimulationEventHandler.execute(self)