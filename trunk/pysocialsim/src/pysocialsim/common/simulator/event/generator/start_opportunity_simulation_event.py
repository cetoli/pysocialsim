from pysocialsim.common.simulator.event.abstract_simulation_event import AbstractSimulationEvent

class StartOpportunitySimulationEvent(AbstractSimulationEvent):
    
    def __init__(self, peerId, priority):
        AbstractSimulationEvent.initialize(self, "START_OPPORTUNITY", peerId, priority)